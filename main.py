import random
import os
from art import logo
from art import vs
from game_data import data

def get_random_alternative():
    return random.choice(data)

def format_data(alternative):
    name = alternative["name"]
    description = alternative["description"]
    country = alternative["country"]
  
    return f"{name}, a {description} from {country}"

def check_answer(answer, a_followers, b_followers):
    if a_followers > b_followers:
      return answer == "a"
    else:
        return answer == "b"

def game():
    score = 0
    print(logo)
    continue_game = True
    alternative_a = get_random_alternative()
    alternative_b = get_random_alternative()

    while continue_game:
        alternative_a = alternative_b
        alternative_b = random.choice(data)

        while alternative_a == alternative_b:
            alternative_b = random.choice(data)
    
        print(f"Compare A: {format_data(alternative_a)}.")
        print(vs)
        print(f"Against B: {format_data(alternative_b)}.")
        
        answer = input("Who has more Instragram followers? Type 'A' or 'B': ").lower()
        a_follower_count = alternative_a["follower_count"]
        b_follower_count = alternative_b["follower_count"]
        is_correct = check_answer(answer, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            os.system('cls')
            print(logo)
            print(f"You're right! Current score: {score}.")
        else:
            continue_game = False
            print(f"Sorry, that's wrong. Final score: {score}")
game()
