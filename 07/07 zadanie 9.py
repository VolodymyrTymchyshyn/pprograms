file = open('/Users/a111/Library/Application Support/Microsoft/Teams/Service Worker/CacheStorage/db0c921df77539e32ddd04f4bf5a5b44c13b38e3/index.txt','r')
s=0
for i in file:
    s+=int(i)
print(s)
file.close()
