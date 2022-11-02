from attribute.attribute import Attribute

class Name(Attribute):
    """Class for the attribute Name"""
    _validation_pattern = r"[A-Za-z]{2,25}( [A-Za-z]{2,25})?"
    _validation_error_message = "name is not valid"
    