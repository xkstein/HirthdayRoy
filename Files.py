import json

    
class Folder():
    # each file object should know it's containing folder, and what it contains.
    def __init__(self, name, Contents, container, encrypted, password, fileType):
        self.name = name
        self.contents = Contents
        self.container = container
        self.ecrypted = bool
        self.password = password
        
    def getContents(self):
        for key in self.contents:
            inside = []
            inside.append(key)
        return inside


#print(Zone1.contents)
#Zone1.getContents()
