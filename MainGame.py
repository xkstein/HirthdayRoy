import json
from Files import Folder
from User import User 

# This next bit just opens the json temporarily as fp and parses it with json.load()
with open('resources/main.json', 'r') as fp:
    jsonData = json.load(fp)

mainFolder = Folder(jsonData["name"], jsonData["unlocked"], jsonData["pass"], jsonData["container"], jsonData["contents"])

def printContents(contents):
    for i in range(len(contents)):
        print(contents[i].name)
        for object in contents[i].contents:
            print(contents[i].contents[object].name)

def Game():
    user = User(mainFolder)
    print(user.look())
    user.enter('location1')
    print(user.look())
    currentDirectory = mainFolder
    printContents(mainFolder.contents)
    running = bool
    #currentDirectory = mainFolder
    while running == True:
        print(currentDirectory.name)
        command_input = input('Command: ')
        #printcontents(currentDirectory.getContents())
        
Game()

