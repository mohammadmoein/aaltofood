from typing import List

from aaltofood.restraunt import Restaurant


class ModelBasic:
    """Model layer for getting the data"""

    def __init__(self, restaurants: List[Restaurant]) -> None:
        self.restaurants = restaurants

    def today_course(self):
        """Return today menu for all added restaurants

        Returns:
            dict: list of courses by restaurants name
        """
        data = {}
        for restaurant in self.restaurants:
            data[restaurant.name] = restaurant.get_today_menu()
        return data
