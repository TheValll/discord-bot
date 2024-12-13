def leaderboard_to_string(game_results, winner, points_win, percentage):
    sorted_results = sorted(game_results.items(), key=lambda x: x[1], reverse=True)
    message = "**🏆 Result of the GIFT game :**\n\n"
    medals = ['🥇', '🥈', '🥉']
    
    for index, (player, points) in enumerate(sorted_results):
        if index < 3:
            message += f"{medals[index]} **{player}** : {points} points\n"
        else:
            if points > 0:
                message += f"🎮 **{player}** : {points} points\n"
            else:
                message += f"🔻 **{player}** : {points} point{'s' if points > 1 else ''}\n"
    
    message += "\n\n"
    message += f"🐐 {winner} is the gifted of the day with {points_win} point(s) and a bonus of {percentage} % = {round((points_win * percentage / 100) + points_win)} !\n"
    return message