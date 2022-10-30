from attribute.attribute import Attribute

class Name(Attribute):
    """Classs for the attribute FullName"""
    _validation_pattern = r"[A-Za-z]{2,25}( [A-Za-z]{2,25})?"
    _validation_error_message = "name is not valid"
    