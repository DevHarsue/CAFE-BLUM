from conexion.tablas import TablaProductos
from interfaz.seleccionar_numero import Ui_Cantidad
from PySide6.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QLabel,QTableWidgetItem,QDialog
from PySide6.QtGui import QPixmap,QCursor
from PySide6.QtCore import Qt
from submain import MainWindow
from validaciones.validador_lines import Validador

class VistaProductos:
    def __init__(self,ventana: MainWindow):
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.line_nombre_bproducto.textChanged.connect(self.agregar_productos)
        self.ui.combo_bproducto.currentIndexChanged.connect(self.agregar_productos)
        self.ui.table_productos.itemPressed.connect(self.item_clickeado)
        Validador().solo_texto_productos(self.ui.line_nombre_bproducto)
        self.agregar_productos()
        self.compra = False
    
    def agregar_productos(self):
        while self.ui.table_productos.rowCount()>0:
            self.ui.table_productos.removeRow(0)
        nombre = self.ui.line_nombre_bproducto.text()
        categoria = self.ui.combo_bproducto.currentText()
        productos = TablaProductos().select_nombre(nombre) if categoria == "TODO" else TablaProductos().select_nombre_categoria(nombre,categoria)
        if not bool(productos):
            return 0
        for producto in productos:
            self.ui.table_productos.insertRow(self.ui.table_productos.rowCount())
            row = self.ui.table_productos.rowCount()-1
            self.ui.table_productos.setItem(row,0,QTableWidgetItem(str(producto[0])))
            self.ui.table_productos.setItem(row,1,QTableWidgetItem(str(producto[1])))
            self.ui.table_productos.setItem(row,2,QTableWidgetItem(str(producto[2])))
            self.ui.table_productos.setItem(row,3,QTableWidgetItem(str(producto[3])))
            self.ui.table_productos.setItem(row,4,QTableWidgetItem(str(producto[4])))
    
    def item_clickeado(self):
        row = self.ui.table_productos.currentRow()
        self.datos = []
        for x in range(5):
            self.datos.append(self.ui.table_productos.item(row,x).text())
            
        if self.compra:
            self.dialogo = NumberInputDialog(self)
            self.dialogo.show()
            return 0
        if self.ventana.rol =="USUARIO":
            return 0
        self.ventana.preguntar("EDITAR PRODUCTO","¿Desea editar productos?")
        if not self.ventana.respuesta:
            return 0
        self.ui.stacked_widget.setCurrentWidget(self.ui.widget_actualizar_productos)
        self.ventana.vista_actualizar_producto.cargar(self.datos)
        

class NumberInputDialog(QDialog):
    def __init__(self,ventana):
        super().__init__()
        self.setModal(True)
        self.ventana = ventana
        self.ui = Ui_Cantidad()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.dar_cantidad)
        self.ui.buttonBox.rejected.connect(self.close)
    
    def dar_cantidad(self):
        self.ventana.cantidad = self.ui.spinBox.value()
        if self.ui.spinBox.value()<=0:
            self.no_producto()
            return 0
        self.ventana.ui.stacked_widget.setCurrentWidget(self.ventana.ui.widget_facturar)
        self.ventana.ventana.vista_factura.meter_producto()
        self.close()
        self.ventana.compra = False
        
    def no_producto(self):
        self.ventana.ventana.mostrar_mensaje("Cantidad Invalida","La cantidad tiene que ser mayor a 0")
        self.close()

