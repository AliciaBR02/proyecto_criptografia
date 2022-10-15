class Profesor:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.asignaturas = []
    def insertar_asignatura(self, asignatura):
        # comprobar que la string está bien
        if asignatura == "":
            return -1
        # comprobar que existe la clase
        if asignatura not in self.asignaturas:
            self.asignaturas.append(asignatura)
            return 0
        return -1
    # podríamos hacer un json para cada clase, y dentro de cada examen/item poner el nombre del profe y alumno
    # asignatura.json