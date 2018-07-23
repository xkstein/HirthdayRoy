import json
from Files import Folder 

# This next bit just opens the json temporarily as fp and parses it with json.load()
with open('resources/main.json', 'r') as fp:
    jsonData = json.load(fp)

mainFolder = Folder(jsonData["name"], jsonData["unlocked"], jsonData["pass"], jsonData["container"], jsonData["contents"])

def printContents(contents):
    for i in range(len(contents)):
        print(contents[i].name)

def Game():
    printContents(mainFolder.contents)
    running = bool
    currentDirectory = mainFolder
    while running == True:
        print(currentDirectory.name)
        command_input = input('Command: ')
        #printcontents(currentDirectory.getContents())
        

Game()
