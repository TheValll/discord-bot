import os
import json
import random
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Get the absolute path to the data directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

class Utils:
    @staticmethod
    def get_date(formatted=False):
        date_today = datetime.now() + timedelta(hours=0)
        if formatted:
            return date_today.strftime("%d/%m")
        return date_today
        
    @staticmethod
    def get_token():
        load_dotenv()
        return os.getenv("DISCORD_TOKEN")

    @staticmethod
    def get_channel_log_id():
        load_dotenv()
        token_log = os.getenv("CHANNEL_LOG_ID")
        return int(token_log) if token_log else None
    
    @staticmethod
    def get_channel_skynoz_id():
        load_dotenv()
        token_log = os.getenv("SKYNOZ_CHANNEL_ID")
        return int(token_log) if token_log else None
    
class Birthday:
    @staticmethod
    def load_birthday_data():
        path = os.path.join(DATA_DIR, 'birthdays.json')
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
        
    @staticmethod
    def get_birthdays_by_date(target_date_obj):
        data = Birthday.load_birthday_data()
        date_formatted = target_date_obj.strftime("%d/%m")
        results = []

        for server_key, info in data.items():
            channel_id = info['channel_id']
            server_name = info['server_name']
            
            for member in info['members']:
                if member['birthday'] == date_formatted:
                    results.append({
                        "name": member['name'],
                        "channel_id": channel_id,
                        "server_name": server_name
                    })

        return results if results else None
    
    @staticmethod
    def get_next_birthdays(current_date_obj, target_channel_id):
        data = Birthday.load_birthday_data()
        
        target_server = None
        for info in data.values():
            if info['channel_id'] == target_channel_id:
                target_server = info
                break
        if not target_server:
            return None
        
        upcoming_members = []
        min_days_diff = 366 

        for member in target_server['members']:
            b_day, b_month = map(int, member['birthday'].split('/'))
            try:
                b_date = datetime(current_date_obj.year, b_month, b_day)
            except ValueError:
                b_date = datetime(current_date_obj.year, b_month, b_day - 1)
            
            if b_date.date() <= current_date_obj.date():
                b_date = b_date.replace(year=current_date_obj.year + 1)
            
            diff = (b_date.date() - current_date_obj.date()).days
            
            member_data = {
                "name": member['name'],
                "birthday": member['birthday'],
                "days_remaining": diff
            }

            if diff < min_days_diff:
                min_days_diff = diff
                upcoming_members = [member_data]
            elif diff == min_days_diff:
                upcoming_members.append(member_data)
        
        return upcoming_members
    
class SkynozGame:
    LEADERBOARD_PATH = os.path.join(DATA_DIR, "leaderboard.json")
    VOTES_PATH = os.path.join(DATA_DIR, "votes.json")
    LOG_PATH = os.path.join(DATA_DIR, "game_logs.txt")
    SKYNOZ_CHANNEL_ID = Utils.get_channel_skynoz_id()
    PLAYERS = ["Baptiste", "Brian", "Xarwin", "Stoaker", "Mael", "Alix", "Val", "Trytox", "Weebzard", "Mirio", "Kuzuha", "Lightingloyz", "OOOOOW MY GOD", "Asplix"]

    @staticmethod
    def load_json(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def save_json(path, data):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def add_points_random(voter_name):
        data = SkynozGame.load_json(SkynozGame.LEADERBOARD_PATH)
        target_name = random.choice(SkynozGame.PLAYERS)
        points = random.randint(1, 10)
    
        if target_name in data:
            data[target_name] += points
            SkynozGame.save_json(SkynozGame.LEADERBOARD_PATH, data)
            
            with open(SkynozGame.LOG_PATH, "a", encoding="utf-8") as log:
                log.write(f"[{datetime.now()}] {voter_name} a généré {points} pts pour {target_name}\n")
            
            return target_name, points
        return None, 0

    @staticmethod
    def get_formatted_leaderboard():
        data = SkynozGame.load_json(SkynozGame.LEADERBOARD_PATH)
        sorted_leaderboard = sorted(data.items(), key=lambda x: x[1], reverse=True)
        
        msg = "🏆 **LEADERBOARD SKYNOZ** 🏆\n"
        for i, (name, score) in enumerate(sorted_leaderboard, 1):
            msg += f"{i}. **{name}** : {score} pts\n"
        return msg