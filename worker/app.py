from resources import MyQueues, db_config
from handlers import RequestHandler
from app_engine import DataHandlerAWS
import logging


mapping = {
    MyQueues.REQUEST_QUEUE: RequestHandler,
}


def lambda_handler(event, context):
    queue_enum = MyQueues.from_arn(event["Records"][0]["eventSourceARN"])
    meta = {"queue": queue_enum}
    handler_class = mapping[queue_enum]
    logging.info(f"===> Events received invoking handled {handler_class.__name__} <====")
    return DataHandlerAWS(class_handler=handler_class, event=event, config=db_config).process()
