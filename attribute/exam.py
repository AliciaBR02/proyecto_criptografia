from attribute.attribute import Attribute

class Exam(Attribute):
    """Classs for the attribute FullName"""
    _validation_pattern = r"[A-Za-z0-9]{2,25}( [A-Za-z0-9]{2,25})?"
    _validation_error_message = "exam is not valid"