"""Contains common errors when handing resources in Daos.
"""
class DuplicateIdInCollection(Exception):
    "Raised when there is a duplicate id in the collection"
    pass

class IdNotExistInCollection(Exception):
    "Raised when there is a no id in the collection"
    pass