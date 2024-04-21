import reflex as rx
from la_hacks.json_parser import get_product_info
from la_hacks.state import State

def results() -> rx.Component:
    return rx.cond(
        State.get_upc.to_string() != 'no upc',
        rx.box(
            rx.html(
                """
                <button class="mb-2 text-blue-600" onclick="window.location.replace('/scanner');">← Back</button>
                """
            ),
            rx.image(src=State.get_upc['image_url']),
            rx.heading(State.get_upc['name']),
            rx.text(f"Brand: {State.get_upc['brand']}"),
            rx.text(f"Eco Grade: {State.get_upc['eco_grade']}"),
            rx.text(f"Carbon Footprint: {State.get_upc['co2']} g"),
            # Single accordion root with multiple items
            rx.accordion.root(
                rx.accordion.item(
                    header="Positives",
                    value="default",
                    content=rx.list.unordered(
                        rx.foreach(
                            State.get_upc['ingredients'],  # Assuming this should be additives or positives list
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
                            State.get_upc['ingredients'],
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
                color_scheme=None
            ),
            class_name="bg-[#FFFAE2] text-[#505050] p-0 h-[100vh]",
            style={"fontFamily": "Montserrat, sans-serif", "fontWeight": "200"}
        )
    )
