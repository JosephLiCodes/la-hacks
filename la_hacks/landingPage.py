from reflex import App, Component
import reflex as rx

def landingPage() -> rx.Component:
    text_size = "5"
    """Create the main view for the Reflex landing page."""
    return rx.flex(
        rx.flex(
            rx.container(
                rx.image(src="/logos/logo.png", height="4em",),
                style={
                    "borderRadius": "50%",   # This will make the container a circle
                    "border": "2px solid #56876D",  # Adjust the color and width as needed
                },
                justify="center",
            ),
            rx.text(
                "WelcomeHAHA to environmental scanner! Get started with your first scan!",
                size=text_size,
                color_scheme="green",
                align = "center",
            ),
            padding="1em",
            align="center",  # Aligns children to the start of the cross axis, i.e., the top of the container
            width="100%",
            direction="column",
            spacing="4",  # Adjust the spacing value as needed for gap between items
            margin_top="35%",
        ),
        rx.button(
            rx.icon(tag="tree-pine"),
            "Lets rumble!",
            color_scheme="brown", 
            on_click=rx.window_alert("Lets rumble!"),
        ),
        padding="1em",
        align="center",  # Aligns children to the start of the cross axis, i.e., the top of the container
        width="100%",
        direction="column",
        spacing="9",
        height="100vh",
    )

