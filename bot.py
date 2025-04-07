import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv
from twitch_integration import start_twitch_task

# --- Charger le .env ---
load_dotenv()

# --- Initialisation du bot ---
intents = discord.Intents.default()
intents.members = True
intents.message_content = True  # Pour lire le contenu des messages

bot = commands.Bot(command_prefix='!', intents=intents)

# --- Citations KH ---
kh_quotes = [
    "Mon cœur est la clé.",
    "Je suis ce que je suis, à cause de qui nous sommes tous.",
    "Qui d'autre va manger des glaces avec moi ?",
    "Mon ami m'a offert ça... C'est pourquoi je ne peux pas perdre !",
    "Il y a plus de lumière que les ténèbres ne pourront jamais éteindre."
]

# --- Bienvenue ---
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='général')
    if channel:
        await channel.send(f"Bienvenue dans le Royaume du Cœur, {member.mention} ! Pose ta Keyblade et installe-toi.")

# --- Commande !khquote ---
@bot.command()
async def khquote(ctx):
    quote = random.choice(kh_quotes)
    await ctx.send(f"\u2728 {quote} \u2728")

# --- Démarrage ---
@bot.event
async def on_ready():
    print(f"{bot.user} est prêt à protéger les cœurs et à suivre les lives !")
    
    # Démarre la tâche de notification Twitch
    await start_twitch_task(bot)  # Appelle la fonction pour démarrer la vérification Twitch

# --- Lancer le bot avec le token sécurisé ---
bot.run(os.getenv("DISCORD_TOKEN"))
