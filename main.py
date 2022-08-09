#!/usr/bin/env python

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config

TOKEN = config.API_TOKEN

def start(update, context):
    update.message.reply_text("""
Bienvenue sur le bot officiel de tcollart.

Les commandes disponibles sont :
- /site pour obtenir l'adresse du site
- /youtube pour obtenir la chaîne YouTube
- /linkedin pour obtenir son profil Linkedin
    """)

def fonction(update, context):
    update.message.reply_text("Un message à répondre en fonction de la commande saisie par l'utilisateur")

def pas_compris(update, context):
    update.message.reply_text('Je n\'ai pas compris votre message', update.message.text )

def main():
    # La classe Updater permet de lire en continu ce qu'il se passe sur le channel
    updater = Updater(TOKEN, use_context=True)

    # Pour avoir accès au dispatcher plus facilement
    dp = updater.dispatcher

    # On ajoute des gestionnaires de commandes
    # On donne a CommandHandler la commande textuelle et une fonction associée
    dp.add_handler(CommandHandler("cmd", fonction))

    # Pour gérer les autres messages qui ne sont pas des commandes
    dp.add_handler(MessageHandler(Filters.text, pas_compris))

    # Sert à lancer le bot
    updater.start_polling()

    # Pour arrêter le bot proprement avec CTRL+C
    updater.idle()


if __name__ == '__main__':
    main()
