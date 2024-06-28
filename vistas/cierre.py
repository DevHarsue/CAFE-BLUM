from submain import MainWindow
from utilidades import obtener_fecha
from PySide6.QtCore import QDate
from conexion.tablas import TablaTotales

class VistaCierre:
    def __init__(self, ventana: MainWindow):
        self.ventana = ventana
        self.ui = ventana.ui
        fecha = obtener_fecha().split("-")
        self.ui.date_cierre.setDate(QDate(int(fecha[0]),int(fecha[1]),int(fecha[2])))
        self.ui.boton_buscar_cierre.pressed.connect(self.buscar_cierre)
        self.ui.boton_cierre.pressed.connect(self.cierre)
        self.ui.date_cierre.dateChanged.connect(self.reiniciar)
    
    def buscar_cierre(self):
        fecha = self.ui.date_cierre.date().toString("yyyy-MM-dd")
        tabla = TablaTotales()
        total = tabla.select_fecha(fecha)
        if not bool(total):
            total = tabla.calcular_diario(fecha)
            if not bool(total):
                self.ventana.mostrar_mensaje("Cierre no disponible","No hay ventas este dia")
                return 0
            self.ui.label_cierre_bs.setText(str(round(total[0][1],2)))
            self.ui.label_cierre_cop.setText(str(int(total[1][1])))
            self.ui.label_cierre_dolar.setText(str(round(total[2][1],2)))
            self.ui.boton_cierre.setEnabled(True)
        else:
            self.ui.label_cierre_bs.setText(str(round(total[0][3],2)))
            self.ui.label_cierre_cop.setText(str(int(total[1][3])))
            self.ui.label_cierre_dolar.setText(str(round(total[2][3],2)))
            self.ventana.mostrar_mensaje("Cierre Realizado","Este dia ya ha sido cerrado")
        
    def cierre(self):
        fecha = self.ui.date_cierre.date().toString("yyyy-MM-dd")
        bs = self.ui.label_cierre_bs.text()
        dolar = self.ui.label_cierre_dolar.text()
        cop = self.ui.label_cierre_cop.text()
        tabla = TablaTotales()
        tabla.insert(fecha,"1",bs)
        tabla.insert(fecha,"2",cop)
        tabla.insert(fecha,"3",dolar)
        self.ventana.mostrar_mensaje("Cierre Registrado","Cierre Realizado Exitosamente")
        self.reiniciar()

    
    def reiniciar(self):
        self.ventana.ui.label_cierre_bs.setText("0")
        self.ventana.ui.label_cierre_cop.setText("0")
        self.ventana.ui.label_cierre_dolar.setText("0")
        self.ventana.ui.boton_cierre.setEnabled(False)
        