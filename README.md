# Star-Wars-API
# Star-Wars

SpotDraft Star Wars Backend assignment:
A Favourites app that exposes REST APIs for Star Wars data. 
You can find my project live at: https://starwarz-backend-api.herokuapp.com/

The JSON api used is https://swapi.dev/.
Tools used:
Language & Framework: Python, Flask
Database: Mongodb atlas

Endpoints
Endpoints for planets:
1. Endpoint: /api/planets 
Method: GET
Resonse: Info of all planets
2. Endpoint : /api/planets/<name>
Query parameter: name (name takes the name of the planet)
Response: Returns the creation date, last updation date, is favourite
Method: PUT
3. Endpoint: /api/planets/favourite

Endpoints for movies:
1. Endpoint: /api/movies 
Method: GET
Resonse: Info of all planets
2. Endpoint : /api/movies/<title>
3. Endpoint :/api/movies/favourite

Insertion of data into MongoDB:

movies_url = "https://swapi.dev/api/films/"
response = requests.get(movies_url)
data = response.json()
temp_list = []
for movie in data['results']:
    dic = {}
    dic['title'] = movie.get('title')
    dic['release_date'] = movie.get('release_date')
    dic['created'] = movie.get('created')
    dic['updated'] = movie.get('created')
    dic['url'] = movie.get('url')
    dic['is_favourite'] = False
    temp_list.append(dic)

db = client['StarWars']
movies_collection = db['movies']
movies_collection.insert(temp_list)

planets_url = "https://swapi.dev/api/planets/"
response = requests.get(planets_url).json()
planets_data = []
for planet in response['results']:
    dic = {}
    dic['name'] = planet.get('name')
    dic['created'] = planet.get('created')
    dic['updated'] = planet.get('created')
    dic['url'] = planet.get('url')
    dic['is_favourite'] = False
    planets_data.append(dic)

db = client['StarWars']
movies_collection = db['planets']
movies_collection.insert(planets_data)



