class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "choosing_action"
        self.prompt_action()

    def prompt_action(self):
        print("Write action (buy, fill, take, remaining, exit):")

    def print_state(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def make_coffee(self, water_needed, milk_needed, beans_needed, cost):
        if self.water < water_needed:
            print("Sorry, not enough water!")
        elif self.milk < milk_needed:
            print("Sorry, not enough milk!")
        elif self.beans < beans_needed:
            print("Sorry, not enough coffee beans!")
        elif self.cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= water_needed
            self.milk -= milk_needed
            self.beans -= beans_needed
            self.cups -= 1
            self.money += cost

    def process_input(self, user_input):
        if self.state == "choosing_action":
            if user_input == "buy":
                self.state = "choosing_coffee"
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            elif user_input == "fill":
                self.state = "filling_water"
                print("Write how many ml of water you want to add:")
            elif user_input == "take":
                print(f"I gave you {self.money}")
                self.money = 0
                self.prompt_action()
            elif user_input == "remaining":
                self.print_state()
                self.prompt_action()
            elif user_input == "exit":
                self.state = "exited"

        elif self.state == "choosing_coffee":
            if user_input == "back":
                pass
            elif user_input == "1":
                self.make_coffee(250, 0, 16, 4)
            elif user_input == "2":
                self.make_coffee(350, 75, 20, 7)
            elif user_input == "3":
                self.make_coffee(200, 100, 12, 6)
            self.state = "choosing_action"
            self.prompt_action()

        elif self.state == "filling_water":
            self.water += int(user_input)
            self.state = "filling_milk"
            print("Write how many ml of milk you want to add:")

        elif self.state == "filling_milk":
            self.milk += int(user_input)
            self.state = "filling_beans"
            print("Write how many grams of coffee beans you want to add:")

        elif self.state == "filling_beans":
            self.beans += int(user_input)
            self.state = "filling_cups"
            print("Write how many disposable coffee cups you want to add:")

        elif self.state == "filling_cups":
            self.cups += int(user_input)
            self.state = "choosing_action"
            self.prompt_action()


coffee_machine = CoffeeMachine()

while coffee_machine.state != "exited":
    line = input()
    coffee_machine.process_input(line)