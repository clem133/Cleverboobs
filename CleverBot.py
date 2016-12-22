# _*_ coding:utf-8 _*_
import asyncio
import discord
import logging
import random
import os
import time
from cleverbot import Cleverbot
logging.basicConfig(level=logging.INFO)
client = discord.Client()
servers = list(client.servers)
cb = Cleverbot()

@client.async_event
def on_message(message):
        if message.content.startswith('#GO'):
                yield from client.change_status(discord.Game(name=random.choice(["dibou","rtichau","Broutter","la claire fontaine","bricot"])))
                yield from client.send_message(message.channel, 'Bonjour je suis ton papi')
                return
        if message.author == client.user:
                return
        if not message.author.id == '181436810654777344':
                return
        yield from client.send_typing(message.channel)
        O = cb.ask(message.content)
        
        time.sleep(2)
        print (O)
        yield from client.send_message(message.channel,O.format(message))







print ('CleverClem Bot Pret!!')
client.run('clemen.landier3@gmail.com','3690741')

