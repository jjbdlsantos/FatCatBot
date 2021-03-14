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

def checkMoney(id):
  if checkUserExists(id):
    user = db[id]
    return "Current balance: " + str(user["money"])
  else:
    return "User does not exist."

def regUser(id):
  if not checkUserExists(id):
    db[id] = {"id": id, "money": 1000.00}
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
    