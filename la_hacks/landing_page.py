import reflex as rx
from dotenv import load_dotenv
from la_hacks.scanner import scanner
from la_hacks.results_page import results
from reflex import App, Component

load_dotenv()

def landing_page() -> rx.Component:
    """Create the main view for the Reflex landing page."""
    return rx.flex(
        rx.flex(
            rx.container(
                rx.image(src="/icons/landing.webp", width="100%", style={"max-height": "50vh", "object-fit": "cover"}),
                justify="center",
                class_name="bg-[#F3EFE3]",
                width="100%"
            ),
            rx.text(
                "Welcome to environmental scanner! Get started with your first scan!",
                style={
                    "font-family": "Montserrat, sans-serif",
                    "font-weight": "500",
                    "font-size": "1rem",  # Base responsive size
                    "letter-spacing": "0.5px",
                    "text-align": "center",
                    "color": "#505050",
                    "padding-top": "2rem",  # Adds space above the text
                    "padding-bottom": "1rem",  # Adds space below the text
                },
                class_name="sm:text-sm md:text-lg lg:text-xl",  # Responsive text sizing
            ),
            align="center",
            width="100%",
            direction="column",
            spacing="4",
        ),
        rx.html(
                """
                <style>
                    .btn-rumble {
                        background-color: #474448; /* Button background color */
                        color: white; /* Button text color */
                        padding: 0.625rem 1.25rem; /* Button padding */
                        font-size: 1rem; /* Base responsive text size */
                        border-radius: 0.4375rem; /* Rounded corners */
                        cursor: pointer; /* Pointer cursor on hover */
                        display: flex; /* Flexbox for alignment */
                        align-items: center; /* Center items vertically */
                        justify-content: center; /* Center items horizontally */
                    }
                    .btn-rumble img {
                        margin-right: 0.625rem; /* Space between icon and text */
                        height: 1.25rem; /* Icon size */
                    }
                </style>
                <button class="btn-rumble" onclick="window.location.href='/scanner';">
                    <img src="/icons/tree.svg" alt="Tree Icon">Let's rumble!
                </button>
                """,
                align="center",
        ),
        align="center",
        width="100%",
        direction="column",
        spacing="9",
        height="100vh",
        class_name="bg-[#FFFAE2]",
    )

app = rx.App(
    theme=rx.theme(
        appearance="dark", has_background=True, radius="medium", accent_color="mint"
    ),
    tailwind={
        "theme": {
            "extend": {
                "screens": {
                    'sm': '640px',
                    'md': '768px',
                    'lg': '1024px',
                    'xl': '1280px',
                    '2xl': '1536px',
                }
            },
        },
        "plugins": ["@tailwindcss/typography"],
    }
)
app.add_page(landing_page)
app.add_page(scanner)
app.add_page(results, route='/results/[upc]')
