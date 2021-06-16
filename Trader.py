from replit import db

class Trader:
    def __init__(self, user, money):
      self.user = user
      self.money = 1000.00
      db[self.user] = self.money

def subtractMoney(id, val):
  if checkUserExists(id):
    user = db[id]
    user["money"] = user["money"] - val
    db[id] = user
    return "New Balance: " + str(user["money"])
  else:
    return "User does not exist."

def addMoney(id, val):
  if checkUserExists(id):
    user = db[id]
    user["money"] = user["money"] + val
    db[id] = user
    return "New Balance: " + str(user["money"])
  else:
    return "User does not exist."

def addShares(id, shareAmt):
  if checkUserExists(id):
    user = db[id]
    user["shares1"] = user["shares1"] + shareAmt
    db[id] = user
    return "Successfully added shares"
  else:
    return "User does not exist."

def sellShares(id, toSell):
  if checkUserExists(id):
    user = db[id]
    if toSell <= user["shares1"]:
      user["shares1"] = user["shares1"] - toSell
      db[id] = user
      return "Shares sold!"
    else:
      return "Sorry, you don't have enough shares to sell!"


def checkMoney(id):
  if checkUserExists(id):
    user = db[id]
    return "Current balance: " + str(user["money"])
  else:
    return "User does not exist."

def regUser(id):
  if not checkUserExists(id):
    db[id] = {"id": id, "money": 1000.00, "shares1": 0}
    return "User created!"
  else:
    return "User already exists!"

def checkUserExists(id):
  keys = db.keys()
  for key in keys:
    if id == key:
      return True
  return False

def debug():
  keys = db.keys()
  for k in keys:
    print("Keys: " + k)
    value = db[k]
    print(value)

def clearDB():
  keys = db.keys()
  for k in keys:
    del db[k]
    