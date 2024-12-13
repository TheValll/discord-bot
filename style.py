def format_game_results(game_results, name, date, winner, total_points, percentage):
    sorted_results = sorted(game_results.items(), key=lambda x: x[1], reverse=True)
    
    message = "**🏆 Résultats du jeu du GIFT :**\n\n"
    
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
    if percentage != 0:
        message += f"🐐 {winner} is the gifted of the day with {total_points} point(s) and a bonus of {percentage} % = {round((total_points * percentage / 100) + total_points)} !\n"
    else:
        message += f"🐐 {winner} is the gifted of the day with {total_points} point(s) !\n"
    message += f"🎂 Next birthday : {name} the {date}\n"
    return message
