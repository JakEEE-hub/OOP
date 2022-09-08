class Player:
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

while True:
    a = input("Would you like to add FOOTBALL player or BASKETBALL player (f/b/c-none)?\n")
    if a.upper() == "F":
        new_player = None
        print("New football player!")
        first_name = input("Write first name: ")
        second_name = input("Write second name: ")
        height_cm = input("Write height in cm: ")
        weight_kg = input("Write weight in kg: ")
        goals = input("Write number of goals: ")
        yellow_cards = input("Write number of yellow cards: ")
        red_cards = input("Write number of red cards: ")
        new_player = FootballPlayer(first_name=first_name, last_name=second_name, height_cm=height_cm,
                                    weight_kg=weight_kg, goals=goals, yellow_cards=yellow_cards, red_cards=red_cards)
        with open("h13_1.json", "w") as players_file:
            players_file.write(str(new_player.__dict__))
    elif a.upper() == "B":
        new_player = None
        print("New basketball player!")
        first_name = input("Write first name: ")
        second_name = input("Write second name: ")
        height_cm = input("Write height in cm: ")
        weight_kg = input("Write weight in kg: ")
        points = input("Write number of points: ")
        rebounds = input("Write number of rebounds: ")
        assists = input("Write number of assists: ")
        new_player = BasketballPlayer(first_name=first_name, last_name=second_name, height_cm=height_cm,
                                    weight_kg=weight_kg, points=points, rebounds=rebounds, assists=assists)
        with open("h13_1.py", "w") as players_file:
            players_file.write(str(new_player.__dict__))
    else:
        break


