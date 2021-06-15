import os
os.environ['MPLCONFIGDIR'] = "./matplotlib"
import matplotlib.pyplot as plt 
from datetime import datetime
import random
import numpy as np
from replit import db


saveFolder = './matplotlib/'
saveFormat = '.png'

def genDateID():
  #return datetime.now().strftime('%Y%m-%d%H-%M%S')
  return datetime.now().strftime('%Y%m-%d%H-%M')

#Returns two arrays containing the x (1st array) axis data and y (2nd array) axis data
def createDailyTrend():
  y1440 = [0] * 1440
  xTime = list(range(0, 1440))
  y1440[0] = random.randint(1, 1000)
  y1440[1439] = random.randint(1, 1000)

  numOfTrends = random.randint(1, 20)
  for val in range(numOfTrends):    
    randomPointInTime = random.randint(1, 1439)
    randomVal = random.randint(1, 1000)
    y1440[randomPointInTime] = randomVal

  yTrend = []
  xTrend = []
  i = 0
  for val in y1440:
    if val > 0:
      yTrend.append(val)
      xTrend.append(i)
    i = i + 1

  x = 0
  for val in y1440:
    if val == 0:
      y1440[x] = np.interp(x, xTrend, yTrend)
    x = x + 1

  return xTime, y1440

def saveTrendData():
  x, y = createDailyTrend()
  today = [x, y]
  db[datetime.now().strftime('%Y-%m-%d')] = today



def saveGraph():
  return 1

def generateGraph(x, y):
  # line 1 points 
  savePath = './matplotlib/graph.png'
  x1 = [1,2,3] 
  y1 = [2,4,1] 
  # plotting the line 1 points  
  plt.plot(x1, y1, label = "line 1") 
    
  # naming the x axis 
  plt.xlabel('Time') 
  # naming the y axis 
  plt.ylabel('$$$') 
  # giving a title to my graph 
  plt.title('Two lines on same graph!') 
    
  # show a legend on the plot 
  plt.legend() 
    
  # function to show the plot 
  plt.savefig(savePath)
  return savePath

def genGraph():
  savePath = './matplotlib/' + genDateID() + '.png'
  x, y = createDailyTrend()
  #save daily tren

def genGraphNow():
  timeInMin = (datetime.now().hour * 60) + datetime.now().minute
  dailyTrends = db[datetime.now().strftime('%Y-%m-%d')]
  xData = dailyTrends[0]
  yData = dailyTrends[1]

def displayGraph(path):
  return 1





