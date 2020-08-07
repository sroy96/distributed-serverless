from abc import ABC
from global_file import get_db_object
from interface import HandlerInterface
from resources import db_config
import uuid

class RequestHandler(HandlerInterface, ABC):
    def __init__(self, data, config):
        super().__init__(db_config)
        self.data = data
        self.db_object = get_db_object(db_config)
        self.request_id = uuid.uuid1()

    def save_data(self, request_id, data):
        print("========INSERTING TO DB==========")
        print(str(data))
        self.db_object.insert_one({
            "requestId": request_id,
            "data": data
        })

    def business_data(self, data):
        pass

    def operate(self):
        print("======OPERATING ON THE PASSED DATA======")
        request_id = self.request_id
        data = self.data
        try:
            RequestHandler.save_data(self, request_id, data)
            # logger.info(f"Data has been save successfully")
        except Exception as e:
            print("ERROR================", e)
    # logger.error("Pessimistic Lock error")
    # Try it in dead letter queue
