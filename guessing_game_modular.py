from guessing_game_functions import player_name, game_play, get_scores

player_name
print("Hello, {}!" .format(player_name))


while True:
    question = input("What would you like to do? \n A) Play a game. \n B) See best scores. \n C) Nothing. \n ")

    if question.upper() == "A":
        game_play()
    elif question.upper() == "B":
        get_scores()
    else:
        break