urls = {"google":"google.com",18:"unesco.org"}
print(urls["google"])
print(urls.get("google"))
print("google" in urls)
print("google.com" in urls)
print("google.com" in urls.values())

print(len(urls))
print(urls.keys())
print(urls.values())
print(urls.items())