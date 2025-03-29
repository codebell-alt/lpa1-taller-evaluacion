# Gestiona los pagos en el sistema.
class Pago:
    def __init__(self, id_pago, monto, metodo_pago, estado_pago, fecha_pago):
        self.id_pago = id_pago
        self.monto = monto
        self.metodo_pago = metodo_pago
        self.estado_pago = estado_pago
        self.fecha_pago = fecha_pago

    def procesar_pago(self):
        pass
