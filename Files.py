import json
    
class Folder():
    # each file object should know it's containing folder, and what it contains.
    def __init__(self, Name, Unlocked, Password, Container, Contents):
        self.name = Name
        self.unlocked = Unlocked
        self.password = Password
        self.container = Container
        
        contents = {}
        # This next bit basically goes through each entry in the contents and declares objects for each storing them in self.contents 
        for x in range(0, len(Contents)):
            item = Contents[x]
            if (item["fileType"] == "folder"):
                contents[x] = Folder(item["name"], item["unlocked"], item["pass"], item ["container"], item["contents"])
            elif (item["fileType"] == "textFile"):
                contents[x] = TextFile(item["name"], item["unlocked"], item["pass"], item["words"])
        
        self.contents = contents

    
    '''    
    def getContents(self):
        for keys in self.contents:
            inside = []
            inside.append(key)
        return inside
    '''

class TextFile():
    # Alright, so I hope this isn't what we'll do, but rn Words holds the content of the file
    def __init__(self, Name, Unlocked, Password, Words):
        self.name = Name
        self.unlocked = Unlocked
        self.password = Password
        self.words = Words

#print(Zone1.contents)
#Zone1.getContents()
