# Import the required libraries
import os
import discord

from dotenv import load_dotenv
from space_time import SpaceTime
from get_birthdays import get_birthday
from get_channel_id_from_member import get_channel_id_from_member
from get_next_birthday import get_next_birthday
from gift_game import gift_game
from style import format_game_results

# Get the current date
date_today, real_date, date_formatted, current_hour, current_minute = SpaceTime.get_today()

# Init discord
load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    # Log message
    message = f'Bot connected at {real_date}'
    channel_id = 1231619459354202112
    channel = client.get_channel(channel_id)
    try:
        await channel.send(message)
    except Exception as E: 
        print(f"Error sendind message to channel {channel_id} {E}")


    # Get birthdays
    birthdays = get_birthday(date_formatted)
    run_skynoz_game = 0

    if birthdays:
        for birthday in birthdays:
            message = f'@everyone Happy birthday at {birthday["member_name"]} \n'
            channel_id = get_channel_id_from_member(birthday["server_id"])
            channel = client.get_channel(channel_id)

            if birthday["server_id"] == 2:
                next_birthday = get_next_birthday(date_formatted, 2)
                message += f' \n 🎂 Next birthday : {next_birthday["member_name"]} the {next_birthday["member_birthday_date"]} \n'
                run_skynoz_game += 1

            try:
                await channel.send(message)
            except Exception as e:
                print(f"Error sending birthday message to channel {channel_id}: {e}")

    if run_skynoz_game == 0:
        next_birthday = get_next_birthday(date_formatted, 2)
        new_leaderboard, winner, points, percentage = gift_game("skynoz", real_date)
        message = format_game_results(new_leaderboard, next_birthday["member_name"], next_birthday["member_birthday_date"], winner, points, percentage)

        channel_id = 1351570674564726876
        channel = client.get_channel(channel_id)

        try:
            await channel.send(message)
        except Exception as e:
            print(f"Error sending birthday message to channel {channel_id}: {e}")

# DO NOT LAUNCH ON DEV MODE
client.run(discord_token)