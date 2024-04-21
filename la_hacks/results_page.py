import reflex as rx
from la_hacks.json_parser import get_product_info
from la_hacks.state import State
from la_hacks.gemini_wrapper import fetch_esg_data


def results() -> rx.Component:
    return rx.cond(
        State.get_upc.to_string() != 'no upc',
        rx.box(
            rx.html(
                """
                <button onclick="window.location.replace('/scanner');">Back</button>
                """
            ),
            rx.image(src=State.get_upc['image_url']),
            rx.heading(State.get_upc['name']),
            rx.text(f"Brand: {State.get_upc['brand']}"),
            rx.text(f"Eco Grade: {State.get_upc['eco_grade']}"),
            rx.text(f"Carbon Footprint: {State.get_upc['co2']} g"),
            rx.text(f"POSITIVES:"),
            rx.list.unordered(
                items = State.get_good_and_bad_deeds['esg_good'],
                list_style_type="none",
            ),
            rx.text(f"NEGATIVES:"),
            rx.list.unordered(
                items = State.get_good_and_bad_deeds['esg_bad'],
                list_style_type="none",
            ),
            rx.accordion.root(
                        rx.accordion.item(
                            header="Additives",
                            content=rx.list.unordered(
                                items=State.get_upc['additives']
                            ),
                            font_size="3em",
                            style={"backgroundColor": "#505050"}
                        ),
                        collapsible=True,
                    ),
            rx.accordion.root(
                rx.accordion.item(
                    header="Ingredients",
                    content=rx.list.unordered(
                        items=State.get_upc['ingredients']
                    ),
                    font_size="3em",
                    style={"backgroundColor": "#505050"}
                ),
                collapsible=True,
            )
        )
    )