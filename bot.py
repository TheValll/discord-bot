# Import the required libraries
import os
import discord
from dotenv import load_dotenv
from dates_theval import dates_theval
from dates_skynoz import dates_skynoz
from dates_flasteh import dates_flasteh
from datetime import datetime, timedelta
from skynoz_game import game
from style import format_game_results
from next_birthday import next_birthday

# Get the current date
date_today = datetime.now()
real_date = date_today + timedelta(hours=1)
date_formatted = real_date.strftime("%d/%m")
current_hour = real_date.hour
current_minute = real_date.minute

if (current_hour == 23 and current_minute >= 58) or (current_hour == 0 and current_minute <= 2):
    # Load the environment variables
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    # Create a Discord client
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        # By default 0 birthday
        birthday_theval = 0
        birthday_skynoz = 0
        birthday_flasteh = 0

        # TheVal server dates
        for ppl in dates_theval:
            if dates_theval[ppl] == date_formatted:
                message = f'@everyone Happy birthday at {ppl}'
                channel_id = 1074125665512734770
                channel = client.get_channel(channel_id)
                response = message
                await channel.send(response)
                birthday_theval += 1
        
        # Skynoz server dates
        for ppl in dates_skynoz:
            if dates_skynoz[ppl] == date_formatted:
                message = f'@everyone Happy birthday at {ppl}'
                channel_id = 1231734938286559283
                channel = client.get_channel(channel_id)
                response = message
                await channel.send(response)
                birthday_skynoz += 1

        # Flasteh server dates
        for ppl in dates_flasteh:
            if dates_flasteh[ppl] == date_formatted:
                message = f'@everyone Happy birthday at {ppl}'
                channel_id = 960260059810648064
                channel = client.get_channel(channel_id)
                response = message
                await channel.send(response)
                birthday_flasteh += 1


        if birthday_skynoz == 0:
            try:
                message = game()
                name, date = next_birthday(dates_skynoz, date_today)
                message_styled = format_game_results(message, name, date)
                channel_id = 1231734938286559283
                channel = client.get_channel(channel_id)
                response = message_styled
                await channel.send(response)
            except Exception as E:
                channel_id = 1231619459354202112
                channel = client.get_channel(channel_id)
                response = E
                await channel.send(response)

        # Log message when bot is on in TheVal server
        message = f'Bot connected at {real_date}'
        channel_id = 1231619459354202112
        channel = client.get_channel(channel_id)
        response = message
        await channel.send(response)

    client.run(TOKEN)
else:
    print("DEV MODE !!")
