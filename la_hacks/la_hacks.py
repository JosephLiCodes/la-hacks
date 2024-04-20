"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from dotenv import load_dotenv
from la_hacks.results_page import results
load_dotenv()

text_size = "5"

def index() -> rx.Component:
    """Create the main view for the Reflex landing page."""
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.spacer(),
                rx.heading("AI personal landing page", font_size="1.5em"),
                rx.spacer(),
                rx.color_mode.icon(),
                rx.color_mode.switch(),
                width="100%",
            ),
            rx.hstack(
                rx.vstack(
                    rx.text(
                        "Welcome to Reflex! Providing insights about Reflex, think about innovating in Python. Here are some quick links:",
                        size=text_size,
                    ),
                    rx.unordered_list(
                        rx.list_item(
                            rx.text("Website: ", weight="bold"),
                            rx.link(
                                "🔗 Reflex Site",
                                href="https://reflex.dev",
                            ),    
                        ),
                        rx.list_item(
                            rx.text("Twitter: ", weight="bold"),
                            rx.link(
                                "🔗 @getreflex",
                                href="https://twitter.com/getreflex",
                            ),
                        ),
                        rx.list_item(
                            rx.text("Github: ", weight="bold"),
                            rx.link(
                                "🔗 reflex-dev / reflex",
                                href="https://github.com/reflex-dev/reflex",
                            ),
                        ),
                        spacing="2",
                    ),
                    rx.text(
                        "Discover the power of Reflex with these commands:",
                    ),
                    rx.unordered_list(
                        rx.list_item(
                            rx.code("/tell me about Reflex"),
                        ),
                        rx.list_item(
                            rx.code("/how do I install Reflex"),
                        ),
                        spacing="2",
                    ),
                    width="65%",
                ),
                rx.container(
                    rx.color_mode_cond(
                        rx.image(src="/logos/light/reflex.svg", height="4em"),
                        rx.image(src="/logos/dark/reflex.svg", height="4em"),
                    ),
                    width="35%",
                ),
                spacing="7",
            ),
            rx.text("Powered by Reflex", size="3"),
            width="70em",
            background_color=rx.color("mauve", 1),
            padding="2em",
            align="center",
            border_radius="1em",
            margin_top="52px",
            margin_bottom="24px",
            margin_x="52px"
        ),
        width="100%",
        height="100vh",
        background="radial-gradient(circle at 22% 11%, rgba(62, 180, 137, .40), hsla(0, 0%, 100%, 0) 19%), radial-gradient(circle at 82% 25%, rgba(33, 150, 243, .36), hsla(0, 0%, 100%, 0) 35%), radial-gradient(circle at 25% 61%, rgba(250, 128, 114, .56), hsla(0, 0%, 100%, 0) 55%)",
    )

app = rx.App(
    theme=rx.theme(
        appearance="dark", has_background=True, radius="medium", accent_color="mint"
    ),
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
    }
)
app.add_page(index)
app.add_page(results, route='/results/[upc]')
