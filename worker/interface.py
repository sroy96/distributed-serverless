from abc import abstractmethod, abstractclassmethod
from enum import Enum


class NextResource(Enum):
    pass


class Lambda(NextResource):
    pass


class Queue(NextResource):
    pass


class HandlerInterface(object):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def save_data(self, request_id, data):
        raise NotImplementedError

    @abstractmethod
    def business_data(self, data):
        raise NotImplementedError
