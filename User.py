import Files

class User():
    def __init__(self, StartFolder):
        # I know this is bad un-modular code, but like ahhh, I'm going to assume that we'll only declare users at start
        self.fullDir = StartFolder
        self.currentDir = StartFolder

    # So this basically processes the strings sent over by the MainGame object and runs the methods they envoke
    def runCommand(self, query):
        query = query.split(" ")
        if (hasattr(self, query[0]) and len(query) >= 2):
            getattr(self, query[0])(query[1])
            return None
        elif (hasattr(self, query[0]) and len(query) == 1):
            getattr(self, query[0])()
            return None
        print("Command not recognized, please try again ")
    
    # This just takes a filename, cycles through all the contents of a folder for a match and runs it's code if its a file object
    def open(self, fileName):
        for i in range(0, len(self.currentDir.contents)):
            if (fileName == self.currentDir.contents[i].name):
                if (type(self.currentDir.contents[i]) is Files.File):
                    exec(self.currentDir.contents[i].path)
                    return None
                else:
                    print("That appears to be the incorrect filetype, try entering 'enter " + fileName + "' if you're attempting to change directories")
    
    # This works the same as open() just it makes self.currentFolder the matching folder
    def enter(self, folderName):
        print("looking for " + folderName + ". . .")
        for i in range(0, len(self.currentDir.contents)):
            if (folderName == self.currentDir.contents[i].name):
                if (type(self.currentDir.contents[i]) is Files.Folder):
                    self.currentDir = self.currentDir.contents[i]
                    print("Sucessfully entered directory " + folderName)
                    return None
                else: 
                    print("That item has the incorrect filetype, try entering 'open " + folderName + "' if you're attempting to run a file")

    # Bro idk how to write this off the top of my head. Current thinking is to actually have the game cycle through all the fucking contents of all the possible folders until it matches self.contents and then fucking just set it equal to the last. that can't be most efficient though
    def back(self):
        for object in self.fullDir.contents:
            if (self.fullDir.contents[object] == self.currentDir):
                self.currentDir = self.fullDir

    # This cycles through every entry in the contents of currentDir and prints a list of their names
    def look(self):
        print("Contents of current directory: ")
        dirObjects = []
        for object in self.currentDir.contents:
            dirObjects.append(self.currentDir.contents[object].name)
        print(*dirObjects, sep="\n")

    def help(self):
        print("Availible functions: \n\nopen ['file name']\nenter ['directory name']\nback\nlook\nquit")
        return None

    # This quits the application
    def quit(self):
        exit()
