# <h1>Star-Wars-API</h1>

SpotDraft Star Wars Backend assignment:<br>
A Favourites app that exposes REST APIs for Star Wars data. <br>
You can find my project live at: https://starwarz-backend-api.herokuapp.com/ <br>

The JSON api used is https://swapi.dev/.<br>
<h6>Language & Framework used: Python, Flask</h6>
<h6>Database: Mongodb atlas<br></h6>

<h3>Endpoints</h3>
Endpoints for planets:<br>
1. Endpoint: <i>/api/planets</i> <br>
<b>Method</b>: GET<br>
<b>Response</b>: Info of all planets<br>
2. Endpoint:  <i>/api/planets/{name}<br></i>
<b>Query parameter</b>: name (name takes the name of the planet)<br>
<b>Method</b>: GET<br>
<b>Response</b>: Returns the creation date, last updation date, is_favourite.<br><br>

3. Endpoint: <i>/api/planets/favourite<br></i>
<b>Method:</b> GET<br>
<b>Response:</b> Returns all planets which are set as favourite by user<br><br>
    
 4. Endpoint: <i>/api/planets/favourite<br></i>
<b>Method:</b> PUT<br>
<b>Query parameters:</b><br>
    favourite :(set as True or False)<br>
    custom_name: if users wants to set a custom name for planet<br>
<b>Response:</b> Returns all planets which are set as favourite by user<br><br>

<h6>Endpoints for movies:</h6>
1. Endpoint: <i>/api/movies <br></i>
<b>Method:</b> GET<br>
<b>Response:</b> Info of all movies<br><br>

2. Endpoint :<i> /api/movies/<name></i><br>
<b>Query parameter:</b> name (name takes the name of the planet)<br>
<b>Method:</b> GET<br>
<b>Response:</b> Returns the release date, last updation date, created_date, is_favourite<br><br>

3. Endpoint: <i>/api/movies/favourite<br></i>
<b>Method:</b> GET<br>
<b>Response:</b> Returns all movies which are set as favourite by user<br><br>
    
 4. Endpoint: <i>/api/movies/favourite<br></i>
<b>Method:</b> PUT<br>
<b>Query parameters:</b><br>
    favourite :(set as True or False)<br>
    custom_name: if users wants to set a custom name for movie<br>
Response: Returns all movies which are set as favourite by user.<br><br>
    
<h6>Insertion of data into MongoDB:</h6>

    movies_url = "https://swapi.dev/api/films/"
```python:
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



