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
    message += f"Test pour voir si les clips marchent LOL\n"
    message += f"https://cdn.discordapp.com/attachments/1317136815060160584/1317136834525921330/trhrthr.mp4?ex=675d96c4&is=675c4544&hm=c98fd48ed15108e20cd2a8cb1c34442ed5f49d58df76cc5326db1c9f75b7fb95&\n"
    return message
