# Gestiona los reportes generados en el sistema.
class Reporte:
    def __init__(self, id_reporte, fecha_generacion, tipo):
        self.id_reporte = id_reporte
        self.fecha_generacion = fecha_generacion
        self.tipo = tipo

    def generar_reporte(self):
        pass

    def exportar_pdf(self):
        pass

    def exportar_excel(self):
        pass

