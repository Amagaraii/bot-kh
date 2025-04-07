Bonjour, bienvenue sur ce projet de bot pour un de mes streamer ! https://www.twitch.tv/shaoredfields

c'est un bot (peut importe le nom du bot) qui lance des annonce de début de live automatiquement dans un salon discord que vous pouvez nommé comme vous le souhaitez du moment que vous le changer dans le code (quand le processus est lancé : bot.py) -> python bot.py 

pour commencé si vous cloner ce repo je serais ravis de le voir ce faire utiliser / amélioré bien entendu il ne s'agit que d'un début 

ÉTAPE 1 :

cloner le repo ... une fois fait lancé le dossier dans lequel il est maintenant ! il y a un fichier texte qui sert a installer ce qu'il y est utilisé pour faire marcher le bot.
on ouvre le terminal ! vous devez être au bon endroit du dossier c'est a dire a ça racine de la ou il a les fichiers -> pip install -r requirements.txt

a partir de la il ne reste vraiment pas grand chose a faire selon votre IDE il vous faut une env (environnement virtuel) ATTENTION c'est ce qui prend le plus de poids dans le dossier -> python -m venv env -> env\Scripts\activate


ÉTAPE 2 : 

Crée votre bot sur https://dev.twitch.tv/console et https://discord.com/developers/applications 

pour discord : 

Clique sur "New Application"
Donne un nom à ton bot (ex : Bot_incroyable) puis clique sur Create

🤖 2. Créer le bot dans l'application
Dans la sidebar gauche, clique sur "Bot"

Clique sur "Add Bot", puis Yes, do it!

Tu peux ensuite :

Changer son avatar
Modifier son nom
Activer l’option "MESSAGE CONTENT INTENT" si ton bot lit les messages (message_content = True dans ton code)


Pour twitch : 

1. Créer ton application Twitch
Va sur : https://dev.twitch.tv/console

Connecte-toi avec ton compte Twitch.

Clique sur le bouton "Applications" dans la barre latérale.
Clique sur "Register Your Application" (en haut à droite).
Remplis les infos :
Name : ce que tu veux (ex : Bot_de_fou).
OAuth Redirect URLs : http://localhost
Category : coche "Application intégrée"
Clique sur "Create"

📦 2. Récupérer les identifiants
Après création, tu verras ton application dans la liste.

Clique dessus, et tu auras :
Client ID ✅
Client Secret (tu dois cliquer sur "New Secret" si c’est la première fois) ✅

ÉTAPE 3 : 

Maintenant qu'on en est la on vas crée un fichier .env ou on vas pouvoir renseigner tous ce qu'on a besoin au bon fonctionnement du bot !

on vas avoir besoin d'un token discord pour le bot : DISCORD_TOKEN=votre_token_discord (a écrire dans le .env) Clique sur "Reset Token" pour générer un nouveau token dans le portail discord ⚠️ Ne partage jamais ce token — c’est la clé d’accès à ton bot.

Pour Twitch on vas avoir CLIENT_ID et CLIENT_SECRET pareil a mettre dans votre .env -> Après création, tu verras ton application dans la liste.

Clique dessus, et tu auras :
Client ID ✅
Client Secret (tu dois cliquer sur "New Secret" si c’est la première fois) ✅
