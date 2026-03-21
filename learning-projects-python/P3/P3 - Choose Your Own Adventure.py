#Project 3: Treasure Island Game

print(r'''
*********************************************************************
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
*********************************************************************
''')

print("Welcome to Treasure Hunt.\nYour mission is to find the lost treasure.")

cross_road = input("You came across a cross road. Which path would you choose?\nType 'left' or 'right' = ").lower()
if cross_road == "left":
    sea = input("You reached a sea. There is an Castle in the middle of the sea."
                "\nType 'wait' to wait for a boat. OR Type 'swim' to swim across. = ").lower()
    if sea == "wait":
        door = input("You arrive at the Castle unharmed. There is a hall with 3 doors."
                     "\nOne 'red', one 'yellow' and one 'blue'. Which colour do you choose? = ").lower()
        if door == "yellow":
            print("You found the lost treasure! You Win!")
        elif door == "blue":
            print("You entered a room full of snakes. Game Over!")
        elif door == "red":
            print("You entered a room full of fire. Game Over!")
        else:
            print("Please enter a valid input. Try again.")

    elif sea == "swim":
        print("Hungry Sharks ate you. Game Over!")
    else:
        print("Please enter a valid input. Try again.")

elif cross_road == "right":
    print("You stumbled in a ditch. Game Over!")
else:
    print("Please enter a valid input. Try again.")


# Python Concepts Learned / Practised:
# - print() function
# - input() function
# - Variables
# - Raw string literal, r
# - Multi-line printing, triple quote '''
# - ASCII art
# - Conditional statements (if, elif, else)
# - Nested statement
# - String method, lower()
# - Comparison operator, ==

