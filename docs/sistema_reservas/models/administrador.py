# administrador.py - Hereda de Usuario y añade funcionalidades de gestión.
from models.usuario import Usuario

class Administrador(Usuario):
    def gestionar_hoteles(self):
        """ Administra los hoteles en el sistema """
        pass

    def modificar_disponibilidad(self):
        """ Modifica la disponibilidad de habitaciones """
        pass

    def gestionar_usuarios(self):
        """ Administra los usuarios del sistema """
        pass

    def generar_reportes(self):
        """ Genera reportes sobre las reservas y clientes """
        pass

