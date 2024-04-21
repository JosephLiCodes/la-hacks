"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from dotenv import load_dotenv
from la_hacks.scanner import scanner
from la_hacks.results_page import results
from la_hacks.landing_page import landing_page
load_dotenv()

text_size = "5"

def index() -> rx.Component:
    """Create the main view for the Reflex landing page."""
    return landing_page()

app = rx.App(
    theme=rx.theme(
        appearance="light", has_background=True, radius="medium", accent_color="gray"
    ),
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
    },
    stylesheets=[
        "/styles.css",
    ]
)

app.add_page(index)
app.add_page(scanner)
app.add_page(results, route='/results/[upc]')
