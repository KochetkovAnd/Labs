from HTTPhelper import *
from Tree import *
from Parser import *
from helperFunctions import *

def getListByHost(host):
    port = 80
    info = "/"
    return checkURL(host, port, [], "/")

def checkURL(host, port, checkedURL, startInfo):
    
    checkedURL.append(startInfo)

    for info in checkedURL:
        helper = HTTPHelper(host, port)
        helper.sendRequest(info, host)
        URLList = getURL(helper.getResponse().replace("\\r", ""))
        unionList(checkedURL, URLList)

    return checkedURL    