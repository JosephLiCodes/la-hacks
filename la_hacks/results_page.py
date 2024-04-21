import reflex as rx
from la_hacks.json_parser import get_product_info
from la_hacks.state import State
from la_hacks.results_intro import intro


def results() -> rx.Component:
    return rx.cond(
        State.get_upc.to_string() != 'no upc',
        rx.box(
            rx.html(
                """
                <button onclick="window.location.replace('/scanner');">Back</button>
                """
            ),
            intro(),
            #negatives list 
            rx.text(f"POSITIVES:"),
            rx.list.unordered(
                items = State.get_upc['additives'],
                list_style_type="none",
            ),
            rx.text(f"NEGATIVES:"),
            rx.list.unordered(
                items = State.get_upc['ingredients'],
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
            ),
            class_name="bg-[#F3EFE3]"
        )
    )