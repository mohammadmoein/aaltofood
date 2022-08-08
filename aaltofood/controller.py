from aaltofood.model import ModelBasic
from aaltofood.view import ViewBasic


class Controller:
    """Controller class to connect view and model"""

    def __init__(self, model: ModelBasic, view: ViewBasic) -> None:
        self.model = model
        self.view = view

    def show_menu(self):
        """render the menu"""
        courses = self.model.today_course()
        for name, items in courses.items():
            self.view.show_menu(name, items)
