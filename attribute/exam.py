from attribute.attribute import Attribute

class Exam(Attribute):
    """Class for the attribute FullName"""
    _validation_pattern = r"[A-Za-z0-9]{1,25}( [A-Za-z0-9]{1,25})?"
    _validation_error_message = "exam is not valid"