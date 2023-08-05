from entities.person import Person

class Professor(Person):
    def __init__(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, id_professor):
        super().__init__(nombre, apellido_paterno, apellido_materno, fecha_nacimiento)
        self.id_professor = id_professor