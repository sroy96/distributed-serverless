import configs.app_constants
from configs.interface import Queue

STANDARD_DATE_FORMAT = "YYYY-MM-DD"


class MyQueues(Queue):
    REQUEST_QUEUE = f"https://sqs.ap-south-1.amazonaws.com/996119619820/flow_queue"
    DEAD_LETTER_QUEUE = f"https://sqs.ap-south-1.amazonaws.com/996119619820/flow_queue"

    @staticmethod
    def from_arn(arn):
        *_, service, region, account_id, queue_name = arn.strip().split(":")
        queue_url = f"https://{service}.{region}.amazonaws.com/{account_id}/{queue_name}"
        return MyQueues.from_url(queue_url)

    @staticmethod
    def from_url(url):
        return MyQueues(url)


db_config = {
    "DB_URI": configs.app_constants.DB_URL,
    "DB_NAME": configs.app_constants.DB_NAME,
    "DATA_COLLECTION_NAME": configs.app_constants.DATA_COLLECTION_NAME
}
