# Maneja las notificaciones a los clientes y administradores.
class Notificacion:
    def __init__(self, id_notificacion, tipo, mensaje, fecha_envio):
        self.id_notificacion = id_notificacion
        self.tipo = tipo
        self.mensaje = mensaje
        self.fecha_envio = fecha_envio

    def enviar_email(self):
        pass

    def enviar_sms(self):
        pass

