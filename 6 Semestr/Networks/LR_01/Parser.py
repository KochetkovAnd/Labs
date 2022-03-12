import re
from helperFunctions import *

def getURL(page):
    regex = '<a href="[^"\']+"'
    URLList = re.findall(regex, page)

    InnerLinkList = []

    for URL in URLList:
        URL = URL[9:-1]
        if not checkOuterLink(URL) and URL != "/":
            appendUnique(InnerLinkList, URL)  

    return InnerLinkList