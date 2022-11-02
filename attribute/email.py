from attribute.attribute import Attribute

class Email(Attribute):
    """Class for the attribute FullName"""
    _validation_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    _validation_error_message = "email is not valid"