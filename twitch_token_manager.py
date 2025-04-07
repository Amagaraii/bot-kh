import requests
import os
from dotenv import load_dotenv

load_dotenv()
ENV_FILE = ".env"

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")


def refresh_access_token(client_id, client_secret, refresh_token):
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }

    response = requests.post(url, params=params)
    data = response.json()

    if "access_token" in data:
        print("✅ Token rafraîchi avec succès !")
        print("ACCESS_TOKEN =", data["access_token"])

        # Met à jour le ACCESS_TOKEN dans le fichier .env
        update_env_var("ACCESS_TOKEN", data["access_token"])

        # Si un nouveau refresh_token est présent dans la réponse, on le met à jour aussi
        if "refresh_token" in data:
            print("Nouveau refresh_token trouvé !")
            update_env_var("REFRESH_TOKEN", data["refresh_token"])

        return data["access_token"]
    else:
        print("❌ Erreur lors du rafraîchissement du token :", data)
        return None


def get_valid_access_token():
    if ACCESS_TOKEN:
        return ACCESS_TOKEN

    # Si le token d'accès n'existe pas, on le rafraîchit
    if REFRESH_TOKEN:
        return refresh_access_token(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)

    print("❌ Aucun token valide trouvé.")
    return None


def update_env_var(key, value):
    lines = []
    found = False

    # Lire les lignes existantes
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, "r") as file:
            lines = file.readlines()

    # Mettre à jour ou ajouter la variable
    with open(ENV_FILE, "w") as file:
        for line in lines:
            if line.startswith(f"{key}="):
                file.write(f"{key}={value}\n")
                found = True
            else:
                file.write(line)
        if not found:
            file.write(f"{key}={value}\n")
