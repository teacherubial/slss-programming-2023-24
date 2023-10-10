# Exercise 1
# Author: Ubial
# 6 October 2023

# Find the problem

korean_food = ["bibimbap", "budae jiggae", "kimbap"]

fave_food = input("What's your favourite food? ")

if fave_food.lower().strip("!,.?") in korean_food:
    print("I think you like Korean food.")
else:
    print("Sorry I can't help you.")