from reflex import App, Component
import reflex as rx



def landing_page() -> rx.Component:
    text_size = "5"
    """Create the main view for the Reflex landing page."""
    return rx.flex(
        rx.flex(
            rx.container(
                rx.image(src="/icons/landing.webp", width="100%", style={"height": "135%", "object-fit": "cover"}),
                justify="center",
            ),
            rx.text(
                "Welcome to environmental scanner! Get started with your first scan!",
                style={
                    "font-family": "Montserrat, sans-serif",
                    "font-weight": "500",
                    "font-size": "18px",
                    "letter-spacing": "0.5px",
                    "text-align": "center",
                    "color": "#505050",
                    "margin-top": "120px",
                },
            ),
            align="center",  # Aligns children to the start of the cross axis, i.e., the top of the container
            width="100%",
            direction="column",
            spacing="4",  # Adjust the spacing value as needed for gap between items
        ),
        rx.html(
                """
                <style>
                    .btn-rumble {
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
                <button class="btn-rumble bg-[#474448]" onclick="window.location.href='/scanner';">
                    <img src="/icons/tree.svg" alt="Tree Icon">Let's rumble!
                </button>
                """,
                align="center",
            ),

        align="center",  # Aligns children to the start of the cross axis, i.e., the top of the container
        width="100%",
        direction="column",
        spacing="9",
        height="100vh",
        class_name="bg-[#FFFAE2]",
    )

