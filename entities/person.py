from datetime import datetime
class Person:
    def __init__(self, nombre, ap_paterno, ap_materno, fech_nacimiento):
        self.nombre = nombre
        self.apellido_paterno = ap_paterno
        self.apellido_materno = ap_materno
        self.fecha_nacimiento = fech_nacimiento

    def calcular_edad(self):
        fecha = datetime.strptime(self.fecha_nacimiento, "%Y-%m-%d")
        hoy = datetime.now()
        edad = hoy.year - fecha.year - ((hoy.month, hoy.day) < (fecha.month, fecha.day))
        return edad
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
    