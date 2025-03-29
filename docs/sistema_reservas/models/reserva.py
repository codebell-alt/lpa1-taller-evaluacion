# Define la clase Reserva con su lógica de negocio.
class Reserva:
    def __init__(self, id_reserva, fecha_inicio, fecha_fin, estado, costo_total):
        self.id_reserva = id_reserva
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado
        self.costo_total = costo_total

    def procesar_pago(self):
        pass

    def cancelar(self):
        pass

    def modificar(self):
        pass

