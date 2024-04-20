import reflex as rx
from la_hacks.json_parser import get_product_info
from la_hacks.state import State


def results() -> rx.Component:
    return rx.cond(
        State.get_upc.to_string() != 'no upc',
        rx.box(
            rx.button(
                rx.icon(tag="arrow_left"),
                color_scheme="red",
                on_click=rx.redirect("/scanner")
            ),
            rx.image(src=State.get_upc['image_url']),
            rx.heading(State.get_upc['name']),
            rx.text(f"Brand: {State.get_upc['brand']}"),
            rx.text(f"Eco Grade: {State.get_upc['eco_grade']}"),
            rx.text(f"Carbon Footprint: {State.get_upc['co2']} g"),
            rx.accordion.root(
                rx.accordion.item(
                    header="Additives",
                    content=rx.list.unordered(
                        items=State.get_upc['additives']
                    ),
                    font_size="3em"
                ),
                collapsible=True,
            ),
            rx.accordion.root(
                rx.accordion.item(
                    header="Ingredients",
                    content=rx.list.unordered(
                        items=State.get_upc['ingredients']
                    ),
                    font_size="3em"
                ),
                collapsible=True,
            ),
        )
    )

