import requests
import json
import math
import random

def game():
    # Players
    users = ["Baptiste", "Brian", "Xarwin", "Stoaker", "Mael", "Alix", "Val", "Trytox", "Weebzard", "Mirio", "Kuzuha"]


    # Get random rate
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 17.611001,
        "longitude": 8.080946,
        "daily": "uv_index_max",
        "timezone": "Europe/London"
    }
    responses = requests.get(url, params=params)


    # Calcul random rate
    res = json.loads(responses.text)
    rate = math.radians(res["daily"]["uv_index_max"][0]) * pow(res["daily"]["uv_index_max"][0], res["daily"]["uv_index_max"][0])
    weighted_random_index = random.randint(0, int(rate) % len(users))

    # Get winner
    winner = users[weighted_random_index]


    # Open leaderboard
    with open('leaderboard.json', 'r') as file:
        data = json.load(file)


    # Edit leaderboard
    if winner in data:
        data[winner] += random.randint(1, 10)
        
    new_leaderboard = json.dumps(data)


    # Edit leaderboard
    with open("leaderboard.json", "w") as outfile:
        outfile.write(new_leaderboard)


    # Return leaderboard
    return data