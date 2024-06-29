from submain import MainWindow
from utilidades import obtener_fecha
from PySide6.QtCore import QDate
from conexion.tablas import TablaTotales
from PDF.cierre import CierrePDF
import os
import webbrowser

class VistaCierre:
    def __init__(self, ventana: MainWindow):
        self.ventana = ventana
        self.ui = ventana.ui
        fecha = obtener_fecha().split("-")
        self.ui.date_cierre.setDate(QDate(int(fecha[0]),int(fecha[1]),int(fecha[2])))
        self.ui.boton_buscar_cierre.pressed.connect(self.buscar_cierre)
        self.ui.boton_cierre.pressed.connect(self.cierre)
        self.ui.date_cierre.dateChanged.connect(self.reiniciar)
        self.ui.boton_rehacer.pressed.connect(self.borrar_cierre)
        self.actualizacion = False
        
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
            if not self.actualizacion:
                self.ventana.mostrar_mensaje("Cierre Realizado","Este dia ya ha sido cerrado")
            self.ui.boton_rehacer.setEnabled(True)
            self.actualizacion=False
        
    def cierre(self):
        fecha = self.ui.date_cierre.date().toString("yyyy-MM-dd")
        tabla = TablaTotales()
        total = tabla.calcular_diario(fecha)
        bs = str(total[0][-1])
        cop = str(total[1][-1])
        dolar = str(total[2][-1])
        tabla.insert(fecha,"1",bs)
        tabla.insert(fecha,"2",cop)
        tabla.insert(fecha,"3",dolar)
        self.ventana.mostrar_mensaje("Cierre Registrado","Cierre Realizado Exitosamente")
        self.imprimir(fecha,dolar,bs,cop)
        self.reiniciar()

    def imprimir(self,fecha,dolar,bs,cop):
        pdf = CierrePDF(fecha,dolar,bs,cop)
        documentos_path = str(os.path.expanduser("~\\Documents"))
        try:
            os.makedirs(documentos_path+"\\BLUM")
        except FileExistsError:
            pass
        path = f"{documentos_path}\\BLUM\\cierre_{fecha}.pdf"
        pdf.output(path)
        webbrowser.open_new(path)
    
    def reiniciar(self):
        self.ventana.ui.label_cierre_bs.setText("0")
        self.ventana.ui.label_cierre_cop.setText("0")
        self.ventana.ui.label_cierre_dolar.setText("0")
        self.ventana.ui.boton_cierre.setEnabled(False)
        self.ventana.ui.boton_rehacer.setEnabled(False)
    
    def borrar_cierre(self):
        self.ventana.preguntar("Borrar Cierre","¿Desea rehacer el cierre?")
        if not self.ventana.respuesta:
            return 0
        
        fecha = self.ui.date_cierre.date().toString("yyyy-MM-dd")
        tabla = TablaTotales()
        total = tabla.calcular_diario(fecha)
        ids = tabla.select_fecha(fecha)
        if not bool(total):
            self.ventana.preguntar("No se han encontrado facturas","No se han encontrado facturas\n¿Desea borrar el cierre?")
            if self.ventana.respuesta:
                tabla.delete(str(ids[0][0]))
                tabla.delete(str(ids[1][0]))
                tabla.delete(str(ids[2][0]))
                self.reiniciar()
        
            return 0
        
        tabla.update(str(ids[0][0]),{"total_ingresado":str(total[0][-1])})
        tabla.update(str(ids[1][0]),{"total_ingresado":str(total[1][-1])})
        tabla.update(str(ids[2][0]),{"total_ingresado":str(total[2][-1])})
        self.ventana.mostrar_mensaje("Cierre Actualizado","Cierre Actualizado Correctamente")
        self.imprimir(fecha,str(total[2][-1]),str(total[0][-1]),str(total[1][-1]))
        self.actualizacion = True       
        self.buscar_cierre()
        