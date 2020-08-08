from abc import ABC
import json
import app_constants
from global_file import get_db_object
from interface import HandlerInterface
from resources import db_config
import uuid
import logging

class RequestHandler(HandlerInterface, ABC):
    def __init__(self, data, config):
        super().__init__(db_config)
        self.data = data
        self.db_object = get_db_object(db_config)
        self.request_id = uuid.uuid1()

    def save_data(self, data):
        logging.info("========INSERTING TO DB==========")
        self.db_object.insert_one({
            "info": data
        })

    def business_data(self, data):
        pass

    def operate(self):
        print("======OPERATING ON THE PASSED DATA======")
        _data = self.data
        logging.info(f"Data passed to be dumped {json.dumps(_data)}")
        duplicate_count_query = {"info.data.email": _data["data"]["email"]}
        duplicate_count = self.db_object.find(duplicate_count_query).count()
        if duplicate_count > 0:
            _data["exception"] = _data["exception"].append(["Data Already there"])
            _data["data"]["success"] = "Failed"
            print(f"=== Data already exist=={str(json.dumps(_data))}")
            raise Exception
        else:
            try:
                _data["request_id"] = str(uuid.uuid1())
                if _data["data"]["country"] == "INDIA":
                    _data["data"]["phone"] = app_constants.INDIA + _data["data"]["phone"]
                RequestHandler.save_data(self, _data)
            except Exception as e:
                logging.error(f"ERROR================{e}")
