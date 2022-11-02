from attribute.attribute import Attribute

class Subjects(Attribute):
    """Class for the attribute Subjects"""
    _validation_pattern = r"(Mathematics|Physics|Chemistry|Biology|Language|English|French|German|History|Geography|Philosophy|Economics|Technical Drawing|Computer Science|Physical Education|Religion)"
    _validation_error_message = "subject is not valid"
