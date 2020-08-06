from . import logger
import json
import traceback
from .joinus import JoinUs


class DataHandler(object):
    def __init__(self, class_handler, event, config, meta=None, ):
        logger.debug(f"Creating Data Handler Object, from cls ===> {class_handler.__name__}")
        self.class_handler = class_handler
        self.event = event
        self.config = config
        self.meta = meta

    def process(self):
        logger.info(f"Start Processing the {self.class_handler.__name__}")
        error_flag = False
        for raw_message in self.event.get("Records"):
            try:
                body = json.loads(raw_message["body"]) #body is string form
                data = JoinUs.from_join_request(body)
                print(f"==>Data retrieved for= {data.name} <==", data.serialize())
                self.class_handler(data=data.serialize(),
                                   meta=self.meta,
                                   config=self.config).operate()
            except Exception as e:
                error_flag = True
                logger.error("Error in Batch Handler Data: ", exc_info=True)
                logger.error(traceback.format_exc())


class DataHandlerAWS(DataHandler):
    def __init__(self, context=None, meta=None, **kwargs):
        if context:
            log_details = {
                "logGroup": context.log_group_name,
                "logStream": context.log_stream_name,
                "lambdaRequestId": context.aws_request_id
            }
        else:
            log_details = None

        if not meta:
            meta = {}

        meta.update({
            "logDetails": log_details
        })

        super().__init__(meta=meta, **kwargs)
