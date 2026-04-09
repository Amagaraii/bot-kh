import discord
import aiohttp
import os
import asyncio
import json
from dotenv import load_dotenv
from twitch_token_manager import refresh_access_token, CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN



# --- Chargement des variables d'environnement ---
load_dotenv()

# --- Configuration centralisée ---
TWITCH_CONFIG = {
    "client_id": os.getenv("CLIENT_ID"),
    "access_token": os.getenv("ACCESS_TOKEN"),
    "streamers": [streamer.strip() for streamer in os.getenv("STREAMERS", "").split(",")],  
    "check_interval": 300,  # 5 minutes
    "status_cache_file": "live_status_cache.json"
}

API_URL = "https://api.twitch.tv/helix/streams"

# --- Charger l'état précédent depuis un fichier ---
def load_previous_status():
    try:
        with open(TWITCH_CONFIG["status_cache_file"], "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {streamer: False for streamer in TWITCH_CONFIG["streamers"]}

def save_status(status_dict):
    with open(TWITCH_CONFIG["status_cache_file"], "w") as f:
        json.dump(status_dict, f)

# --- Vérifie si le streamer est en live ---
async def check_stream_status(user_name):
    async with aiohttp.ClientSession() as session:
        headers = {
            "Client-ID": TWITCH_CONFIG["client_id"],
            "Authorization": f"Bearer {TWITCH_CONFIG['access_token']}",
        }
        params = {"user_login": user_name}

        async with session.get(API_URL, headers=headers, params=params) as response:
            if response.status == 401:
                print(f"⚠️ Token expiré. Rafraîchissement en cours...")
                new_token = refresh_access_token(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)
                if new_token:
                    TWITCH_CONFIG["access_token"] = new_token  # mise à jour en live
                    return await check_stream_status(user_name)  # retenter la requête
                else:
                    print("❌ Impossible de rafraîchir le token.")
                    return {"is_live": False}

            data = await response.json()
            if data.get("data"):
                stream_data = data["data"][0]
                return {
                    "is_live": True,
                    "title": stream_data["title"],
                    "thumbnail_url": f"https://static-cdn.jtvnw.net/previews-ttv/live_user_{user_name.lower()}.jpg"
                }
            return {"is_live": False}

# --- Tâche principale qui tourne sans tasks.loop ---
async def start_twitch_task(bot):
    print("🎮 Démarrage de la surveillance des streamers...")
    previous_status = load_previous_status()

    async def periodic_check():
        while True:
            for streamer in TWITCH_CONFIG["streamers"]:
                result = await check_stream_status(streamer)
                is_live = result["is_live"]

                # Seulement si l'état change vers "en live"
                if is_live and not previous_status.get(streamer, False):
                    print(f"🔴 {streamer} vient de lancer son live !")

                    # Embed personnalisé
                    embed = discord.Embed(
                        title=f"{streamer} est en live !",
                        description=result["title"],
                        url=f"https://www.twitch.tv/{streamer}",
                        color=discord.Color.purple()
                    )
                    embed.set_image(url=result["thumbnail_url"])

                    # Envoi du message dans le salon
                    for guild in bot.guilds:
                        channel = discord.utils.get(guild.text_channels, name="🔴-live")
                        if channel:
                            await channel.send("@everyone", embed=embed)

                # Afficher un log seulement si changement d'état
                if is_live != previous_status.get(streamer, False):
                    print(f"↪️ État changé pour {streamer} : {'en live' if is_live else 'hors ligne'}")

                # Mettre à jour l'état
                previous_status[streamer] = is_live

            # Sauvegarder dans le cache
            save_status(previous_status)

            await asyncio.sleep(TWITCH_CONFIG["check_interval"])

    asyncio.create_task(periodic_check())
