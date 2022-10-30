from attribute.attribute import Attribute

class Subjects(Attribute):
    """Classs for the attribute FullName"""
    _validation_pattern = r"(Matemáticas|Física|Química|Biología|Lengua|Inglés|Francés|Alemán|Historia|Geografía|Filosofía|Economía|Dibujo Técnico|Informática|Educación Física|Religión)"
    _validation_error_message = "subject is not valid"