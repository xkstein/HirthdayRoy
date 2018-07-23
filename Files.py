import json

    
class Folder():
    # each file object should know it's containing folder, and what it contains.
    def __init__(self, name, Contents, container, encrypted, password):
        self.name = name
        self.contents = Contents
        self.container = container
        self.ecrypted = bool
        self.password = password
        
    def getContents(self):
        for key in self.contents:
            inside = []
            inside.append(key)
            print(inside)

Zone1 = Folder("Zone1", {"junk":"trunk","bad":"good"}, "HomeZone", True, "Funk")

#print(Zone1.contents)
Zone1.getContents()
        


        
