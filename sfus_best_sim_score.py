# SFU's Best
# Author: Ubial
# 10 November 2023

# Load data from .csv file
# Read it in a meaningful way
# Link our similarity score algo to the data

# Open the file
with open("./data.csv") as f:
    # Read the first line of data

    f.readline()

# Create a "profile" for someone that shows their
# favourite places at SFU
profile = [
    "Bubble World",
    "Chef Hung",
    "Uncle Fatih's",
    "Guadalupe (MBC)",
    "Steve's Poke Bar"
]

# Initialize our top similarity score and their name

# For every line of data in the file (string)
    # convert the line of data into a list

    # initialize the CURRENT sim score

    # for every item in our PROFILE
        # if that item is in the data's list
            # increase the sim score by 1