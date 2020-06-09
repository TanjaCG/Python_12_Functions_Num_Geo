from guessing_game_functions import player_name, game_play, get_scores, get_top_scores

print("Hello, {}!" .format(player_name))

while True:
    question = input("What would you want to do? \n A) Play a game. \n "
                     "B) See best scores. \n C) See all scores. \n D) Nothing. ")

    if question.upper() == "A":
        game_play()
    elif question.upper() == "B":
        get_top_scores()
    elif question.upper() == "C":
        for all_scores in get_scores():
            print(str(all_scores["attempts"]) + " attempts, date: " + all_scores.get("datetime") +
                  ", player name: " + all_scores.get("player name") +
                  ", wrong guesses: " + str(all_scores.get("wrong_guess")))
    else:
        print("Bye!")
        break
