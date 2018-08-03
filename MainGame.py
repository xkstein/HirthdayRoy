import json
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
        commandInput = input('\nCommand: ')
        user.runCommand(commandInput)

Game()

