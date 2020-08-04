import os
import logging
from enum import Enum, auto
import pymongo
from configs.interface import Queue

STANDARD_DATE_FORMAT = "YYYY-MM-DD"


class MyQueues(Queue):
    REQUEST_QUEUE = f"https://sqs.ap-south-1.amazonaws.com/611334599981/-kflow-test-L1"
    DEAD_LETTER_QUEUE = f"https://sqs.ap-south-1.amazonaws.com/611334599981/-kflow-test-L1"

    @staticmethod
    def from_arn(arn):
        *_, service, region, account_id, queue_name = arn.strip().split(":")
        queue_url = f"https://{service}.{region}.amazonaws.com/{account_id}/{queue_name}"
        return MyQueues.from_url(queue_url)

    @staticmethod
    def from_url(url):
        return MyQueues(url)


client = pymongo.MongoClient('example.com', ssl=True)
