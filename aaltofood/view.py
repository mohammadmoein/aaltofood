from datetime import datetime
from typing import List

from rich.console import Console
from rich.table import Table


class ViewBasic:
    """basic render menu"""

    @staticmethod
    def show_menu(restaurants_name: str, courses: List[str]) -> None:
        """render the menu

        Args:
            restaurants_name (str): res
            courses (List[str]): course meal
        """
        pass


class ConsoleView(ViewBasic):
    """render menu in console

    Args:
        ViewBasic (_type_): implement Viewbasic show_menu method
    """

    @staticmethod
    def show_menu(restaurants_name: str, courses: List[str]) -> None:
        console = Console()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Date", style="dim", width=12)
        table.add_column("Food")
        table.add_column("Place", justify="right")
        today = datetime.today().strftime("%m-%d")
        for food_course in courses:
            table.add_row(today, food_course, restaurants_name)

        console.print(table)
