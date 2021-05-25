from json import JSONEncoder
class CustomJsonEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__