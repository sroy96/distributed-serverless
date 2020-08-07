class InternalStatusCodes:

    def authenticatiion_api(self):
        status_store = {
            101: "Valid Authentication"
        }
        return status_store

    def ocr_api(self):
        status_store = {
            101: "Successful OCR"
        }
        return status_store

    def http_status_description(self):
        message_store = {
            200: "Request Successful",
            400: "Mandatory fields are missing / invalid",
            401: "API Key is missing or invalid.",
            402: "Credits to access the APIs expired.",
            500: "Internal processing error of Karza.",
            503: "The source for authentication is down for maintenance or inaccessible.",
            504: "The response latency from the source for authentication is > 30sec."

        }
        return message_store

    def http_status_message(self):
        status_store = {
            200: "OK",
            400: "Bad Request",
            401: "Unauthorized Access",
            402: "Insufficient Credits",
            500: "Internal Server Error",
            503: "Source Unavailable",
            504: "Endpoint Request Timed Out"
        }
        return status_store
