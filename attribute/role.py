from attribute.attribute import Attribute

class Role(Attribute):
    """Class for the attribute Subjects"""
    _validation_pattern = r"(Student|Teacher)"
    _validation_error_message = "role is not valid"
