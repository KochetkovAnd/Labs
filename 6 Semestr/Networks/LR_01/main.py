from HTTPhelper import *
from Tree import *
from Parser import *
from helperFunctions import *

def getListByHost(host):
    port = 80
    info = "/"
    return recursiveCheck([], info, 0, host, port)

def recursiveCheck(allURL, info, number, host, port):
    helper = HTTPHelper(host, port)
    appendUnique(allURL, info)
    if number < 5:    

        helper.sendRequest(info, host)
        URLList = getURL(helper.getResponse())

        removeAlreadyChecked(allURL, URLList)

        for URL in URLList:
            allURL = recursiveCheck(allURL,URL, number + 1, host, port)

    return allURL