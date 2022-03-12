def appendUnique(list, element):

    if "\\n" in element:
        first = element.find('\\n')
        second = element.rfind('\\n')
        element = element[: first] + element [second + 2 :]

    if not (element in list):
        list.append(element)

def removeEmptyElements(list):
    newlist = []
    for l in list:
        if l != "":
            newlist.append(l)
    return newlist

def listToText(list):
    text = ""
    for l in list:
        text += l+"\n"
    return text

def unionList(list1, list2):
    for element in list2:
        if not (element in list1):
            list1.append(element)

def removeURLWithV(list):
    list2 = []
    for l in list:
        if not("?" in l):
            list2.append(l)
    return list2

def checkOuterLink(link):
    return "http" in link or "https" in link or "#" in link or "." in link