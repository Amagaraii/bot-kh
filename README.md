# 🤖 Discord Twitch Notification Bot

Bot Discord permettant de notifier automatiquement lorsqu’un ou plusieurs streamers Twitch passent en live.

---

## 🚀 Fonctionnalités

* 🔴 Détection automatique des lives Twitch
* 📢 Notification dans un salon Discord avec embed
* 🔁 Rafraîchissement automatique du token Twitch (OAuth)
* 👥 Support de plusieurs streamers
* 💾 Cache local pour éviter le spam (détection de changement d’état)
* ⚡ Commande Discord personnalisée (`!khquote`)
* 🧠 Architecture asynchrone (Python async)

---

## 🛠️ Stack technique

* Python 3.12
* discord.py
* aiohttp
* requests
* dotenv

---

## 📁 Structure du projet

```
bot-kh/
├── bot.py
├── twitch_integration.py
├── twitch_token_manager.py
├── requirements.txt
├── .env
└── live_status_cache.json
```

---

## ⚙️ Installation

### 1. Cloner le projet

```
git clone <repo>
cd bot-kh
```

---

### 2. Créer un environnement virtuel

```
py -3.12 -m venv .venv
```

Activation (Git Bash) :

```
source .venv/Scripts/activate
```

---

### 3. Installer les dépendances

```
python -m pip install -r requirements.txt
```

---

## 🔐 Configuration

Créer un fichier `.env` à la racine :

```
DISCORD_TOKEN=your_discord_token
CLIENT_ID=your_twitch_client_id
CLIENT_SECRET=your_twitch_client_secret
REFRESH_TOKEN=your_twitch_refresh_token
ACCESS_TOKEN=your_twitch_access_token
STREAMERS=Streamer1,Streamer2
```

---

## ▶️ Lancer le bot

```
python bot.py
```

---

## 🧪 Utilisation

### Commande Discord

```
!khquote
```

→ Envoie une citation aléatoire

---

### Notifications Twitch

* Le bot vérifie toutes les 5 minutes
* Envoie un message dans le salon `🔴-live`
* Mentionne `@everyone` quand un streamer passe en live

---

## 🔄 Gestion des tokens Twitch

Le bot :

* utilise un `access_token`
* le renouvelle automatiquement via le `refresh_token`
* met à jour le `.env` automatiquement

---

## ⚠️ Sécurité

Ajouter dans `.gitignore` :

```
.env
.venv
```

Ne jamais partager :

* tokens Discord
* tokens Twitch

---

## 📈 Améliorations possibles

* Gestion multi-serveurs
* Logs avancés
* Retry / backoff API
* Déploiement Docker / VPS
* Configuration dynamique par serveur

---

## 👨‍💻 Auteur

Projet réalisé par Angel dans le cadre d’un apprentissage du développement full stack et des intégrations API.

---

## 📄 Licence

Projet libre d’utilisation à des fins éducatives.
