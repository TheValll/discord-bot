import json
import random

def game():
    # Players
    users = ["Baptiste", "Brian", "Xarwin", "Stoaker", "Mael", "Alix", "Val", "Trytox", "Weebzard", "Mirio", "Kuzuha" , "Lightingloyz", "OOOOOW MY GOD"]

    weighted_random_index = random.randint(0, len(users) - 1)

    # Get winner
    winner = users[weighted_random_index]

    # Open leaderboard
    # with open('/home/valentin78_massonniere/discord-bot/leaderboard.json', 'r') as file:
    with open('leaderboard.json', 'r') as file:
        data = json.load(file)

    # Edit leaderboard
    if winner in data:
        data[winner] += random.randint(1, 10)
        
    new_leaderboard = json.dumps(data)

    # Edit leaderboard
    # with open("/home/valentin78_massonniere/discord-bot/leaderboard.json", "w") as outfile:
    with open("leaderboard.json", "w") as outfile:
        outfile.write(new_leaderboard)

    # Return leaderboard
    return data

for i in range(35):
    game()