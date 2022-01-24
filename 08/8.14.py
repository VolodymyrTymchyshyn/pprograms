import json
dicti={"name":"venom","year":2020,"opinion":"ęąuper"}
with open("favourite.json","w") as f:
    f.write(json.dumps([dicti],ensure_ascii=False))