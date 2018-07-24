import json
from Files import Folder
from User import User 

# This next bit just opens the json temporarily as fp and parses it with json.load()
with open('resources/main.json', 'r') as fp:
    jsonData = json.load(fp)

mainFolder = Folder(jsonData["name"], jsonData["unlocked"], jsonData["pass"], jsonData["container"], jsonData["contents"])

'''
I think User.look makes this functionally obsolete, but I don't really wanna delete it yet because it prints the 
entire contents which may be nice for debuging

def printContents(contents):
    for i in range(len(contents)):
        print(contents[i].name)
        for object in contents[i].contents:
            print(contents[i].contents[object].name)
'''

def Game():
    user = User(mainFolder)
    user.look()
    while True:
        #print(currentDirectory.name)
        command_input = input('\nCommand: ')
        user.runCommand(command_input)
        #printcontents(currentDirectory.getContents())
        
Game()

