# Import the required libraries
import os
import discord

from space_time import SpaceTime
from get_birthday import get_birthday
from skynoz_game import skynoz_game
from get_next_birthday import get_next_birthday
from get_channel_id import get_server_id
from get_clips_random import get_clips_random
from dotenv import load_dotenv

load_dotenv()

# Get the current date
date_today, real_date, date_formatted, current_hour, current_minute = SpaceTime.get_today()

# Init discord
discord_token = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    # Log message when bot is on in TheVal server
    message = f'Bot connected at {real_date}'
    channel_id = 1231619459354202112
    channel = client.get_channel(channel_id)
    response = message
    try:
        await channel.send(response)
    except Exception as e:
        print(f"Error sending message to channel {channel_id}: {e}")

    # Get birthdays
    birthdays = get_birthday(date_formatted)
    run_skynoz_game = 0
    
    if birthdays != []:
        for birthday in birthdays:
            message = f'@everyone Happy birthday at {birthday["member_name"]} \n'
            next_birthday_name, next_birthday_date = get_next_birthday(birthday["server_name"], date_today)
            message += f"🎂 Next birthday : {next_birthday_name} the {next_birthday_date}\n"
            channel_id = birthday["channel_id"]
            channel = client.get_channel(channel_id)
            try:
                await channel.send(message)
            except Exception as e:
                print(f"Error sending birthday message to channel {channel_id}: {e}")
            
            if birthday["server_name"] == "skynoz":
                run_skynoz_game += 1

    if run_skynoz_game == 0: 
        message = skynoz_game(real_date)
        next_birthday_name, next_birthday_date = get_next_birthday("skynoz", date_today)
        message += f"🎂 Next birthday : {next_birthday_name} the {next_birthday_date}\n"

        # Get a random clip 2 days by month
        if real_date.day == 15 or real_date.day == 30:
            message += f"🎬 {get_clips_random(real_date)}\n"

        channel_id = get_server_id("skynoz")
        channel = client.get_channel(channel_id)
        try:
            await channel.send(message)
        except Exception as e:
            print(f"Error sending Skynoz game message to channel {channel_id}: {e}")

# DO NOT LAUNCH ON DEV MODE
client.run(discord_token)
