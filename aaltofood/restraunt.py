from datetime import datetime
from urllib.parse import urljoin

import requests
from loguru import logger


class Restaurant(object):
    """
    Implement base class for restaurant
    """

    def __init__(self, name: str, location: str, url: str) -> None:
        self.name = name
        self.location = location
        self.url = url

    def get_menu(self, date: str):
        """Getting the menu from API. This should be implemented by base class"""
        pass

    def get_today_menu(self):
        """Return today menu to view"""
        pass

    def parse_menu(self, menu_dict: dict):
        """parse the response to list of courses

        Args:
            menu_dict (dict): response

        """
        pass

    def __repr__(self) -> str:
        return f"{self.name} locate at {self.location}"


class SodexoComputerScience(Restaurant):
    """Sodexo Restaurant"""

    def get_menu(self, date):
        api_url = urljoin(self.url, date)
        menu = {}
        try:
            resp = requests.get(api_url)
            resp.raise_for_status()
            menu = resp.json()
        except requests.exceptions.HTTPError as err:
            logger.error(err)

        return menu

    def get_today_menu(self):
        today = datetime.today().strftime("%Y-%m-%d")
        menu_dict = self.get_menu(today)
        courses = self.parse_menu(menu_dict)
        return courses

    def parse_menu(self, menu_dict: dict):
        courses = menu_dict.get("courses", {})
        return [c["title_en"] for c in courses.values()]


class TUASRestaurant(Restaurant):
    """TUAS Restaurant"""

    def get_menu(self, date: str):
        menu = {}
        try:
            resp = requests.get(self.url)
            resp.raise_for_status()
            menu = resp.json()
        except requests.exceptions.HTTPError as err:
            logger.error(err)

        return menu

    def get_today_menu(self):
        menu = self.get_menu(None)
        return self.parse_menu(menu)

    def parse_menu(self, menu_dict: dict):
        today = datetime.today().strftime("%Y-%m-%d")
        week_courses = menu_dict["MenusForDays"]
        today_menu = [
            w["SetMenus"] for w in week_courses if w["Date"].startswith(today)
        ][0]

        return [q["Components"][0] for q in today_menu if len(q["Components"]) > 0]
