import json
from Files import Folder 

mainFolder = Folder("MainFolder", {"wack":"hack"}, None, False, None,"Folder")

def printcontents(contents):
    for i in range(len(contents)):
        print(contents[i])

def Game():
    running = bool
    currentDirectory = mainFolder
    while running == True:
        print(currentDirectory.name)
        command_input = input('Command: ')
        #printcontents(currentDirectory.getContents())
        

Game()
