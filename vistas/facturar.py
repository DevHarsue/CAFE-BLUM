from validaciones.validador_lines import Validador
from conexion.tablas import TablaClientes,TablaDivisas,TablaFacturas,TablaDetalles
from PySide6.QtWidgets import QTableWidgetItem
from submain import MainWindow
from utilidades import obtener_fecha
from PDF.factura import FacturaPDF
import os
import webbrowser

class VistaFacturar:
    def __init__(self,ventana: MainWindow) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_buscar_cliente_facturar.pressed.connect(self.buscar_cliente)
        self.ui.boton_facturar.pressed.connect(self.facturar)
        self.ui.line_cedula_facturar.textChanged.connect(self.reiniciar_cliente)
        self.ui.combo_nacionalidad_facturar.currentIndexChanged.connect(self.reiniciar_cliente)
        self.ui.boton_buscar_producto_facturar.pressed.connect(self.seleccionar_producto)
        Validador().cedulas(self.ui.line_cedula_facturar)
        self.total = 0
        self.ui.label_bs.mousePressEvent = self.cargar_bs
        self.ui.label_dolar.mousePressEvent = self.cargar_dolar
        self.ui.label_cop.mousePressEvent = self.cargar_cop
        self.ui.double_bs_facturar.valueChanged.connect(self.calcular_bs)
        self.ui.double_dolares_facturar.valueChanged.connect(self.calcular_dolar)
        self.ui.spin_cop_facturar.valueChanged.connect(self.calcular_cop)
        self.tasa_bolivares = float(TablaDivisas().select(str(1))[0][-1])
        self.tasa_cop = float(TablaDivisas().select(str(2))[0][-1])
        self.ui.boton_facturar.setDisabled(True)
        self.ui.table_productos_facturar.itemActivated.connect(self.borrar_producto)
        self.ui.table_productos_facturar.itemPressed.connect(self.borrar_producto)
        
    
    def buscar_cliente(self):
        cedula = self.ui.line_cedula_facturar.text()
        if cedula == "" or (len(cedula)<7):
            self.ventana.mostrar_mensaje("Cedula invalidad","Porfavor ingresa un numero de cedula valido")
            return 0
        
        nacionalidad = self.ui.combo_nacionalidad_facturar.currentText()
        self.cliente = TablaClientes().select_cedula(nacionalidad,cedula)
        
        if bool(self.cliente):
            self.cliente = self.cliente[0]
            self.ui.line_nombre_facturar.setText(self.cliente[3])
            self.ui.line_apellido_facturar.setText(self.cliente[4])
        else:
            self.cliente = False
            self.ventana.preguntar("Cliente No encontrado","¿Desea registrar cliente?")
            respuesta = self.ventana.respuesta
            if respuesta == True:
                self.ui.stacked_widget.setCurrentWidget(self.ui.widget_registrar_cliente)
                self.ui.line_cedula.setText(cedula)
                self.ui.nacionalidad.setCurrentIndex(self.ui.combo_nacionalidad_facturar.currentIndex())
                
            return 0 
        
    def reiniciar_cliente(self):
        self.ui.line_nombre_facturar.setText("")
        self.ui.line_apellido_facturar.setText("")
    
    def seleccionar_producto(self):
        self.ventana.vista_producto.compra = True
        self.ui.stacked_widget.setCurrentWidget(self.ui.widget_productos)
        
        
    def facturar(self):
        if self.ui.line_nombre_facturar.text()=="":
            self.ventana.mostrar_mensaje("Cliente no seleccionado","Porfavor busque un cliente")
            return 0
        productos = []
        imprimir = []
        for x in range(self.ui.table_productos_facturar.rowCount()):
            id = self.ui.table_productos_facturar.item(x,0).text()
            nombre = self.ui.table_productos_facturar.item(x,1).text()
            precio = self.ui.table_productos_facturar.item(x,2).text()
            cantidad = self.ui.table_productos_facturar.item(x,3).text()
            subtotal = self.ui.table_productos_facturar.item(x,4).text()
            productos.append((id,cantidad))
            imprimir.append({'numero': id, 'articulo': nombre,'qty': cantidad, 'precio': precio,"subtotal":subtotal},)
            
        tabla = TablaFacturas()
        tabla.insert(str(self.cliente[0]),obtener_fecha())
        venta = tabla.select_ultima_factura()[0]
        
        tabla = TablaDetalles()
        tabla.insert(str(venta[0]),"1",str(self.ui.double_bs_facturar.value()))
        tabla.insert(str(venta[0]),"2",str(self.ui.spin_cop_facturar.value()))
        tabla.insert(str(venta[0]),"3",str(self.ui.double_dolares_facturar.value()))
        
        self.ventana.mostrar_mensaje("Factura exitosa","Facturacion realizada exitosamente")
        pdf = FacturaPDF(venta[0],obtener_fecha(),f"{self.cliente[3]} {self.cliente[4]}",self.cliente[5],self.cliente[6],imprimir,self.total,self.total_sin_iva,self.ui.double_dolares_facturar.value(),self.ui.double_bs_facturar.value(),self.ui.spin_cop_facturar.value())
        documentos_path = str(os.path.expanduser("~\\Documents"))
        try:
            os.makedirs(documentos_path+"\\BLUM")
        except FileExistsError:
            pass
        path = f"{documentos_path}\\BLUM\\factura_{venta[0]}_{self.cliente[3]}.pdf"
        pdf.output(path)
        webbrowser.open_new(path)
        
        self.reiniciar_cliente()
        self.reiniciar_productos()
    
    def meter_producto(self):
        datos = self.ventana.vista_producto.datos
        datos.pop(2)
        datos.pop(-1)
        datos.append(self.ventana.vista_producto.cantidad)
        datos.append(float(datos[-1])*float(datos[-2]))
        
        for x in range(self.ui.table_productos_facturar.rowCount()):
            if self.ui.table_productos_facturar.item(x,0).text() == datos[0]:
                cantidad = int(self.ui.table_productos_facturar.item(x,3).text())+self.ventana.vista_producto.cantidad
                self.ui.table_productos_facturar.setItem(x,3,QTableWidgetItem(str(cantidad)))
                self.ui.table_productos_facturar.setItem(x,4,QTableWidgetItem(str(cantidad*float(datos[-3]))))
                self.calcular()
                return 0
        
        self.ui.table_productos_facturar.insertRow(self.ui.table_productos_facturar.rowCount())
        row = self.ui.table_productos_facturar.rowCount()-1
        for i,x in enumerate(datos):
            self.ui.table_productos_facturar.setItem(row,i,QTableWidgetItem(str(x)))
        
        self.calcular()
        self.calcular_bs()
        self.calcular_cop()
        self.calcular_dolar()
        
    def calcular(self):
        row = self.ui.table_productos_facturar.rowCount()
        self.total = 0
        for x in range(row):
            self.total +=float(self.ui.table_productos_facturar.item(x,4).text())
        
        self.total_sin_iva=self.total
        self.ui.label_total.setText("TOTAL EN DOLARES: "+str(self.total))
        self.total = round(self.total+(self.total*0.16),2)
        self.ui.label_total_iva.setText("TOTAL + IVA: "+str(self.total))
        self.ui.label_dolar.setText(str(self.total))
        self.ui.label_bs.setText(str(self.total*self.tasa_bolivares))
        self.ui.label_cop.setText(str(int(self.total*self.tasa_cop)))
        
    
    def cargar_bs(self,e):
        self.ui.double_bs_facturar.setValue(self.total*self.tasa_bolivares)
    def cargar_dolar(self,e):
        self.ui.double_dolares_facturar.setValue(self.total)
    def cargar_cop(self,e):
        self.ui.spin_cop_facturar.setValue(self.total*self.tasa_cop)
    
    def calcular_dolar(self):
        ingresado_bs = self.ui.double_bs_facturar.value()
        ingresado_cop = self.ui.spin_cop_facturar.value()
        dolar = self.total-round((ingresado_bs/self.tasa_bolivares)+ingresado_cop/self.tasa_cop,2)
        ingresado_dolar = self.ui.double_dolares_facturar.value()
        if ingresado_dolar > dolar:
            self.ui.double_dolares_facturar.setValue(dolar)
            ingresado_dolar = dolar
        restante_dolar =round(dolar-ingresado_dolar,2)
        self.ui.label_dolar.setText(str(round(restante_dolar,2)))
        self.ui.label_bs.setText(str(round(restante_dolar*self.tasa_bolivares,2)))
        self.ui.label_cop.setText(str(round(restante_dolar*self.tasa_cop,-2)))
        self.comprobar_factura()
        
        
    def calcular_bs(self):
        ingresado_dolar = self.ui.double_dolares_facturar.value()
        ingresado_cop = self.ui.spin_cop_facturar.value()
        bs = (self.total-round((ingresado_dolar+ingresado_cop/self.tasa_cop),2))*self.tasa_bolivares
        ingresado_bs = self.ui.double_bs_facturar.value()
        if ingresado_bs > bs:
            self.ui.double_bs_facturar.setValue(bs)
            ingresado_bs = bs
            
        restante_bs = bs-ingresado_bs
        self.ui.label_bs.setText(str(round(restante_bs,2)))
        self.ui.label_dolar.setText(str(round(restante_bs/self.tasa_bolivares,2)))
        self.ui.label_cop.setText(str(round((restante_bs/self.tasa_bolivares)*self.tasa_cop,-2)))
        self.comprobar_factura()

    def calcular_cop(self):
        ingresado_bs = self.ui.double_bs_facturar.value()
        ingresado_dolar = self.ui.double_dolares_facturar.value()
        cop = round((self.total-round((ingresado_dolar+ingresado_bs/self.tasa_bolivares),2))*self.tasa_cop,-2)
        protuberancia = int(str(int(cop))[-2:])
        if protuberancia >0:
            cop = cop-protuberancia
        ingresado_cop = self.ui.spin_cop_facturar.value()
        if ingresado_cop > cop:
            self.ui.spin_cop_facturar.setValue(cop)
            ingresado_cop = cop
            
        restante_cop = cop-ingresado_cop
        self.ui.label_cop.setText(str(round(restante_cop,2)))
        self.ui.label_dolar.setText(str(round(restante_cop/self.tasa_cop,2)))
        self.ui.label_bs.setText(str(round((restante_cop/self.tasa_cop)*self.tasa_bolivares,2)))
        self.comprobar_factura()
        self.calcular_dolar()
    
    def comprobar_factura(self):
        dolar = float(self.ui.label_dolar.text())
        bs = float(self.ui.label_bs.text())
        cop = float(self.ui.label_cop.text())

        if dolar==0 and bs==0 and cop==0 and self.ui.table_productos_facturar.rowCount()>0:
            self.ui.boton_facturar.setEnabled(True)
        else:
            self.ui.boton_facturar.setDisabled(True)
            
    def reiniciar_productos(self):
        while self.ui.table_productos_facturar.rowCount() > 0:
            self.ui.table_productos_facturar.removeRow(0)
        self.calcular()
        self.calcular_bs()
        self.calcular_cop()
        self.calcular_dolar()
    
    def borrar_producto(self):
        row = self.ui.table_productos_facturar.currentRow()
        self.ventana.preguntar("Quitar Producto","¿Quitar Producto de la Venta?")
        respuesta = self.ventana.respuesta
        if not respuesta:
            return 0
        self.ui.table_productos_facturar.removeRow(row)
        self.comprobar_factura
        self.calcular()
        self.calcular_bs()
        self.calcular_cop()
        self.calcular_dolar()