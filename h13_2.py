import datetime
import json
import random

class Result:
    def __init__(self, attempts, date):
        self.attempts = attempts
        self.date = date

#FUNCTIONS!
def play_game():
    score_list = get_score_list()
    secret = random.randint(1, 30)
    attempts = 0

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            result_obj = Result(attempts=attempts, date=str(datetime.datetime.now()))
            score_list.append(result_obj.__dict__)
            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")

def get_score_list():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
    return score_list

def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda item: item["attempts"])[:3]
    return top_score_list


#GAME!
while True:
    play_game()
    selection = input("Would you like to \nA) Play new game \n"
                      "B) See the best scores \nC) Quit \n")

    if selection.upper() == "A":
        play_game()
    elif selection.upper() == "B":
        for score_dict in get_top_scores():
            result_obj = Result(attempts=score_dict.get("attempts"),
                                date=score_dict.get("date"))
            print("Attempts: {attempts}, Date: {date}".format(attempts=result_obj.attempts,
                                                              date=result_obj.date))
    else:
        break