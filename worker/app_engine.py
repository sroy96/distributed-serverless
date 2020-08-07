from joinus import JoinUs
import json


class DataHandler(object):
    def __init__(self, class_handler, event, config):
        self.class_handler = class_handler
        self.event = event
        self.config = config

    def process(self):
        print("============INVOKING PROCESS==============")
        # logger.info(f"Start Processing the {self.class_handler.__name__}")
        for raw_message in self.event.get('Records'):
            try:
                message_body = raw_message['body']
                data = JoinUs.from_join_request(message_body)
                self.class_handler(data,
                                   self.config).operate()
            except Exception as e:
                print("ERROR OCCURRED ......", e)
                # logger.error("Error in Batch Handler Data: ", exc_info=True)
                # logger.error(traceback.format_exc())


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

        # meta.update({
        #     "logDetails": log_details
        # })

        super().__init__(**kwargs)
