import sys

from loguru import logger

from aaltofood.controller import Controller
from aaltofood.model import ModelBasic
from aaltofood.restraunt import SodexoComputerScience, TUASRestaurant
from aaltofood.view import ConsoleView


def main():
    sodexo = SodexoComputerScience(
        name="Sodexo",
        location="Computer science building",
        url="https://www.sodexo.fi/en/ruokalistat/output/daily_json/6754/",
    )
    tuas = TUASRestaurant(
        name="TUAS",
        location="Electerical Engineering",
        url="https://www.foodandco.fi/modules/json/json/Index?costNumber=0199&language=en",
    )

    model = ModelBasic([sodexo, tuas])
    view = ConsoleView()
    controller = Controller(model, view)
    controller.show_menu()


if __name__ == "__main__":
    logger.add(
        sys.stdout,
        colorize=True,
        format="<green>{time}</green> <level>{message}</level>",
    )
    main()
