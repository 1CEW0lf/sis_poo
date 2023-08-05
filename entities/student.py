from entities.person import Person

class Student(Person):
    def __init__(self, nombre, ap_paterno, ap_materno, fech_nacimiento, matr):
        super().__init__(nombre, ap_paterno, ap_materno, fech_nacimiento)
        self.matricula = matr