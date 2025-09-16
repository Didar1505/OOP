from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_machine = CoffeeMaker()
money_machine = MoneyMachine()

user_input = input("What would you like: "+menu.get_items()+"\t")
if user_input == 'off':
    pass
elif user_input == 'report':
    print(coffe_machine.report())
else:
    drink = menu.find_drink(user_input)
    if drink:
        user_coins = input()
        money_machine.process_coins()
        if money_machine.make_payment(menu.menu[drink].cost):
            coffe_machine.make_coffee(drink)


