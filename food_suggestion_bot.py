# Food Suggestion Bot
# Author: Ubial
# 6 October 2023

# A bot that asks the user what their favourite
# food is. Based on that food, it will classify
# the type/genre/cuisine of the food, then
# give a restaurant suggestion.

import random
import time

# Introduce the bot to the user
# Ask the user what their favourite food is
print("Hello, I am here to suggest you a restaurant.")
time.sleep(1)
fave_food = input("To help me suggest a restaurant, tell me what your favourite food is. ")
time.sleep(1)

# Cuisines
italian_food = ["pasta", "pizza", "canneloni", "tiramisu"]
# Add another cuisine that our bot should make a suggestion for
western_food = ["burgers", "fries", "hot dogs"]

# If they answer with Italian food,
# Suggest an Italian restaurant
if fave_food.lower().strip("!.,?") in italian_food:
    print("I see that you might like Italian food. 🍝")
    time.sleep(1)
    print("I suggest Broli Kitchen.")
    time.sleep(1)
    print("Here's their address.")
    print("186-8180 No 2 Rd, Richmond, BC")
elif fave_food.lower().strip("!..?") in western_food:
    print("I think that you like western food. 🍔")
    time.sleep(1)
    print("I suggest White Spot.")
    time.sleep(1)
    print("Here's their address.")
    print("6551 No. 3 Rd #1902, Richmond, BC")
    print("It's in Richmond Centre.")
else:
    print("Sorry, I'm not sure what kind of food that is.")
    time.sleep(1)
    print("I can't, unfortunately, provide a suggestion.")

print("Thanks for using the Food Suggestion Bot!")