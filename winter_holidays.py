# Winter Holidays
# Author: Ubial
# 8 January 2024

# Requirements:
#  - create a function called winter_holiday()
#     - takes one parameter - string
#     - returns a summary of an event from your holidays

# Please do not use ChatGPT or any LLM

# If you use an LLM, indicate that you did use it
# Also, write the prompt that you used
# I USED CHATGPT
# Prompt: ...


import random


def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/24

    Params:
        good_or_bad - string that indicates whether the event
            is good or bad

    Returns:
        an event that happened to you during the holidays
        the event is selected part"""


def main() -> None:
    # Runs all the things we want to test in our .py file
    winter_holiday("good")
    # "I got a Lego set for the first time in a long time."
    # "I went to Richmond Centre to walk around aimlessly."
    winter_holiday("bad")
    # "I hoped to snowboard during the holiday and there was only rain."
    # "I asked for a bidet for Christmas, instead I got a rando smart watch amazon."


# If we're running THIS FILE using Python
if __name__ == "__main__":
    main()
