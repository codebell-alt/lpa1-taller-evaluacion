# Define la clase Habitacion con funcionalidades específicas.
class Habitacion:
    def __init__(self, numero, tipo, precio, disponibilidad, capacidad, servicios):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponibilidad = disponibilidad
        self.capacidad = capacidad
        self.servicios = servicios

    def reservar(self):
        pass

    def modificar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def cambiar_disponibilidad(self, estado):
        self.disponibilidad = estado

