import json, os
from Files import Folder
from User import User 

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
    user = User()
    while True:
        # dunno, kinda wanted to show what folder hes in, im sure theres a more intuative elegant way, go wild
        commandInput = input('\nQuestAIDS~/' + user.currentDir.name + '/~$ ')
        user.runCommand(commandInput)

os.system("clear")
print("Welcome to QUEST AIDS\n[working title. yeah uncertain what you want this to look like, everything I've added is just placeholder, go wild]\n\ntry entering 'help'\n")
Game()

