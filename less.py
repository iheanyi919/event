print("hello chris")

from urllib import request

k = request.urlopen("https://www.chelseanews.com")
print(k.getcode())
print(k.read())
