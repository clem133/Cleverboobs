# _*_ coding:utf-8 _*_
import asyncio
import discord
import logging
import os
import random
import time
from cleverbot import Cleverbot
logging.basicConfig(level=logging.INFO)
client = discord.Client()
cb = Cleverbot()

@client.async_event
def on_message(message):
        if message.content.startswith('#GO'):
                yield from client.change_status(discord.Game(name=random.choice(["dibou","rtichau","Broutter","la claire fontaine","bricot","rien"])))
                return
        if message.author == client.user:
                return
        if not message.author.id == '179942811800436736':
                return
        yield from client.send_typing(message.channel)
        O = cb.ask(message.content)
        time.sleep(2)
        print (O)
        yield from client.send_message(message.channel,O.format(message))






print ('CleverBot2 Pret!!')
client.run('mail','mdp')

