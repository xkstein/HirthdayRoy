import Files

class User():
    def __init__(self, StartFolder):
        # I know this is bad un-modular code, but like ahhh, I'm going to assume that we'll only declare users at start
        self.fullDir = StartFolder
        self.currentDir = StartFolder

    def runCommand(self, query):
        print("Alright")
    
    # This just takes a filename, cycles through all the contents of a folder for a match and runs it's code if its a file object
    def open(self, fileName):
        for i in range(0, len(self.currentDir.contents)):
            if (fileName == self.currentDir.contents[i].name):
                print("Match")
                if (type(self.currentDir.contents[i]) is Files.File):
                    exec(self.currentDir.contents[i].path)
                    return None
    
    # This works the same as open() just it makes self.currentFolder the matching folder
    def enter(self, folderName):
        print("looking for " + folderName + ". . .")
        for i in range(0, len(self.currentDir.contents)):
            if (folderName == self.currentDir.contents[i].name):
                if (type(self.currentDir.contents[i]) is Files.Folder):
                    self.currentDir = self.currentDir.contents[i]
                    print("Sucessfully entered directory " + folderName)
                    return None

    def look(self):
        print("Looking for items in directory " + self.currentDir.name)
        dirObjects = []
        for object in self.currentDir.contents:
            dirObjects.append(self.currentDir.contents[object].name)
        return dirObjects
