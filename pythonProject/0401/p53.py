d = {}
urls = {"google":"google.com",18:"unesco.org"}

urls["x"] = 2560
print(urls)

urls["x"] = 1920
print(urls)

del urls["x"]
print(urls.pop(18))
print(urls.clear())