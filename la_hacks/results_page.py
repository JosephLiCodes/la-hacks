import reflex as rx
from la_hacks.json_parser import get_product_info
from la_hacks.state import State
from la_hacks.results_intro import intro
from la_hacks.gemini_wrapper import fetch_esg_data


def results() -> rx.Component:
    return rx.cond(
        State.get_upc.to_string() != 'no upc',
        rx.box(
            rx.html(
                """
                <button class="mb-2 text-blue-600" onclick="window.location.replace('/scanner');">← Back</button>
                """
            ),
            intro(),
            rx.accordion.root(
                rx.accordion.item(
                    header="Positives",
                    value="default",
                    content=rx.list.unordered(
                        rx.foreach(
                            State.get_good_and_bad_deeds['esg_good'],  # Assuming this should be additives or positives list
                            lambda ingredient: rx.list.item(
                                rx.icon("circle_check_big", color="green"),
                                f" {ingredient}",
                                class_name="text-black mb-2 border-b border-gray-200 border-opacity-50"
                            )
                        ),
                        list_style_type="none"
                    ),
                    font_size="3em",
                    class_name="w-full"
                ),
                rx.accordion.item(
                    header="Negatives",
                    content=rx.list.unordered(
                        rx.foreach(
                            State.get_good_and_bad_deeds['esg_bad'],
                            lambda ingredient: rx.list.item(
                                rx.icon("octagon_x", color="red"),
                                f" {ingredient}",
                                class_name="text-black mb-2 border-b border-gray-200 border-opacity-50"
                            )
                        ),
                        list_style_type="none"
                    ),
                    font_size="3em",
                    class_name="w-full"
                ),
                rx.accordion.item(
                    header="Additives",
                    content=rx.list.unordered(
                        items=State.get_upc['additives']
                    ),
                    font_size="3em",
                    class_name="w-full"
                ),
                rx.accordion.item(
                    header="Ingredients",
                    content=rx.list.unordered(
                        items=State.get_upc['ingredients']
                    ),
                    font_size="3em",
                    class_name="w-full"
                ),
                collapsible=True,
                variant="soft",
                class_name="w-full",
                default_value="default",
                exclusive=True,
                color_scheme=None,
            ),
            class_name="bg-[#FFFAE2] text-[#505050] p-0 h-[100vh]",
            style={"fontFamily": "Montserrat, sans-serif", "fontWeight": "200"}
        )
    )
