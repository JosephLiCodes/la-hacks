from typing import List, Dict, Union
import reflex as rx
from la_hacks.json_parser import get_product_info

class State(rx.State):
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
                'co2': product_info['co2']
            }
        return {
            'image_url': '',
            'name': '',
            'brand': [],
            'additives': [],
            'ingredients': [],
            'eco_grade': '',
            'co2': ''
        }
