import random

countries_cities = {"Austria": "Vienna",
                    "Croatia": "Zagreb",
                    "Spain": "Madrid",
                    "Slovenia": "Ljubljana",
                    "Germany": "Berlin",
                    "Italy": "Rome",
                    "Portugal": "Lisbon",
                    "France": "Paris",
                    "Hungary": "Budapest",
                    "Russia": "Moscow",
                    "Belgium": "Brussels",
                    "Netherlands": "Amsterdam",
                    "Romania": "Bucharest"}

user = input("Your name: ")
print("Hello, {0}!".format(user))


def quiz():

    for k in countries_cities:
        country = random.choice(list(countries_cities.keys()))
        print("Q: What is the capital of " + country + "?")
        answer = input("A: ")

        if country in countries_cities and answer == countries_cities[country]:
            print("That is correct!")
        else:
            print("Wrong answer! The correct answer is", countries_cities[country] + ". Start from the beginning.")
            break


while True:

    question = input("Would you like to play Geography quiz? ").lower()

    if "y" not in question:
        print("Bye!")
        break
    else:
        quiz()
