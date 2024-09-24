def format_game_results(game_results):
    sorted_results = sorted(game_results.items(), key=lambda x: x[1], reverse=True)
    
    message = "**🏆 Résultats du jeu du GIFT :**\n\n"
    
    medals = ['🥇', '🥈', '🥉']
    
    for index, (player, points) in enumerate(sorted_results):
        if index < 3:
            message += f"{medals[index]} **{player}** : {points} points\n"
        else:
            # Pour les autres participants
            if points > 0:
                message += f"🎮 **{player}** : {points} points\n"
            else:
                message += f"🔻 **{player}** : {points} point{'s' if points > 1 else ''}\n"
    
    return message