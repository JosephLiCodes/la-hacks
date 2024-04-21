from typing import List, Dict, Union
import reflex as rx
from la_hacks.json_parser import get_product_info
from la_hacks.gemini_wrapper import fetch_esg_data
from collections import defaultdict

class State(rx.State):
    cached:  dict = {}

    @rx.var
    def get_upc(self) -> Dict[str, Union[List[str]]]:
        upc = self.router.page.params.get('upc', 'no upc')
        if upc != 'no upc':
            product_info = get_product_info(upc)
            return {
                'image_url': product_info['image_url'],
                'name': product_info['name'],
                'brand': product_info['brand'],
                'additives': product_info['additives'],
                'ingredients': product_info['ingredients'],
                'eco_grade': product_info['eco_grade'],
                'co2': product_info['co2'],
            }
        return {
            'image_url': '',
            'name': '',
            'brand': [],
            'additives': [],
            'ingredients': [],
            'eco_grade': '',
            'co2': '',
        }

    @rx.var
    def get_good_and_bad_deeds(self) -> Dict[str, Union[List[str]]]:
        upc = self.router.page.params.get('upc', 'no upc')
        if upc != 'no upc':
            if upc in self.cached:
                return self.cached[upc]
            product_info = get_product_info(upc)
            if product_info['image_url'] == 'error':
                return {
                    'esg_good': [],
                    'esg_bad': [],
                    'ethics_score': '',
                }
            esg_good, esg_bad, ethics_score = fetch_esg_data(product_info['brand'])
            self.cached[upc] = {
                'esg_good': esg_good,
                'esg_bad': esg_bad,
                'ethics_score': ethics_score,
            }
            return self.cached[upc]
        return {
            'esg_good': [],
            'esg_bad': [],
            'ethics_score': '',
        }
