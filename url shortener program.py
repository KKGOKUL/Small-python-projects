import pyshorteners
url=input("Enter or copy the URL that you want to short: ")
surl=pyshorteners.Shortener().tinyurl.short(url)
print("Shortened URL is: " +surl)
