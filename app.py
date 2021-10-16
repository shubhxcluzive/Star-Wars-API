from flask import Flask, request
from bson.json_util import dumps
import re
from datetime import datetime
import pymongo
import dns

app = Flask(__name__)

client = pymongo.MongoClient(os.environ.get(star_war_db_key))
db = client['StarWars']
movies_collection = db['movies']
planets_collection = db['planets']


def return_to_json(data):
    response = app.response_class(
        response=dumps(data),
        status=200,
        mimetype='application/json')
    return response


@app.route('/')
def home_page():
    return "Welcome to Star Warz"


@app.route('/api/planets', methods=["GET"])
def get_planets():
    #planets_collection.update_many({}, {"$set": {"custom_name": ""}})
    page = int(request.args.get("page", 1))
    per_page = 10
    res = planets_collection.find().sort('name').skip(per_page * (page - 1)).limit(per_page)
    return return_to_json(res)


@app.route('/api/planets/<name>', methods=["GET"])
def get_planet_byname(name):
    planet = list(planets_collection.find({"name":re.compile(name, re.IGNORECASE)}))[0]
    return return_to_json(planet)


@app.route('/api/movies', methods=["GET"])
def get_movies():
    #movies_collection.update_many({}, {"$set": {"custom_name": ""}})
    page = int(request.args.get("page", 1))
    per_page = 10
    res = movies_collection.find().sort('title').skip(per_page * (page - 1)).limit(per_page)
    return return_to_json(res)


@app.route('/api/movies/<title>', methods=["GET"])
def get_movie_byname(title):
    movie = list(movies_collection.find({"title": re.compile(title, re.IGNORECASE)}))
    return return_to_json(movie)


@app.route('/api/planets/favourite', methods=['PUT'])
def set_planet_favourite():
    name = request.args.get("name")
    isSet = request.args.get("favourite", "true")
    custom_name = request.args.get("custom_name", "")
    search = {"name": re.compile(name, re.IGNORECASE)}
    planet = list(planets_collection.find(search))[0]
    if isSet.lower() == "true":
        if planet['is_favourite'] == True and custom_name != "":
            updated_values = {"$set": {'is_favourite': True, 'updated': str(datetime.now()), "custom_name": custom_name}}
            planets_collection.update_one(search, updated_values)
        elif planet['is_favourite']:
            return return_to_json({"message": "Planet is already set to as favourite True"})
        updated_values = {"$set": {'is_favourite': True, 'updated': str(datetime.now()), "custom_name": custom_name}}
        planets_collection.update_one(search, updated_values)

    elif isSet.lower() == "false":
        if planet['is_favourite'] == False:
            return return_to_json({"message": "Planet is already set to as favourite False"})
        updated_values = {"$set": {'is_favourite': False, 'updated': str(datetime.now())}}
        planets_collection.update_one(search, updated_values)
    return return_to_json(planets_collection.find({"name":re.compile(name, re.IGNORECASE)}))


@app.route('/api/movies/favourite', methods=['PUT'])
def set_movie_favourite():
    title = request.args.get("title")
    isSet = request.args.get("favourite", "true")
    search = {"title": re.compile(title, re.IGNORECASE)}
    movie = list(movies_collection.find(search))[0]
    custom_name = request.args.get("custom_name", "")
    if isSet.lower() == "true":
        if movie['is_favourite'] == True and custom_name != "":
            updated_values = {"$set": {'is_favourite': True, 'updated': str(datetime.now()), "custom_name": custom_name}}
            movies_collection.update_one(search, updated_values)
        elif movie['is_favourite']:
            return return_to_json({"message": "Movie is already set to as favourite True"})
        updated_values = {"$set": {'is_favourite': True, 'updated': str(datetime.now()), "custom_name":custom_name}}
        movies_collection.update_one(search, updated_values)
    elif isSet.lower() == "false":
        if movie['is_favourite'] == False:
            return return_to_json({"message": "Movie is already set to as favourite False"})
        updated_values = {"$set": {'is_favourite': False, 'updated': str(datetime.now())}}
        movies_collection.update_one(search, updated_values)
    return return_to_json(movies_collection.find({"title":re.compile(title, re.IGNORECASE)}))


@app.route('/api/planets/favourite', methods=['GET'])
def get_planet_favourite():
    page = int(request.args.get("page", 1))
    per_page = 10
    res = planets_collection.find({'is_favourite': True}).sort('name').skip(per_page * (page - 1)).limit(per_page)
    return return_to_json(res)


@app.route('/api/movies/favourite', methods=['GET'])
def get_movie_favourite():
    page = int(request.args.get("page", 1))
    per_page = 10
    res = movies_collection.find({'is_favourite': True}).sort('title').skip(per_page * (page - 1)).limit(per_page)
    return return_to_json(res)


if __name__ == '__main__':
    app.run(debug=True)
