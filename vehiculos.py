
class Vehiculos():
    color = 'blanco'

    def __init__(self,nombre='',velocidad_maxima=0,kilometraje=0) -> None:
        self.nombre = nombre
        self.velocidad_max = velocidad_maxima
        self.kilometraje = kilometraje

    def __str__(self) -> str:
        return f'Nombre: {self.nombre},Velocidad_Max:{self.velocidad_max},Kilometraje:{self.kilometraje}'


class Bus(Vehiculos):
    
    def set_capacidad(self,nueva_capacidad=50):
        self.capacidad = nueva_capacidad
