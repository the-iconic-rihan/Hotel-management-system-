# Restaurant management system
import random


class Restaurant:

    def __init__(self, hotel_name):
        self.hotel_name = hotel_name
        self.order = {}

    # taking the orders of veg section
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

    # taking the orders of non-veg section
    def non_veg_food(self, user_non_veg, size, customer_name):
        if user_non_veg in non_veg_food and size == 2 or 1:
            self.order.update({user_non_veg: size})
            print(f"{size}:{user_non_veg} served to {customer_name}")
        else:
            print(f"Sorry, but '{user_non_veg}' is not available at the non-veg card.")

    def non_veg_breakfast(self, user_non_veg, size, customer_name):
        if user_non_veg in non_veg_breakfast and size == 2 or 1:
            self.order.update({user_non_veg: size})
            print(f"{size}:{user_non_veg} served to {customer_name}")
        else:
            print(f"Sorry, but '{user_non_veg}' is not available at the non-veg card.")

    def non_veg_cocktail(self, user_non_veg, size, customer_name):
        if user_non_veg in cocktails and size == 2 or 1:
            self.order.update({user_non_veg: size})
            print(f"{size}:{user_non_veg} served to {customer_name}")
        else:
            print(f"Sorry, but '{user_non_veg}' is not available at the non-veg card.")


# displaying the vegetarian section
def display_drinks():
    print("List of Drinks in veg.")
    for index, drink in enumerate(Drinks):
        print(f"{index + 1}]{drink}")


def display_veg_food():
    print("List of veg-dishes.")
    for index, veg_items in enumerate(veg_food):
        print(f"{index + 1}]{veg_items}")


def display_breakfast():
    print("List of breakfast items.")
    for index, items in enumerate(breakfast):
        print(f"{index + 1}] {items}")


# displaying the non-vegetarian section
def display_cocktails():
    print("List of Cocktails.")
    for index, drink in enumerate(cocktails):
        print(f"{index + 1}]{drink}")


def display_non_veg_dishes():
    print("List of Non-veg dishes.")
    for index, dishes in enumerate(non_veg_food):
        print(f"{index + 1}]{dishes}")


def display_non_veg_breakfast():
    print("List of Non-veg breakfast.")
    for index, dishes in enumerate(non_veg_breakfast):
        print(f"{index + 1}]{dishes}")


def menu_card():
    print("Here is the list of food varieties we have in have in our hotel.")
    print("The vegetarian section :- ")
    display_drinks()
    display_breakfast()
    display_veg_food()
    print("The non-vegetarian section :-")
    display_cocktails()
    display_non_veg_breakfast()
    display_non_veg_dishes()


def main():
    food_variety = ["Vegetarian", "Non-vegetarian", "Drinks"]

    print(f"Welcome to {hotel_name}")
    print("We have following varieties of food in our hotel :-", '%s' % ','.join(map(str, food_variety)))
    menu_card()
    print("Hit your choice ")
    food_type = int(input("\t1]Veg \n\t2] Non-veg \n\t3] Both \t\n: "))
    if food_type == 1:
        food_type_variety = int(input("\t1]Drinks \n\t2]BreakFast \n\t3]Dishes \n\t4] Drinks && Dishes \n\t5] Drinks "
                                      "&& BreakFast \n\tHit your choice : "))
        if food_type_variety == 1:
            _drinks_order()

        elif food_type_variety == 2:
            _breakfast_order()

        elif food_type_variety == 3:
            _dishes_order()

        elif food_type_variety == 4:
            _drinks_order()
            _dishes_order()

        elif food_type_variety == 5:
            _breakfast_order()
            _drinks_order()

        else:
            print("You hit the wrong choice!")
            main()

    elif food_type == 2:
        food_type_variety = int(input("\t1]BreakFast \n\t2]Dishes\n\t3]Cocktails \n\tHit your choice : "))
        if food_type_variety == 1:
            _breakfast_order()
        elif food_type_variety == 2:
            _dishes_order()
        elif food_type_variety == 3:
            _cocktails_order()
            print(hotel_customer.order)
        else:
            print("You hit the wrong choice!")
            main()

    elif food_type == 3:
        food_type_variety = int(input("\t1] Drinks && Cocktails \n\t2] Veg && Non-veg breakfast "
                                      "\n\t3] Non-veg && veg dishes" "\n\tHit your choice : "))
        try:
            if food_type_variety == 1:
                print("We will go with Drinks and Cocktails")
                _drinks_order()
                _cocktails_order()
            elif food_type_variety == 2:
                print("We will go with veg and non-veg breakfast")
                non_veg_breakfast_order()
                _breakfast_order()
            elif food_type_variety == 3:
                print("We will go with veg and non-veg dishes")
                non_veg_dishes_order()
                _dishes_order()
        except IndexError:
            print("The input you gave is incorrect.")
            main()
        else:
            print("All your orders are served , please enjoy the moment.")

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
                 "Pineapple Upside Down Pancakes.": 500,
                 "Porridge/Oatmeal.": 1000}

    veg_food = {
        "Crispy Calamari Rings Recipe": 400,
        "Quick Salted Caramel Pie": 600,
        "Prawn Pie": 5051,
        "Yorkshire Lamb Patties": 2000
    }

    non_veg_breakfast = {
        "Scrambled Eggs": 100,
        "Eggs (Hot or Hard Boiled)": 250,
        "Meats (Sausage, Bacon, or Ham)": 500,
        "Stuffed Omelet": 200
    }
    cocktails = {
        "Mojito": 505,
        "Daiquiri": 450,
        "Bloody Mary": 650,
        "Moscow Mule.": 750
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

    # veg order functioning
    def _drinks_order():
        print("Select the drinks from menu card.")
        user_drink = str(input("What's your order in drinks ? \nEnter the drink name and no of drinks: "))
        size = int(input())
        hotel_customer.drinks(user_drink, size, customer_name)


    def _breakfast_order():
        print("Select the breakfast dish from menu card.")
        user_breakfast = str(input("What's your order in breakfast ? \nEnter the breakfast name and no of dishes: "))
        size = int(input())
        hotel_customer.breakfast(user_breakfast, size, customer_name)


    def _dishes_order():
        print("Select the veg-dish from menu card.")
        user_veg = str(input("What's your order in veg-dishes ? \nEnter the dish name and no of dishes: "))
        size = int(input())
        hotel_customer.veg_food(user_veg, size, customer_name)

    # non_veg order functioning
    def _cocktails_order():
        print("Select the cocktail from menu card.")
        user_non_veg = str(input("What's your order in Cocktails ? \nEnter the cocktail name and no of cocktail: "))
        size = int(input())
        hotel_customer.non_veg_cocktail(user_non_veg, size, customer_name)

    def non_veg_breakfast_order():
        print("Select the non-veg-dish from menu card.")
        user_non_veg = str(input("What's your order in non-veg breakfast ? \nEnter the dish name and no of dishes: "))
        size = int(input())
        hotel_customer.non_veg_breakfast(user_non_veg, size, customer_name)

    def non_veg_dishes_order():
        print("Select the non-veg-dish from menu card.")
        user_non_veg = str(input("What's your order in non-veg dish ? \nEnter the dish name and no of dishes: "))
        size = int(input())
        hotel_customer.non_veg_food(user_non_veg, size, customer_name)

    main()
