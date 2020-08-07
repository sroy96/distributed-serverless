import status_constants
import json
import pymongo


def authentication_response_load(status_enum):
    _exp = status_constants.InternalStatusCodes()
    print(_exp.authenticatiion_api()[status_enum])


def ocr_response_load(status_enum):
    _exp = status_constants.InternalStatusCodes()
    print(_exp.ocr_api()[status_enum])


def http_response_message(status_enum, _key):
    _exp = status_constants.InternalStatusCodes()
    print(_exp.http_status_message()[status_enum])


def http_response_description(status_enum):
    _exp = status_constants.InternalStatusCodes()
    print(_exp.http_status_description()[status_enum])


def json_serializer(data: dict):
    return json.dumps(data)


def json_deserializer(data: str):
    return json.loads(data)


def get_db_object(config):
    mongo_connection = pymongo.MongoClient(config["DB_URI"])
    mongo_db = mongo_connection[config["DB_NAME"]]
    mongo_db_collection = mongo_db[config["DATA_COLLECTION_NAME"]]
    return mongo_db_collection
