import urllib.request


URL = "https://www.youtube.com/user/guru99com"

webURL = urllib.request.urlopen(URL)

data = webURL.read()

print(data)