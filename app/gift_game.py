import os
import json
import random

PATH = os.path.join(os.path.dirname(__file__), "../gift_game_players.json")
with open(PATH, "r") as file:
    data = json.load(file) 

def gift_game(server_name, real_date):
    player = data[server_name]
    leaderboard_key = f"leaderboard_{server_name}"
    leaderboard = data.get(leaderboard_key, {}) 
    day = real_date.day

    if day == 1:
        leaderboard = {key: 0 for key in leaderboard}

    weighted_random_index = random.randint(0, len(player) - 1)
    winner = player[weighted_random_index]

    if winner in leaderboard:
        if day > 20:
            bonus = random.randint(1, 69)
            base = random.randint(1, 10)
            total = round((base * bonus / 100) + base)
            leaderboard[winner] += total
            points = base
            percentage = bonus
        else:
            total = random.randint(1, 10)
            leaderboard[winner] += total
            points = total
            percentage = 0

    data[leaderboard_key] = leaderboard

    with open(PATH, "w") as outfile:
        json.dump(data, outfile, indent=2)

    return data[leaderboard_key], winner, points, percentage
