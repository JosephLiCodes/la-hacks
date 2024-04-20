from reflex import App, Component
import reflex as rx



def landing_page() -> rx.Component:
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
        rx.html(
                """
                <style>
                    .btn-rumble {
                        background-color: brown; /* Brown background */
                        color: white; /* White text */
                        padding: 10px 20px; /* Padding around the text */
                        font-size: 16px; /* Text size */
                        border-radius: 7px; /* Rounded corners */
                        cursor: pointer; /* Pointer cursor on hover */
                        display: flex; /* Flexbox for alignment */
                        align-items: center; /* Center items vertically */
                        justify-content: center; /* Center items horizontally */
                    }
                    .btn-rumble img {
                        margin-right: 10px; /* Space between the icon and text */
                        height: 20px; /* Icon size */
                    }
                </style>
                <button class="btn-rumble" onclick="window.location.href='/scanner';">
                    <img src="/icons/tree.svg" alt="Tree Icon">Let's rumble!
                </button>
                """,
                align="center",
            ),

        padding="1em",
        align="center",  # Aligns children to the start of the cross axis, i.e., the top of the container
        width="100%",
        direction="column",
        spacing="9",
        height="100vh",
    )

