import json
from .resources import MyQueues, client
from .handlers import RequestHandler, DeadLetterQueueHandler
from .app_engine import DataHandlerAWS
from . import logger

mapping: {
    MyQueues.REQUEST_QUEUE: RequestHandler,
    MyQueues.DEAD_LETTER_QUEUE: DeadLetterQueueHandler
}


def lambda_handler(event, context):
    queue_enum = MyQueues.from_arn(event["Records"][0]["eventSourceARN"])
    meta = {"queue": queue_enum}
    handler_class = mapping[queue_enum]
    logger.info(f"===> Events received from the queue {queue_enum.name},"
                f" invoking handled {handler_class.__name__} <====")
    return DataHandlerAWS(class_handler=handler_class, event=event, context=context, meta=meta, config=client).process()
