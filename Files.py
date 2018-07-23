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
            elif (item["fileType"] == "file"):
                contents[x] = File(item["name"], item["unlocked"], item["pass"], item["path"])
        
        self.contents = contents

    
    '''    
    def getContents(self):
        for keys in self.contents:
            inside = []
            inside.append(key)
        return inside
    '''

class File():
    # Alright, what I've learned is that exec(open('file.txt').read()) actually runs the code now, so I may just do that instead of filetypes
    def __init__(self, Name, Unlocked, Password, Path):
        self.name = Name
        self.unlocked = Unlocked
        self.password = Password
        self.path = Path

#print(Zone1.contents)
#Zone1.getContents()
