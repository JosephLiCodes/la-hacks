import reflex as rx
from la_hacks.json_parser import get_product_info
from la_hacks.state import State
from la_hacks.results_intro import intro
from la_hacks.gemini_wrapper import fetch_esg_data

def results() -> rx.Component:
    loader_html = rx.html("""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; width: 100%;">
            <div style="font-size: 24px; font-weight: bold; color: black; margin-bottom: 20px;" class="animate-pulse">EcoScan</div>
            <div class="loader animate-pulse"></div>
        </div>
        <style>
            .loader {
                width: 50px;
                aspect-ratio: 1;
                border: 2px solid #006400; /* Dark green color */
                display: grid;
                box-sizing: border-box;
                animation: l1 4s infinite linear;
            }
            .loader::before,
            .loader::after {
                content: "";
                grid-area: 1/1;
                margin: auto;
                width: 70.7%;
                aspect-ratio: 1;
                border: 2px solid #006400; /* Dark green color */
                box-sizing: content-box;
                animation: inherit;
            }
            .loader::after {
                width: 50%;
                aspect-ratio: 1;
                border: 2px solid #006400; /* Dark green color */
                animation-duration: 2s;
            }
            @keyframes l1 {
                100% {transform: rotate(1turn)}
            }
        </style>
    """)

    accordion_text_style = {"fontSize": "0.85rem"}
    return rx.box(
        rx.cond(
        (State.get_upc.to_string() != 'no upc') & (State.get_good_and_bad_deeds['esg_good'].length() != 0) & (State.get_good_and_bad_deeds['esg_bad'].length() != 0),
            rx.box(
                rx.html(
                    """
                    <button class="mb-2 ml-1 text-black" onclick="window.location.replace('/scanner');">← Back</button>
                    """
                ),
                intro(),
                rx.accordion.root(
                    rx.accordion.item(
                        header=rx.text("Positives", style={"fontSize": "1rem"}),  # Larger font size for headers
                        value="default",
                        content=rx.list.unordered(
                            rx.foreach(
                                State.get_good_and_bad_deeds['esg_good'],
                                lambda ingredient: rx.list.item(
                                    rx.icon("dot", color="#90EE90", size=24),
                                    rx.text(f" {ingredient}", style=accordion_text_style),
                                    class_name="text-black border-b border-gray-200 border-opacity-50"
                                )
                            ),
                            list_style_type="none"
                        ),
                        font_size="3em",
                        class_name="w-full"
                    ),
                    rx.accordion.item(
                        header=rx.text("Negatives", style={"fontSize": "1rem"}),
                        content=rx.list.unordered(
                            rx.foreach(
                                State.get_good_and_bad_deeds['esg_bad'],
                                lambda ingredient: rx.list.item(
                                    rx.icon("dot", color="#FF0000", size=24),
                                    rx.text(f" {ingredient}", style=accordion_text_style, class_name=""),
                                    class_name="text-black mb-2 border-b border-gray-200 border-opacity-50"
                                )
                            ),
                            list_style_type="none"
                        ),
                        font_size="3em",
                        class_name="w-full"
                    ),
                    rx.accordion.item(
                        header=rx.text("Additives", style={"fontSize": "1rem"}),
                        content=rx.list.unordered(
                            items=State.get_upc['additives'],
                            class_name="text-black"
                        ),
                        font_size="4em",
                        class_name="w-full"
                    ),
                    rx.accordion.item(
                        header=rx.text("Ingredients", style={"fontSize": "1rem"}),
                        content=rx.list.unordered(
                            items=State.get_upc['ingredients'],
                            class_name="text-black"
                        ),
                        font_size="4em",
                        class_name="w-full"
                    ),
                    rx.accordion.item(
                        header=rx.text("Alternatives", style={"fontSize": "1rem"}),
                        content=rx.list.unordered(
                            items=[
                                rx.list.item(rx.text("Patagonia")),
                                rx.list.item(rx.text("Allbirds")),
                                rx.list.item(rx.text("Seventh Generation")),
                                rx.list.item(rx.text("Dr. Bronner’s")),
                                rx.list.item(rx.text("Numi Organic Tea")),
                                rx.list.item(rx.text("New Belgium Brewing")),
                                rx.list.item(rx.text("Clif Bar and Company")),
                                rx.list.item(rx.text("Alara Wholefoods")),
                                rx.list.item(rx.text("Stonyfield Organic")),
                                rx.list.item(rx.text("The Ethical Dairy")),
                                rx.list.item(rx.text("Straus Family Creamery"))
                            ],
                            class_name="text-black"
                        ),
                        font_size="3em",
                        class_name="w-full"
                    ),
                    collapsible=True,
                    variant="ghost",
                    class_name="w-full",
                    default_value="default",
                    exclusive=True,
                    color_scheme=None,
                ),
                class_name="bg-[#FFFAE2] p-0 h-[100vh]",
                style={"fontFamily": "Montserrat, sans-serif", "fontWeight": "200"}
            )
        ),
        rx.cond(
            (State.get_upc.to_string() == 'no upc') | (State.get_good_and_bad_deeds['esg_good'].length() == 0) | (State.get_good_and_bad_deeds['esg_bad'].length() == 0),
            rx.box(
                rx.center(
                    loader_html
                ),
                class_name="bg-[#FFFAE2] p-0 h-[100vh]",
                style={"display": "flex", "alignItems": "center", "justifyContent": "center"}
            )
        )
    )
