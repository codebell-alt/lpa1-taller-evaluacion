# Este script crea instancias de las clases principales, simula una reserva y muestra la información relevante.
from models.usuario import Cliente  
from models.administrador import Administrador 
from models.hotel import Hotel
from models.habitacion import Habitacion
from models.reserva import Reserva
from models.pago import Pago
import datetime

# Crear un administrador
admin = Administrador(
    nombre="Carlos Pérez",
    email="admin@hotel.com",
    contraseña="admin123",
    telefono="123456789",
    direccion="Calle 123, Ciudad",
    fecha_nacimiento=datetime.date(1985, 6, 15)
)

# Crear un cliente
cliente = Cliente(
    nombre="Ana Gómez",
    email="ana@example.com",
    contraseña="cliente123",
    telefono="987654321",
    direccion="Avenida 456, Ciudad",
    fecha_nacimiento=datetime.date(1992, 3, 22)
)

# Crear un hotel
hotel = Hotel(
    nombre="Hotel Paraíso",
    ubicacion="Playa Bonita",
    categoria=5,
    servicios=["WiFi", "Piscina", "Spa", "Desayuno incluido"],
    reglas="No se permiten mascotas"
)

# Crear habitaciones
habitacion1 = Habitacion(numero=101, tipo="Suite", precio=150, disponibilidad=True, capacidad=2, servicios=["TV", "Aire Acondicionado"])
habitacion2 = Habitacion(numero=102, tipo="Doble", precio=100, disponibilidad=True, capacidad=2, servicios=["TV", "Balcón"])

# Crear una reserva para el cliente
reserva = Reserva(
    id_reserva=1,
    fecha_inicio=datetime.date(2025, 4, 10),
    fecha_fin=datetime.date(2025, 4, 15),
    estado="Confirmada",
    costo_total=750
)

# Crear un pago asociado a la reserva
pago = Pago(
    id_pago=1,
    monto=750,
    metodo_pago="Tarjeta de Crédito",
    estado_pago="Completado",
    fecha_pago=datetime.date(2025, 4, 5)
)

# Simulación de acciones
print(f"Cliente: {cliente._nombre} ha reservado la habitación {habitacion1.numero} en {hotel.nombre}.")
print(f"Estado de la reserva: {reserva.estado}, Total: ${reserva.costo_total}")
print(f"Pago realizado con {pago.metodo_pago}, Estado: {pago.estado_pago}")

# Modificar disponibilidad de la habitación reservada
habitacion1.cambiar_disponibilidad(False)
print(f"La habitación {habitacion1.numero} ahora está disponible: {habitacion1.disponibilidad}")


