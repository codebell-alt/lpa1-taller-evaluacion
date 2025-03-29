import datetime

# Define la clase base Usuario con atributos y métodos comunes.
class Usuario:
    def __init__(self, nombre, email, contraseña, telefono, direccion, fecha_nacimiento):
        """Constructor de la clase Usuario."""
        self._nombre = nombre
        self._email = email
        self._contraseña = contraseña
        self._telefono = telefono
        self._direccion = direccion
        self._fecha_nacimiento = fecha_nacimiento

    def registrar(self):
        """Método para registrar un usuario."""
        pass

    def iniciar_sesion(self):
        """Método para iniciar sesión."""
        pass

    def cerrar_sesion(self):
        """Método para cerrar sesión."""
        pass

    def recuperar_contraseña(self):
        """Método para recuperar contraseña."""
        pass

# Hereda de Usuario y define funcionalidades específicas para clientes.
class Cliente(Usuario):
    def __init__(self, nombre, email, contraseña, telefono, direccion, fecha_nacimiento):
        """Constructor de Cliente que llama al constructor de Usuario."""
        super().__init__(nombre, email, contraseña, telefono, direccion, fecha_nacimiento)

    def reservar_habitacion(self):
        """Permite a un cliente reservar una habitación."""
        pass

    def cancelar_reserva(self):
        """Permite a un cliente cancelar su reserva."""
        pass

    def modificar_reserva(self):
        """Permite modificar una reserva existente."""
        pass

    def ver_historial_reservas(self):
        """Muestra el historial de reservas del cliente."""
        pass

    def realizar_pago(self):
        """Permite al cliente realizar un pago."""
        pass
