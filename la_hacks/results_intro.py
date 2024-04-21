import reflex as rx
from la_hacks.state import State

class CircleColor(rx.State):
    colors = [
        "red",
        "yellow",
        "green",
    ]


def intro() -> rx.Component:
    return rx.cond(
        True,
        rx.flex(
            rx.box(
                rx.image(
                    src="/tea.png",
                    width="100%",
                    style={
                        "height": "20vh", 
                        "objectFit": "cover",
                        "paddingLeft": "2rem",
                        "paddingRight": "2rem",
                    }
                ),
            ),
            rx.box(
                rx.heading(
                "Pure Leaf Tea",
                style={
                    "fontFamily": "Montserrat, sans-serif",
                    "fontWeight": "550",
                    "fontSize": "2rem",  # Base responsive size
                    "letterSpacing": "0.2px",
                    "textAlign": "left",
                    "color": "#92977E",
                    "paddingTop": "0.5rem",  # Adds space above the text
                    "paddingBottom": "1rem",  # Adds space below the text
                    "paddingLeft": "2rem",
                    "paddingRight": "2rem",
                },
                class_name="sm:text-sm md:text-md lg:text-lg fade-in-text",
                ),
                rx.box(
                    rx.text(rx.text.strong("Brand: "), "Zhenda"),
                    rx.text(rx.text.strong("Ecoscore: "), "B"),
                    rx.text(rx.text.strong("Ethics Score: "), "71"),
                    rx.text(rx.text.strong("Carbon Footprint: "), "69 g"),
                    style={
                    "fontFamily": "Roboto, sans-serif",  # Using Roboto as specified
                    "fontWeight": "200",  # Regular style
                    "fontSize": "0.8rem",  # Set font size to 16px
                    "letterSpacing": "normal",  # Normal letter spacing
                    "textAlign": "left",
                    "color": "#505050",
                    "paddingTop": "5px",  # Adds space above the text
                    "paddingBottom": "15px",  # Adds space below the text
                    "paddingLeft": "2rem",
                    "paddingRight": "2rem",
                    },
                    class_name="sm:text-md md:text-lg lg:text-xl fade-in-text",
                ),
                width="100%"
            ),
            
            class_name="bg-[#F3EFE3]",
            width="100%",
            spacing="6",
        )
    )