from abc import ABC

from configs.interface import HandlerInterface


class RequestHandler(HandlerInterface, ABC):
    def __int__(self, data, meta, config):
        self.data = data
        self.meta = meta
        self.config = config
        super().__init__(config)

    def operate(self):
        #save data to mongo
        pass
