import reflex as rx 

class State(rx.State):
    @rx.var
    def get_upc(self) -> str:
        return self.router.page.params.get('upc', 'no upc')