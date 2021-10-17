# <h2>Star-Wars-API</h2>

SpotDraft Star Wars Backend assignment:<br>
A Favourites app that exposes REST APIs for Star Wars data. <br>
You can find my project live at: https://starwarz-backend-api.herokuapp.com/ <br><br>

The JSON api used is https://swapi.dev/.<br>
Tools used:<br>
Language & Framework: Python, Flask<br>
Database: Mongodb atlas<br><br>

Endpoints<br>
Endpoints for planets:<br>
1. Endpoint: /api/planets <br>
Method: GET<br>
Resonse: Info of all planets<br><br>

2. Endpoint : /api/planets/<name><br>
Query parameter: name (name takes the name of the planet)<br>
Method: GET<br>
Response: Returns the creation date, last updation date, is_favourite.<br><br>

3. Endpoint: /api/planets/favourite<br>
Method: GET<br>
Response: Returns all planets which are set as favourite by user<br><br>
    
 4. Endpoint: /api/planets/favourite<br>
Method: PUT<br>
Query parameters:<br>
    favourite :(set as True or False)<br>
    custom_name: if users wants to set a custom name for planet<br>
Response: Returns all planets which are set as favourite by user<br><br>

Endpoints for movies:<br>
1. Endpoint: /api/movies <br>
Method: GET<br>
Resonse: Info of all movies<br><br>

2. Endpoint : /api/movies/<name><br>
Query parameter: name (name takes the name of the planet)<br>
Method: GET<br>
Response: Returns the release date, last updation date, created_date, is_favourite<br><br>

3. Endpoint: /api/movies/favourite<br>
Method: GET<br>
Response: Returns all movies which are set as favourite by user<br><br>
    
 4.3. Endpoint: /api/movies/favourite<br>
Method: PUT<br>
Query parameters:<br>
    favourite :(set as True or False)<br>
    custom_name: if users wants to set a custom name for movie<br>
Response: Returns all movies which are set as favourite by user.<br><br>
    
Insertion of data into MongoDB:<br><br>

    movies_url = "https://swapi.dev/api/films/"<br>
response = requests.get(movies_url)<br>
data = response.json()<br>
temp_list = []<br>
for movie in data['results']:<br>
    dic = {}<br>
    dic['title'] = movie.get('title')<br>
    dic['release_date'] = movie.get('release_date')<br>
    dic['created'] = movie.get('created')<br>
    dic['updated'] = movie.get('created')<br>
    dic['url'] = movie.get('url')<br>
    dic['is_favourite'] = False<br>
    temp_list.append(dic)<br><br>

db = client['StarWars']<br>
movies_collection = db['movies']<br>
movies_collection.insert(temp_list)<br><br>

planets_url = "https://swapi.dev/api/planets/"<br>
response = requests.get(planets_url).json()<br>
planets_data = []<br>
for planet in response['results']:<br>
    dic = {}<br>
    dic['name'] = planet.get('name')<br>
    dic['created'] = planet.get('created')<br>
    dic['updated'] = planet.get('created')<br>
    dic['url'] = planet.get('url')<br>
    dic['is_favourite'] = False<br>
    planets_data.append(dic)<br><br>

db = client['StarWars']<br>
movies_collection = db['planets']<br>
movies_collection.insert(planets_data)<br>



