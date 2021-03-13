import discord
import os
os.environ['MPLCONFIGDIR'] = "./matplotlib"
import matplotlib.pyplot as plt 

def genGraph():
  # line 1 points 
  savePath = './matplotlib/graph.png'
  x1 = [1,2,3] 
  y1 = [2,4,1] 
  # plotting the line 1 points  
  plt.plot(x1, y1, label = "line 1") 
    
  # line 2 points 
  x2 = [1,2,3] 
  y2 = [4,1,3] 
  # plotting the line 2 points  
  plt.plot(x2, y2, label = "line 2") 
    
  # naming the x axis 
  plt.xlabel('x - axis') 
  # naming the y axis 
  plt.ylabel('y - axis') 
  # giving a title to my graph 
  plt.title('Two lines on same graph!') 
    
  # show a legend on the plot 
  plt.legend() 
    
  # function to show the plot 
  plt.savefig(savePath)
  return savePath

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as: {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$$$today'):
    await message.channel.send('Howdy!')
    await message.channel.send(file=discord.File(genGraph()))

client.run(os.getenv('TOKEN'))