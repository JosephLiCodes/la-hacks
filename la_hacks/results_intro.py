import reflex as rx
from la_hacks.state import State

def intro() -> rx.Component:
    return rx.cond(
        State.get_upc.to_string() != 'no upc',
        rx.flex(
            rx.box(
                rx.image(
                    src=State.get_upc['image_url'],
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
                State.get_upc['name'],
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
                    rx.text(rx.text.strong("Brand: "), State.get_upc['brand']),
                    rx.text(rx.text.strong("Eco Grade: "), State.get_upc['eco_grade']),
                    rx.text(rx.text.strong("Ethics Score: "), State.get_good_and_bad_deeds['ethics_score']),
                    rx.text(rx.text.strong("Carbon Footprint: "), State.get_upc['co2'], "g"),
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