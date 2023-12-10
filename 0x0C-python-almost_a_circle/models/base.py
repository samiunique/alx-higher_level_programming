import json
import csv
import turtle

class Base:
    """ Private class attribute """
    __nb_objects = 0
    """ Set to store used IDs """
    used_ids = set()

    def __init__(self, id=None):
        if id is not None:
            if id in Base.used_ids:
                raise ValueError("ID already in use")
            self.id = id
            """ Add the ID to used_ids """
            Base.used_ids.add(id)
        else:
            Base.__nb_objects += 1
            new_id = Base.__nb_objects
            """ Find a non-used ID """
            while new_id in Base.used_ids:
                Base.__nb_objects += 1
                new_id = Base.__nb_objects
            self.id = new_id
            Base.used_ids.add(new_id)

    def to_json_string(list_dictionaries):
        """ Return the JSON serialization of a list of dicts. """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

