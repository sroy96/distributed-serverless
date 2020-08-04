import json
from .resources import MyQueues, db_config
from .handlers import RequestHandler
from .app_engine import DataHandlerAWS
from . import logger

# MyQueues.DEAD_LETTER_QUEUE: DeadLetterQueueHandler
mapping: {
    MyQueues.REQUEST_QUEUE: RequestHandler,
}


def lambda_handler(event, context):
    queue_enum = MyQueues.from_arn(event["Records"][0]["eventSourceARN"])
    meta = {"queue": queue_enum}
    handler_class = mapping[queue_enum]
    logger.info(f"===> Events received from the queue {queue_enum.name},"
                f" invoking handled {handler_class.__name__} <====")
    return DataHandlerAWS(class_handler=handler_class, event=event, context=context, meta=meta,
                          config=db_config).process()
