import re

class IdFacade():

    def idValidation(self, id):
        numRegExp = re.compile('^([\s\d]+)$')
        return numRegExp.match(id)


idFacade = IdFacade()