# Import the required libraries
import os
import discord
from dotenv import load_dotenv
from dates_theval import dates_theval
from dates_skynoz import dates_skynoz
from dates_flasteh import dates_flasteh
from datetime import datetime

# Get the current date
date_today = datetime.now()
date_formatted = date_today.strftime("%d/%m")

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
            # message = f'@test Happy birthday at {ppl}'
            channel_id = 960260059810648064

            # Test
            message = f'@personneencule Happy birthday at {ppl}\n\n'
            all_birthdays = "\n".join([f"{name}: {date}" for name, date in dates_flasteh.items()])
            message += f"Upcoming birthdays:\n{all_birthdays}"

            channel = client.get_channel(channel_id)
            response = message
            await channel.send(response)
            birthday_flasteh += 1

    # Send no birthday if no birthday
    # if birthday_theval == 0:
    #     message = f'No birthday today'
    #     channel_id = 1074125665512734770
    #     channel = client.get_channel(channel_id)
    #     response = message
    #     await channel.send(response)

    # if birthday_skynoz == 0:
    #     message = f'No birthday today'
    #     channel_id = 1231734938286559283
    #     channel = client.get_channel(channel_id)
    #     response = message
    #     await channel.send(response)

    # Log message when bot is on in TheVal server
    message = f'Bot connected at {date_today}'
    channel_id = 1231619459354202112
    channel = client.get_channel(channel_id)
    response = message
    await channel.send(response)

client.run(TOKEN)