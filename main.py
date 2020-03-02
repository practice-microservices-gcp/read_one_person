from controllers.search_id_controller import readOnePerson
from response_decorator.response_decorator import http_response
import json

@http_response
def read_one_person(request):
    return readOnePerson(request.args['code'])