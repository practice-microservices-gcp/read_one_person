import traceback

from entities.people_entity import PeopleEntity
from entities.response_entity import ResponseEntity
from facades.id_facade import idFacade
from responses import responses
from people_repository.people_repository import peopleRepository

def readOnePerson(id):

    try:
        if (not idFacade.idValidation(id)):
            raise responses.WrongRequest
        else:
            id = int(id)

        personModel = peopleRepository.searchPersonById(id)
        person = PeopleEntity(personModel[0], personModel[1], personModel[2])
        response = ResponseEntity('200 ', person)

        return response
    except responses.WrongRequest:
        message = responses.http_responses['WrongRequest']['message']
        code = responses.http_responses['WrongRequest']['code']
        return ResponseEntity(code, message)
    except responses.NotFound:
        message = responses.http_responses['NotFound']['message']
        code = responses.http_responses['NotFound']['code']
        return ResponseEntity(code, message)
    except Exception:
        print(traceback.format_exc())
        message = responses.http_responses['UnexpectedError']['message']
        code = responses.http_responses['UnexpectedError']['code']
        return ResponseEntity(code, message)

