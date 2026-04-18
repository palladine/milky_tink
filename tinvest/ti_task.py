from . import methods
from .errors import get_error_by_code

class Task:
    def __init__(self, service=None, method=None, body_name_request=None, 
                body_name_response=None, params=None, is_stream=False):
        self.service = service
        self.method = method
        self.body_name_request = body_name_request
        self.body_name_response = body_name_response
        self.params = params if params else {}

        try:
            self.data = getattr(methods, f'setParams{self.method}')(**self.params)
        except Exception as e:
            return(get_error_by_code(707, self, e))
