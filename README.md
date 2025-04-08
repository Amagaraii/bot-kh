# 💫 KH_Bot – Bot Discord avec Intégration Twitch

Un bot Discord développé en Python, qui :
- Envoie une citation de Kingdom Hearts via `!khquote`
- Souhaite la bienvenue aux nouveaux membres
- Surveille les streamers Twitch et notifie quand ils passent en live

---

## 🚀 Fonctionnalités

- 📜 Commande `!khquote` pour une citation aléatoire de KH
- 👋 Message de bienvenue automatique dans `#général`
- 🔴 Notification dans `#🔴-live` dès qu’un streamer est en live
- 🛠️ Commandes admin : `!reloadcache`, `!checknow`, `!showcache`

---

## 🛠️ Prérequis

- Python 3.10+ (idéalement)
- Un **bot Discord** enregistré sur [Discord Developer Portal](https://discord.com/developers/applications)
- Une application **Twitch** sur [Twitch Developer Portal](https://dev.twitch.tv/console)

---

## ⚙️ Installation

### 1. Cloner le projet

git clone https://github.com/ton-user/kh-bot.git
cd kh-bot

2. Créer un environnement virtuel

python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # macOS/Linux

3. Installer les dépendances
pip install -r requirements.txt

4. Créer le fichier .env
À la racine du projet, crée un fichier .env :

DISCORD_TOKEN=ton_token_discord
CLIENT_ID=ton_client_id_twitch
CLIENT_SECRET=ton_client_secret_twitch
REFRESH_TOKEN=ton_refresh_token_twitch
ACCESS_TOKEN=token_temporaire_twitch
STREAMERS=ShaoRedfields
ADMIN_IDS=123456789012345678
ℹ️ STREAMERS peut contenir plusieurs pseudos séparés par des virgules.
ℹ️ ADMIN_IDS doit contenir les IDs Discord autorisés à utiliser les commandes admin.



🧪 Lancer le bot

python bot.py
Tu verras quelque chose comme :

KH_Boty#0351 est prêt à protéger les cœurs et à suivre les lives !
🎮 Démarrage de la surveillance des streamers...




📦 Arborescence

kh-bot/
├── bot.py
├── twitch_integration.py
├── twitch_token_manager.py
├── stream_cache.json
├── requirements.txt
├── .env
└── README.md


💬 Commandes disponibles
Commande	Description	Accès
!khquote	Affiche une citation aléatoire de KH	Tout le monde
!reloadcache	Réinitialise le cache des lives Twitch	Admin
!checknow	Force une vérification immédiate des lives	Admin
!showcache	Affiche le cache actuel	Admin


🧠 Notes utiles
Le fichier stream_cache.json empêche les notifications en double.

Les tokens Twitch expirent, mais un système de rafraîchissement automatique est en place.

Le bot s’attend à ce que tu aies un canal textuel nommé exactement 🔴-live dans ton serveur Discord.

L’interface twitch_token_manager.py gère automatiquement les mises à jour du .env lors du refresh des tokens.

👨‍💻 Auteur
👋 Projet développé par Angel
🎮 Kingdom Hearts dans le cœur, code dans les veines
