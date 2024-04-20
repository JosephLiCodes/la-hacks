import reflex as rx
from la_hacks.json_parser import get_product_info


def results(upc) -> rx.Component:
    product_info = get_product_info(upc)
    if isinstance(product_info, str):  # Error case
        return rx.center(rx.heading(product_info))
    
    co2_formatted = f"{float(product_info['co2']):.2f}".rstrip('0').rstrip('.') if product_info['co2'] != "unknown" else "unknown"
    eco_grade_upper = product_info['eco_grade'].upper()
    
    return rx.center(
        rx.box(
            rx.image(src=product_info['image_url']),
            rx.heading(product_info['name']),
            rx.text(f"Brand: {product_info['brand']}"),
            rx.text(f"Eco Grade: {eco_grade_upper}"),
            rx.text(f"Carbon Footprint: {co2_formatted} g"),
            rx.accordion.root(
                rx.accordion.item(
                    header="Additives",
                    content=rx.list.unordered(
                        items=product_info['additives']
                    ),
                    font_size="3em"
                ),
                collapsible=True,
            ),
            rx.accordion.root(
                rx.accordion.item(
                    header="Ingredients",
                    content=rx.list.unordered(
                        items=product_info['ingredients']
                    ),
                    font_size="3em"
                ),
                collapsible=True,
            ),
        )
    )

