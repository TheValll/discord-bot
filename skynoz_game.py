import json
import random

def game(date):
    # Christmas game
    day = date.day
    month = date.month

    # Players
    users = ["Baptiste", "Brian", "Xarwin", "Stoaker", "Mael", "Alix", "Val", "Trytox", "Weebzard", "Mirio", "Kuzuha" , "Lightingloyz", "OOOOOW MY GOD", "Asplix"]

    weighted_random_index = random.randint(0, len(users) - 1)

    # Get winner
    winner = users[weighted_random_index]

    # Open leaderboard
    with open('/home/valentin78_massonniere/discord-bot/leaderboard.json', 'r') as file:
        data = json.load(file)

    # Edit leaderboard
    if winner in data:
        if month == 12 and day < 25:
            bonus = random.randint(1, 69)
            base = random.randint(1, 10)
            total = round((base * bonus / 100) + base)
            data[winner] += total
            points = base
            percentage = bonus
        else:
            total = random.randint(1, 10)
            data[winner] += total
            points = total
            percentage = 0
        
    new_leaderboard = json.dumps(data)

    # Edit leaderboard
    with open("/home/valentin78_massonniere/discord-bot/leaderboard.json", "w") as outfile:
        outfile.write(new_leaderboard)

    # Return leaderboard
    return data, winner, points, percentage
