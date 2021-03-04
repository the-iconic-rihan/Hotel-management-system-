# Restaurant management system
import random


class Restaurant:

    def __init__(self, hotel_name):
        self.hotel_name = hotel_name
        self.order = {}

    def drinks(self, user_drink, size, customer_name):
        if user_drink in Drinks and size == 2 or 1:
            self.order.update({user_drink: size})
            print(f"{size}:{user_drink} served to {customer_name}")
        else:
            print(f"Sorry, but '{user_drink}' is not available for drinks.")

    def breakfast(self, user_breakfast, size, customer_name):
        if user_breakfast in breakfast and size == 2 or 1:
            self.order.update({user_breakfast: size})
            print(f"{size}:{user_breakfast} served to {customer_name}")
        else:
            print(f"Sorry, but '{user_breakfast}' is not available for breakfast.")

    def veg_food(self, user_veg, size, customer_name):
        if user_veg in veg_food and size == 2 or 1:
            self.order.update({user_veg: size})
            print(f"{size}:{user_veg} served to {customer_name}")
        else:
            print(f"Sorry, but '{user_veg}' is not available at the veg card.")

    def non_veg_food(self, user_non_veg, size, customer_name):
        if user_non_veg in non_veg_food and size == 2 or 1:
            self.order.update({user_non_veg: size})
            print(f"{size}:{user_non_veg} served to {customer_name}")
        else:
            print(f"Sorry, but '{user_non_veg}' is not available at the non-veg card.")


def display_drinks():
    for index, drink in enumerate(Drinks):
        print(f"{index + 1}]{drink}")


def display_veg_food():
    for index, veg_items in enumerate(veg_food):
        print(f"{index + 1}]{veg_items}")


def display_breakfast():
    for index, items in enumerate(breakfast):
        print(f"{index + 1}] {items}")


def main():
    food_variety = ["Vegetarian", "Non-vegetarian", "Drinks"]

    print(f"Welcome to {hotel_name}")
    print("We have following varieties of food in our hotel :-", '%s' % ','.join(map(str, food_variety)))
    # about to def the function

    print("Hit your choice ")
    food_type = int(input("\t1]Veg \n\t2] Non-veg \n\t3] Both \t\n: "))
    if food_type == 1:
        food_type_variety = int(input("\t1]Drinks \n\t2]BreakFast \n\t3]Dishes \n\t4] Drinks && Dishes \n\t5] Drinks "
                                      "&& BreakFast \n\tHit your choice : "))
        if food_type_variety == 1:
            _drinks_order()
            # print(hotel_customer.order)

        elif food_type_variety == 2:
            _breakfast_order()
            # print(hotel_customer.order)

        elif food_type_variety == 3:
            _dishes_order()
        elif food_type_variety == 4:
            print("Here is the menu card of Drinks && Dishes respectively.")
            _drinks_order()
            _dishes_order()

        elif food_type_variety == 5:
            print("Here is the menu card of breakfast && Drinks respectively")
            _breakfast_order()
            _drinks_order()

        else:
            print("You hit the wrong choice!")
            main()

    elif food_type == 2:
        food_type_variety = int(input("\t1]BreakFast \n\t2]Dishes \n\tHit your choice : "))
        if food_type_variety == 1:
            _breakfast_order()
        elif food_type_variety == 2:
            _dishes_order()
        else:
            print("You hit the wrong choice!")
            main()

    else:
        print("You hit the wrong choice!")
        main()


if __name__ == '__main__':
    Drinks = {"Armagnac": 450,
              "Casa Ginger Mint Paloma": 820,
              "Strawberry Kiwi Margarita": 792,
              "Oaxacan Old Fashioned": 1010,
              "The Marble Queen": 5200}
    breakfast = {"Tea": 50,
                 "Breakfast Cereals": 100,
                 "Eggs (Hot or Hard Boiled)": 250,
                 "Meats (Sausage, Bacon, or Ham)": 500,
                 "Porridge/Oatmeal.": 1000}

    veg_food = {
        "Crispy Calamari Rings Recipe": 400,
        "Quick Salted Caramel Pie": 600,
        "Prawn Pie": 5051,
        "Yorkshire Lamb Patties": 2000
    }
    non_veg_food = {
        "Bangers and Mash": 4500,
        " Fish and Chips": 5000,
        "Grilled Chicken Escalope with Fresh Salsa": 550,
        "Chicken and Waffles": 3500
    }
    hotel_name = "Welcome to Hotel InterContinental, Aurangabad, Maharashtra"
    hotel_customer = Restaurant(hotel_name)
    customer_name = str(input("Enter your name : "))


    def _drinks_order():
        print("Here is the menu cart of Drinks")
        display_drinks()
        user_drink = str(input("What's your order in drinks ? \nEnter the drink name and no of drinks: "))
        size = int(input())
        hotel_customer.drinks(user_drink, size, customer_name)


    def _breakfast_order():
        print("Here is the menu cart of breakfast")
        display_breakfast()
        user_breakfast = str(
            input("What's your order in breakfast ? \nEnter the breakfast name and no of dishes: "))
        size = int(input())
        hotel_customer.breakfast(user_breakfast, size, customer_name)


    def _dishes_order():
        print("Here is the menu card of Dishes")
        display_veg_food()
        user_veg = str(input("What's your order in veg-dishes ? \nEnter the dish name and no of dishes: "))
        size = int(input())
        hotel_customer.veg_food(user_veg, size, customer_name)


    main()
