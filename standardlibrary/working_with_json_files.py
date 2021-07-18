import json
from pathlib import Path
movies = [
    { "id": 1, "title": "Terminator","year"  :1989 },
    { "id": 2, "title": "Kindergarten Cop","year"  :1993 },
    { "id": 3, "title": "Matrix","year"  :2000 },
    { "id": 4, "title": "Basic Instinct","year"  :2002 }
]

data = json.dumps(movies)
print("\n json Data\n")
print(data)
Path("movies.json").write_text(data)

jsonData = Path("movies.json").read_text()
movies = json.loads(jsonData)
print("\n movies array of dictionaries \n")
print(jsonData)
print(movies[0])
print(movies[1]["title"])