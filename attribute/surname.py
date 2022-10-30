from attribute.attribute import Attribute

class Surname(Attribute):
    """Classs for the attribute FullName"""
    _validation_pattern = r"[A-Za-z]{2,25}"
    _validation_error_message = "surname is not valid"