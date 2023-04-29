#!/usr/bin/python3
'''
    Views BLuePrint
'''
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.state import State
from models.review import Review
from models.city import City


@app_views.route('/status', strict_slashes=False)
def statusApi():
    '''
    returns a JSON: "status": "OK"
    '''
    return jsonify({'status': 'OK'})


@app_views.route('/stats', strict_slashes=False)
def stats_api():
    '''
    /stats endpoint will return JSON formatted stats on all data
    '''
    return jsonify({
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    })


if __name__ == '__main__':
    pass
