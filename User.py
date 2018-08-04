import Files
import json

class User():
    def __init__(self):
        # I know this is bad un-modular code, but like ahhh, I'm going to assume that we'll only declare users at start
        self.path = []
        self.reinitFolders()

    def reinitFolders(self):
        with open('resources/main.json', 'r') as fp:
            jsonData = json.load(fp)
        self.fullDir = Files.Folder(jsonData["name"], jsonData["unlocked"], jsonData["pass"], jsonData["container"], jsonData["contents"])
        
        if not self.path:
            self.currentDir = self.fullDir
        else:
            self.findDir()
            self.currentDir = eval(self.dirString)

    # jsonData[contents][0][contents][1]
    def findJsonDir(self):
        self.jsonDir = 'jsonData' + ''.join('["{i}"][{j}]'.format(i = self.path[k][0], j = self.path[k][1]) for k in range(0, len(self.path)))

    def unlockItem(self, item):
        userInput = input("This item is locked\n\nEnter password: ").lower().split()
        for i in range(0, len(userInput)):
            if (userInput[i] == item.password):
                print('Password Approved')
                self.findJsonDir()
                with open('resources/main.json', '+r') as fp:
                    jsonData = json.load(fp)
                    exec(self.jsonDir + '["unlocked"] = True')
                    fp.seek(0)
                    json.dump(jsonData, fp, indent=4)
                    fp.truncate()
                del self.path[len(self.path) - 1]
                self.reinitFolders()
    
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
                    if (not self.currentDir.contents[i].unlocked):
                        self.path.append(['contents', i])
                        self.unlockItem(self.currentDir.contents[i])
                    if (self.currentDir.contents[i].unlocked):
                        exec(self.currentDir.contents[i].path)
                        return None
                    else:
                        print("Incorrect Password")
                else:
                    print("That appears to be the incorrect filetype, try entering 'enter " + fileName + "' if you're attempting to change directories")
    
    # This works the same as open() just it makes self.currentFolder the matching folder
    def enter(self, folderName):
        for i in range(0, len(self.currentDir.contents)):
            if (folderName == self.currentDir.contents[i].name):
                if (type(self.currentDir.contents[i]) is Files.Folder):
                    if (not self.currentDir.contents[i].unlocked):
                        self.path.append(['contents', i])
                        self.unlockItem(self.currentDir.contents[i])
                    if (self.currentDir.contents[i].unlocked):
                        self.path.append(['contents', i])
                        self.currentDir = self.currentDir.contents[i]
                        print("Sucessfully entered directory " + folderName)
                        return None
                    else:
                        print('incorrect password')
                else: 
                    print("That item has the incorrect filetype, try entering 'open " + folderName + "' if you're attempting to run a file")

    def findDir(self):
        if (self.path):
            self.dirString = 'self.fullDir' + ''.join('.{i}[{j}]'.format(i = self.path[k][0], j = self.path[k][1]) for k in range(0, len(self.path)))
        else:
            self.dirString = 'self.fullDir'

    # this reads to see if the current dir has a path (if it doesnt its in the mainfolder) and goes to the string of the path made by parentDir
    def back(self):
        if self.path:       # I almost can't believe this works
            del self.path[len(self.path)-1]
            self.findDir()
            self.currentDir = eval(self.dirString)
            print("Changing directory to " + self.currentDir.name)
        else:
            print("What the fuck, I can't find the parent folder, fucking what")

    # This cycles through every entry in the contents of currentDir and prints a list of their names
    def look(self):
        print("\nContents of current directory: \n")
        dirObjects = []
        for object in self.currentDir.contents:
            dirObjects.append(self.currentDir.contents[object].name)
        print(*dirObjects, sep="\n")

    def help(self):
        print("\nAvailible functions: \n\nopen ['file name']       <- Opens files\nenter ['directory name'] <- Enters folder\nback                     <- Goes back to the previous directory\nlook                     <- Scans current folder and prints contents\nquit")
        return None

    # This quits the application
    def quit(self):
        exit()
