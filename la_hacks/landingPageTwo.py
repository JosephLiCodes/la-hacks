from reflex import App, Component
import reflex as rx

def page1():
    return rx.text("This is Page 1", align="center")

def page2():
    return rx.text("This is Page 2", align="center")

def page3():
    return rx.text("This is Page 3", align="center")

def landingPage():
    text_size = "5"
    return rx.flex(
        rx.container(
            rx.image(src="/logos/logo.png", height="4em"),
            style={
                "border_radius": "50%",  # Ensures style keys are Pythonic
                "border": "2px solid #56876D",
            },
            justify="center",
        ),
        rx.text(
            "Welcome to environmental scanner! Get started with your first scan!",
            size=text_size,
            color_scheme="green",
            align="center",
        ),
        padding="1em",
        align="center",
        width="100%",
        direction="column",
        spacing="4",
        margin_top="35%"
    ),
        rx.button(
            "Let's rumble!",
            on_click=lambda: rx.window_alert("Let's rumble!"),
            color_scheme="brown",
            padding="1em",
            align="center",
            width="100%",
            direction="column",
            spacing="9",
            height="100vh"
        )

class MainLandingPage(rx.Component):
    def __init__(self):
        super().__init__()
        self.current_page = 1  # Control current page

    def render(self):
        content = [page1, page2, page3, landingPage][self.current_page - 1]()
        return rx.vstack(
            content,
            rx.hstack(
                rx.button("Previous", on_click=self.go_prev, disabled=self.current_page == 1),
                rx.button("Next", on_click=self.go_next, disabled=self.current_page == 4),
                align="center",
                spacing="2"
            ),
            align="center",
            spacing="4"
        )

    def go_next(self):
        if self.current_page < 4:
            self.current_page += 1
        self.update()

    def go_prev(self):
        if self.current_page > 1:
            self.current_page -= 1
        self.update()

if __name__ == '__main__':
    app = rx.App(MainLandingPage())
    app.run()
