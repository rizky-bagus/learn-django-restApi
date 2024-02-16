from rest_framework.response import Response

class BasedResponse(Response):
    """
    A custom response class for Django REST Framework that adds a `status_code`
    attribute to the response data.
    """
    def __init__(self, data=None, status_code=None, success=None, message=None, **kwargs):
        data = {
            'code': status_code,
            'success' : success,
            'message': message,
            'data': data
        }
        super().__init__(data, **kwargs)
