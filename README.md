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
Method: GET
Response: Returns the creation date, last updation date, is_favourite

3. Endpoint: /api/planets/favourite
Method: GET
Response: Returns all planets which are set as favourite by user
    
 4. Endpoint: /api/planets/favourite
Method: PUT
Query parameters:
    favourite :(set as True or False)
    custome_name: if users wants to set a custom name for planet
Response: Returns all planets which are set as favourite by user

Endpoints for movies:
1. Endpoint: /api/movies 
Method: GET
Resonse: Info of all movies

2. Endpoint : /api/movies/<name>
Query parameter: name (name takes the name of the planet)
Method: GET
Response: Returns the release date, last updation date, created_date, is_favourite

3. Endpoint: /api/movies/favourite
Method: GET
Response: Returns all movies which are set as favourite by user
    
 4.3. Endpoint: /api/movies/favourite
Method: PUT
Query parameters:
    favourite :(set as True or False)
    custome_name: if users wants to set a custom name for movie
Response: Returns all movies which are set as favourite by user
    
    
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



