import json
import random
ROLE_FILE = open('role3.json','r')
ROLE_LIST = json.load(ROLE_FILE)
print(len(ROLE_LIST))

print(ROLE_LIST[random.choice(list(ROLE_LIST.keys()))])
