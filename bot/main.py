import discord
import asyncio
from discord.ext import commands, tasks
from utils import Utils, Birthday, SkynozGame

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
LOG_CHANNEL_ID = Utils.get_channel_log_id()

@tasks.loop(minutes=1)
async def check_birthday_task():
    now = Utils.get_date(False)

    if now.hour == 1 and now.minute == 0:
        log_channel = bot.get_channel(LOG_CHANNEL_ID)
        birthdays = Birthday.get_birthdays_by_date(now)
        
        if birthdays:
            for person in birthdays:
                channel = bot.get_channel(person['channel_id'])
                if channel:
                    try:
                        await channel.send(f"🎂 @everyone Joyeux anniversaire à **{person['name']}** ! 🎉")
                    except Exception as e:
                        print(f"Erreur envoi anniversaire : {e}")

        skynoz_channel = bot.get_channel(Utils.get_channel_skynoz_id())
        if skynoz_channel:
            try:
                leaderboard_msg = SkynozGame.get_formatted_leaderboard()
                await skynoz_channel.send(leaderboard_msg)
            except Exception as e:
                print(f"Erreur envoi leaderboard Skynoz : {e}")

        if log_channel:
            status_anniv = f"{len(birthdays)} anniversaire(s) envoyé(s)" if birthdays else "Aucun anniversaire"
            await log_channel.send(f"✅ `{now.strftime('%d/%m')}` : Vérification terminée.\n🎂 {status_anniv}.\n🏆 Leaderboard Skynoz affiché.")
    
        await asyncio.sleep(61)

@bot.event
async def on_ready():
    today = Utils.get_date(False)
    response = f'Bot connected at {today}'
    channel_id = Utils.get_channel_log_id()
    channel = bot.get_channel(channel_id)
    
    if channel:
        await channel.send(response)
        
    print('Bot ready')

    if not check_birthday_task.is_running():
        check_birthday_task.start()

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="help", description="Get help")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message("Les commandes :\n /next\n /gift (Skynoz server only)")

@bot.tree.command(name="next", description="Affiche le prochain anniversaire pour ce serveur")
async def next_bday(interaction: discord.Interaction):
    today = Utils.get_date(False)

    server_data = Birthday.get_next_birthdays(today, interaction.channel_id)
        
    if server_data:
        names = ", ".join([m['name'] for m in server_data])
        date_bday = server_data[0]['birthday']
        days_left = server_data[0]['days_remaining']
        
        message = (
            f"🎂 **Prochain anniversaire :**\n"
            f"👤 Nom : **{names}**\n"
            f"📅 Date : {date_bday}\n"
            f"⏳ Dans : **{days_left} jour(s)**"
        )
    else:
        message = "Ce salon n'est associé à aucun channel dans la base de données d'anniversaires."
        
    await interaction.response.send_message(message)

@bot.tree.command(name="gift", description="Attribue des points au hasard à un membre (1x par jour)")
async def gift(interaction: discord.Interaction):
    if interaction.channel_id != SkynozGame.SKYNOZ_CHANNEL_ID:
        await interaction.response.send_message("Cette commande n'est utilisable que dans le salon dédié.", ephemeral=True)
        return

    await interaction.response.defer(ephemeral=False)

    user_id = str(interaction.user.id)
    today = Utils.get_date(True)
    
    votes = SkynozGame.load_json(SkynozGame.VOTES_PATH)
    if user_id in votes and votes[user_id] == today:
        await interaction.followup.send("Tu as déjà participé aujourd'hui !", ephemeral=True)
        return

    target, pts = SkynozGame.add_points_random(interaction.user.name)
    
    if target:
        votes[user_id] = today
        SkynozGame.save_json(SkynozGame.VOTES_PATH, votes)
        await interaction.followup.send(f"Commande effectuée!")
    else:
        await interaction.followup.send("Erreur lors de l'attribution des pts.", ephemeral=True)

bot.run(Utils.get_token())