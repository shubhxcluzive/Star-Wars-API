from flask import Flask, request, jsonify
from bson.json_util import dumps
import requests, re
from datetime import datetime
import pymongo
import dns
app = Flask(__name__)
'''

- The favorite API should also allow setting a custom title/name to the movie/planet

- Additionally, the list APIs must support searching by title/name



'''
client = pymongo.MongoClient('mongodb+srv://starwarz:starwarz143@starwars.niitn.mongodb.net/test')
db = client['StarWars']
movies_collection = db['movies']
planets_collection = db['planets']



@app.route('/api/planets', methods=["GET"])
def get_planets():
    page = int(request.args.get("page", 1))
    per_page = 10
    res = planets_collection.find().sort('name').skip(per_page * (page - 1)).limit(per_page)
    return dumps(res)

@app.route('/api/planets/<name>', methods=["GET"])
def get_planet_byname(name):
    planet = list(planets_collection.find({"name":re.compile(name, re.IGNORECASE)}))[0]
    return dumps(planet)

@app.route('/api/movies', methods=["GET"])
def get_movies():
    page = int(request.args.get("page", 1))
    per_page = 10
    res = movies_collection.find().sort('title').skip(per_page * (page - 1)).limit(per_page)
    return dumps(res)

@app.route('/api/movies/<title>', methods=["GET"])
def get_movie_byname(title):
    movie = list(movies_collection.find({"title": re.compile(title, re.IGNORECASE)}))
    return dumps(movie)

@app.route('/api/planets/favourite', methods=['PUT'])
def set_planet_favourite():
    name = request.args.get("name")
    isSet = request.args.get("favourite", "true")
    search = {"name": re.compile(name, re.IGNORECASE)}
    planet = list(planets_collection.find(search))[0]
    if isSet.lower() == "true":
        if planet['is_favourite'] == True:
            return dumps({"message": "Planet is already set to as favourite True"})
        updated_values = {"$set": {'is_favourite': True, 'updated': str(datetime.now())}}
        planets_collection.update_one(search, updated_values)

    elif isSet.lower() == "false":
        if planet['is_favourite'] == False:
            return dumps({"message": "Planet is already set to as favourite False"})
        updated_values = {"$set": {'is_favourite': False, 'updated': str(datetime.now())}}
        planets_collection.update_one(search, updated_values)
    return dumps(planets_collection.find({"name":name}))

@app.route('/api/movies/favourite', methods=['PUT'])
def set_movie_favourite():
    title = request.args.get("title").title()
    isSet = request.args.get("favourite", "true")
    search = {"title": title}
    movie = list(movies_collection.find(search))[0]
    if isSet.lower() == "true":
        if movie['is_favourite'] == True:
            return dumps({"message": "Movie is already set to as favourite True"})
        updated_values = {"$set": {'is_favourite': True, 'updated': str(datetime.now())}}
        movies_collection.update_one(search, updated_values)
    elif isSet.lower() == "false":
        if movie['is_favourite'] == False:
            return dumps({"message": "Movie is already set to as favourite False"})
        updated_values = {"$set": {'is_favourite': False, 'updated': str(datetime.now())}}
        movies_collection.update_one(search, updated_values)
    return dumps(movies_collection.find({"title":title}))





if __name__ == '__main__':
    app.run(debug=True)
