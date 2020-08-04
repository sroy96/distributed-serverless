from abc import ABC
from configs.global_file import get_db_object
from configs.interface import HandlerInterface
import random
from . import logger


class RequestHandler(HandlerInterface, ABC):
    def __int__(self, data, meta, config):
        super().__init__(config)
        self.data = data
        self.meta = meta
        self.db_object = get_db_object(config)
        self.request_id = random.random()

    def save_data(self, request_id, data):
        self.db_object.insert_one({
            "requestId": request_id,
            "data": data
        })

    def business_data(self, data):
        pass

    def operate(self):
        request_id = self.request_id
        data = self.data
        try:
            RequestHandler.save_data(self, request_id, data)
            logger.info(f"Data has been save successfully")
        except Exception:
            logger.error("Pessimistic Lock error")
            # Try it in dead letter queue
