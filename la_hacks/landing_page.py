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
                rx.image(src="/icons/landing.webp", width="100%", style={"height": "66vh", "objectFit": "cover"}),
                justify="center",
                class_name="bg-[#F3EFE3]",
                width="100%"
            ),
            rx.text(
                "Welcome to awesome scanner!",
                style={
                    "fontFamily": "Montserrat, sans-serif",
                    "fontWeight": "550",
                    "fontSize": "1rem",  # Base responsive size
                    "letterSpacing": "0.5px",
                    "textAlign": "center",
                    "color": "#505050",
                    "paddingTop": "2rem",  # Adds space above the text
                    "paddingBottom": "1rem",  # Adds space below the text
                    "paddingLeft": "4rem",
                    "paddingRight": "4rem",
                },
                class_name="sm:text-sm md:text-lg lg:text-xl",  # Responsive text sizing
            ),
            rx.text(
                "Easily scan product barcodes to uncover the environmental practices of the producing company and assess the product's impact. Make informed decisions that align with your values and well-being. Say hello to a more conscious shopping experience, effortlessly delivered at your fingertips.",
                style={
                    "fontFamily": "Roboto, sans-serif",  # Using Roboto as specified
                    "fontWeight": "200",  # Regular style
                    "fontSize": "12px",  # Set font size to 16px
                    "letterSpacing": "normal",  # Normal letter spacing
                    "textAlign": "center",
                    "color": "#505050",
                    "paddingTop": "5px",  # Adds space above the text
                    "paddingBottom": "15px",  # Adds space below the text
                    "paddingLeft": "2rem",
                    "paddingRight": "2rem",
                },
                class_name="sm:text-sm md:text-lg lg:text-xl",  # Responsive text sizing
            ),
            align="center",
            width="100%",
            direction="column",
            spacing="0",
        ),
        rx.html(
                """
                <style>
                    .btn-rumble {
                        background-color: #474448; /* Button background color */
                        color: white; /* Button text color */
                        padding: 0.625rem 1.25rem; /* Button padding */
                        font-size: 1rem; /* Base responsive text size */
                        border-radius: 1.875rem; /* More rounded corners */
                        cursor: pointer; /* Pointer cursor on hover */
                        display: flex; /* Flexbox for alignment */
                        align-items: center; /* Center items vertically */
                        justify-content: center; /* Center items horizontally */
                        box-shadow: 4px 3px 1px rgba(0, 0, 0, 0.3); /* Shadow */
                        font-family: 'Roboto' sans-serif; /* Font declaration */
                        "font-weight": "100";
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
        spacing="0",
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
