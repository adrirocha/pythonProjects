from game_data import profiles
from random import randint


def getProfile():
    return profiles.pop(randint(0,len(profiles)-1))

def checkFollowers(profile_a, profile_b):
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    if answer == "A":
        if profile_a['level'] > profile_b['level']:
            return True, profile_b
        else:
            return False
    if answer == "B":
        if profile_b['level'] > profile_a['level']:
            return True, profile_b
        else:
            return False


is_game_over = False
current_score = 0

profile_a = getProfile()
while not is_game_over and len(profiles):
    profile_b = getProfile()

    print(f"Compare A: {profile_a['name']}, a {profile_a['description']}, from {profile_a['country']}")
    print(f"Against B: {profile_b['name']}, a {profile_b['description']}, from {profile_b['country']}")
    result, profile_a = checkFollowers(profile_a, profile_b)
    if result == False:
        print(f"Sorry, that's wrong. Final Score: {current_score}")
        is_game_over = True
    else:
        current_score += 1
        print(f"You're right! Current score: {current_score}")
        if len(profiles):
            profile_b = getProfile()
        else:
            print("You won!")
