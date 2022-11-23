from attribute.attribute import Attribute

class Role(Attribute):
    """Class for the attribute Subjects"""
    _validation_pattern = r"(s|t)"
    _validation_error_message = "role is not valid"
