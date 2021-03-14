import discord
import os
from StockMarket import genGraph
from Trader import regUser, checkMoney, clearDB

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as: {0.user}'.format(client))

@client.event
async def on_message(message):
  currentUser = str(message.author.id)
  if message.author == client.user:
    return

  if message.content.startswith('$$$today'):
    await message.channel.send('Howdy!')
    await message.channel.send(file=discord.File(genGraph()))
    print(message.author)

  if message.content.startswith('$$$reg'):
    print("Current User is: " + currentUser)
    await message.channel.send(regUser(currentUser))

  if message.content.startswith('$$$bal'):
    await message.channel.send(checkMoney(currentUser))

  if(message.content.startswith('$debug')):
    clearDB()

client.run(os.getenv('TOKEN'))