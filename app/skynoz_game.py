# Import the required libraries
from get_winner import get_winner
from get_points import get_points
from insert_leaderboard import insert_leaderboard
from get_leaderboard import get_leaderboard
from leaderboard_to_string import leaderboard_to_string

def skynoz_game(real_date):
    try:
        winner = get_winner('skynoz')
        points, percentage = get_points(real_date)
        insert_leaderboard(winner, points, percentage, real_date)
        leaderboard = get_leaderboard(real_date, 'skynoz')
        message = leaderboard_to_string(leaderboard, winner["member_name"], points, percentage)

        return message
    except Exception as E:
        print(E)