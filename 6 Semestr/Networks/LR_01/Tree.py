from helperFunctions import *

class Root():
    def __init__(self, data):
        self.data = data
        self.child = []

    def findChild(self, word):
        for c in self.child:
            if c.data == word:
                return c
    
    def existChild(self, word):
        for c in self.child:
            if c.data == word:
                return True
        return False


class Tree():
    def __init__(self, list):
        self.mainRoot = Root("/")
        for l in list:
            curRoot = self.mainRoot
            words = removeEmptyElements(l.replace("?", "/").replace("=", "/").split("/"))
            for w in words:
                if curRoot.existChild(w):
                    curRoot = curRoot.findChild(w)
                else:
                    newRoot = Root(w)
                    curRoot.child.append(newRoot)
                    curRoot = newRoot

    def onPrint(self):
        return recursionPrint(self.mainRoot, "", 0)
        

def recursionPrint(root, text, number):
    text += " " * 25*number + "|" + root.data + "\n"
    
    for c in root.child:
        text  = recursionPrint(c, text, number + 1)
    return text





    



