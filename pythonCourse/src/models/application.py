""" Application module"""

import os
from src.models.restaurant import Restaurant
from src.models.menu.drink import Drink
from src.models.menu.dessert import Dessert
from src.models.menu.food import Food
from src.challenges.between_break_lines import between_break_lines


class Application:
    """This class is responsible to manage the application"""

    def __init__(self):
        self._name = "Sabor Express"
        self._version = "1.0.0"
        self._author = "Henrique de Paula Rodrigues"
        self._restaurants = []
        self._options_available = [
            "1. Register restaurant",
            "2. List restaurant",
            "3. Activate restaurant",
            "4. Disable restaurant",
            "5. Evaluate restaurant",
            "6. Create a drink",
            "7. Create a food",
            "8. Create a dessert",
            "9. Show restaurant menu",
            "10. Exit app",
        ]

    def __str__(self):
        return (
            f"{self._name} was created by {self._author}"
            + f" and currently is in the version {self._version}"
        )

    def __evaluate_restaurant(self, restaurant_name):
        """Menu option for evaluate a restaurant"""
        existent_restaurant = self.__find_restaurant_by_name(
            restaurant_name=restaurant_name
        )
        if existent_restaurant is None:
            print("Cannot find any restaurant with that name.")
            self.__rerun_app()
        elif existent_restaurant.active == "✅":
            client_name = input(
                "To continue your restaurant evaluation, please type your name:\n"
            )
            try:
                score = int(
                    input(f"Type your score for the {restaurant_name} (0 to 5):\n")
                )
                existent_restaurant.evaluate(client=client_name, score=score)
            except AssertionError as exception:
                if isinstance(exception, AssertionError):
                    print(exception)
                    return
                print("You must type an integer number")
                return
            print("Thanks for help evaluate us!")
            return
        else:
            print("This restaurant is not active.")

    def bump_version(self, bump_type: str):
        """This method bump the version of the app"""
        [major, minor, patch] = self._version.split(".")
        if bump_type == "PATCH":
            patch = int(patch) + 1
        elif bump_type == "MINOR":
            minor = int(minor) + 1
        elif bump_type == "MAJOR":
            major = int(major) + 1
        else:
            print("invalid BUMP TYPE")
        self._version = f"{major}.{minor}.{patch}"

    def __find_restaurant_by_name(self, restaurant_name: str) -> Restaurant | None:
        """This method find a restaurant if in the base and returns it.
        Else returns None
        """
        for restaurant in self._restaurants:
            if restaurant.name == restaurant_name:
                return restaurant
        return None

    def __register_restaurant(self, restaurant: Restaurant):
        """This method register a restaurant"""
        existent_restaurant = self.__find_restaurant_by_name(
            restaurant_name=restaurant.name
        )
        if existent_restaurant is None:
            self._restaurants.append(restaurant)
            print("Restaurant registered")
            return
        print("Restaurant already exists")

    def __activate_restaurant(self, restaurant_name: str):
        """
        This method activate a restaurant if it exists
        """
        current_restaurant = self.__find_restaurant_by_name(
            restaurant_name=restaurant_name
        )
        if isinstance(current_restaurant, Restaurant):
            current_restaurant.activate()
            print(f"The restaurant {restaurant_name} is now active")
            return
        print(f"Cannot find restaurant called {restaurant_name}")

    def __add_drink_item_menu(self, restaurant_name):
        """create a drink item for the current restaurant menu"""
        current_restaurant = self.__find_restaurant_by_name(
            restaurant_name=restaurant_name
        )
        if isinstance(current_restaurant, Restaurant):
            drink_name = input("insert the drink name:\n")
            try:
                drink_price = float(input("insert the price:\n"))
                drink_size = int(input("insert the size (mL)\n"))
            except ValueError as exception:
                if isinstance(exception, ValueError):
                    print(
                        "wrong type was inserted, please for this input you should use numbers."
                    )
                    return
                print("An error occurs")
                return
            new_drink = Drink(name=drink_name, size=drink_size, price=drink_price)
            current_restaurant.create_option_menu(new_drink)
            return
        print("Cannot find a restaurant with that name.")

    def __add_dessert_item_menu(self, restaurant_name):
        """create a dessert item for the current restaurant menu"""
        current_restaurant = self.__find_restaurant_by_name(
            restaurant_name=restaurant_name
        )
        if isinstance(current_restaurant, Restaurant):
            dessert_name = input("insert the dessert name:\n")
            try:
                dessert_price = float(input("insert the price:\n"))
                dessert_weight = int(input("insert the weight (g)\n"))
            except ValueError as exception:
                if isinstance(exception, ValueError):
                    print(
                        "wrong type was inserted, please for this input you should use numbers."
                    )
                    return
                print("An error occurs")
                return
            new_dessert = Dessert(
                name=dessert_name, weight=dessert_weight, price=dessert_price
            )
            current_restaurant.create_option_menu(new_dessert)
            return
        print("Cannot find a restaurant with that name.")

    def __add_food_item_menu(self, restaurant_name):
        """create a food item for the current restaurant menu"""
        current_restaurant = self.__find_restaurant_by_name(
            restaurant_name=restaurant_name
        )
        if isinstance(current_restaurant, Restaurant):
            food_name = input("insert the food name:\n")
            try:
                food_price = float(input("insert the price:\n"))
                food_description = input("insert the description:\n")
            except ValueError as exception:
                if isinstance(exception, ValueError):
                    print(
                        "wrong type was inserted, please for this input you should use numbers."
                    )
                    return
                print("An error occurs")
                return
            new_food = Food(
                name=food_name, description=food_description, price=food_price
            )
            current_restaurant.create_option_menu(new_food)
            return
        print("Cannot find a restaurant with that name.")

    def __show_restaurant_menu(self, restaurant_name: str):
        """This method shows the restaurant menu"""
        current_restaurant = self.__find_restaurant_by_name(
            restaurant_name=restaurant_name
        )
        if isinstance(current_restaurant, Restaurant):
            current_restaurant.show_menu()
            self.__rerun_app()
            return
        print("Cannot find a restaurant with that name.")

    def __disable_restaurant(self, restaurant_name: str):
        """
        This method disable a restaurant if it exists
        """
        current_restaurant = self.__find_restaurant_by_name(
            restaurant_name=restaurant_name
        )
        if isinstance(current_restaurant, Restaurant):
            current_restaurant.disable()
            return f"The restaurant {restaurant_name} is now disabled"
        return f"Cannot find restaurant called {restaurant_name}"

    def __list_restaurants(self):
        """List all restaurants registered in the app"""
        print(
            "| name".ljust(23)
            + "| category".ljust(23)
            + "| active ".ljust(23)
            + " | score".ljust(23)
            + "|\n"
        )
        self.__print_line(character="*", repeat=93)

        for restaurant in self._restaurants:
            print(restaurant)
        print("\n")

    def __clear_prompt(self):
        """This function clear the prompt"""
        if os.name == "posix":
            os.system("clear")  # -> unix like Operation System
        else:
            os.system("cls")  # -> windows Operation System

    def __exit_app(self):
        """This function exit from the app"""
        self.__clear_prompt()
        print("the app is ended\n")

    def __show_options(self):
        """Show the options available in the program"""
        between_break_lines(word=self._options_available)

    def __rerun_app(self):
        """this will restart the app"""
        input("press ENTER to come back to menu")
        self.__clear_prompt()
        self.__init_app()

    def __run_option(self, selected_option: int):
        """Run the option based on the selected option"""
        self.__clear_prompt()
        try:
            if self._options_available[selected_option - 1]:
                self.__print_line(character="*", repeat=120)
                print(self._options_available[selected_option - 1], "\n")
                self.__print_line(character="*", repeat=120)
        except IndexError as exception:
            if isinstance(exception, IndexError):
                pass
            else:
                print(exception)
        match selected_option:
            case 1:
                name = input("type the restaurant name:\n")
                category = input("type the restaurant category:\n")
                new_restaurant = Restaurant(name=name, category=category)
                self.__register_restaurant(restaurant=new_restaurant)
                self.__rerun_app()

            case 2:
                self.__list_restaurants()
                self.__rerun_app()
            case 3:
                restaurant_name = input(
                    "type the restaurant name that you want to activate:\n"
                )
                self.__activate_restaurant(restaurant_name=restaurant_name)
                self.__rerun_app()
            case 4:
                restaurant_name = input(
                    "type the restaurant name that you want to disable:\n"
                )
                self.__disable_restaurant(restaurant_name=restaurant_name)
                self.__rerun_app()
            case 5:
                restaurant_name = input(
                    "type the restaurant name that you want to evaluate:\n"
                )
                self.__evaluate_restaurant(restaurant_name=restaurant_name)
                self.__rerun_app()
            case 6:
                restaurant_name = input(
                    "type the restaurant name that you want to add the drink:\n"
                )
                self.__add_drink_item_menu(restaurant_name=restaurant_name)
                self.__rerun_app()
            case 7:
                restaurant_name = input(
                    "type the restaurant name that you want to add the food:\n"
                )
                self.__add_food_item_menu(restaurant_name=restaurant_name)
                self.__rerun_app()
            case 8:
                restaurant_name = input(
                    "type the restaurant name that you want to add the dessert:\n"
                )
                self.__add_dessert_item_menu(restaurant_name=restaurant_name)
                self.__rerun_app()
            case 9:
                restaurant_name = input(
                    "type the restaurant name that you want to show the menu:\n"
                )
                self.__show_restaurant_menu(restaurant_name=restaurant_name)
                self.__rerun_app()
            case 10:
                self.__exit_app()
            case _:
                print("Invalid option!\n")
                self.__rerun_app()

    @staticmethod
    def __print_line(character: str, repeat: int):
        """Print the {str} in {repeat} times"""
        print(f"{character*repeat}\n")

    def __init_app(self):
        """This method init the app procedure"""
        print(f"{self._name}\n")
        self.__show_options()
        try:
            selected_option = int(input("Select one option:\n"))
            self.__run_option(selected_option=selected_option)
        except ValueError as exception:
            if isinstance(exception, ValueError):
                print("You must type a integer number dude.\n")
            self.__rerun_app()

    def run(self):
        """This method run the application"""
        self.__clear_prompt()
        self.__init_app()
