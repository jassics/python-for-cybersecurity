# pip3 install pyshorteners
import pyshorteners

url = input("Long url: ")

# shorteners without API key
shortener = pyshorteners.Shortener()
print("tiny.url: ", shortener.tinyurl.short(url))
print("os.db url: ", shortener.osdb.short(url))
print("is.gd url: ", shortener.isgd.short(url))

