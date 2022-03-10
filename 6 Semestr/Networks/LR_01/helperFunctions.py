def appendUnique(list, element):
    if not (element in list):
        list.append(element)

def removeAlreadyChecked(checkedList, list):
    for URL in checkedList:
        if URL in list:
            list.remove(URL)

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