import json


class JoinUs(object):
    def __init__(self,
                 request_id=None,
                 name=None,
                 college_name=None,
                 phone=None,
                 consent=None,
                 country=None,
                 email=None,
                 is_success=None,
                 exceptions=None
                 ):
        self.request_id = request_id
        self.name = name
        self.college_name = college_name
        self.phone = phone
        self.consent = consent
        self.country = country
        self.email = email
        self.is_execution_success = is_success
        self.exceptions = exceptions

    @classmethod
    def from_join_request(cls, raw_message):
        raw_message_json = json.loads(raw_message)
        data = raw_message_json["data"]
        name = data.get("name")
        college_name = data.get("college_name")
        phone = data.get("phone")
        consent = data.get("consent")
        country = data.get("country")
        email = data.get("email")
        is_execution_success = raw_message_json["success"]
        exceptions = raw_message_json.get("exceptions", [])
        request_id = raw_message_json["request_id"]

        # obj = cls(name, college_name, phone, consent, country, email, is_execution_success, exceptions, request_id)
        obj = {
            "request_id": request_id,
            "success": is_execution_success,
            "exception": exceptions,
            "data": {
                "name": name,
                "college_name": college_name,
                "phone": phone,
                "email": email,
                "country": country,
                "consent": consent
            }
        }
        return obj

    def update(self, is_success=None, exceptions=None):
        assert all([is_success, exceptions])

        self.is_execution_success = is_success
        self.exceptions = exceptions

    def serialize(self):
        return {
            "request_id": self.request_id,
            "success": self.is_execution_success,
            "exception": self.exceptions,
            "data": {
                "name": self.name,
                "college_name": self.college_name,
                "phone": self.phone,
                "email": self.email,
                "country": self.country,
                "consent": self.consent
            }
        }
