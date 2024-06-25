from conexion.tablas import TablaProductos
from PySide6.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QLabel,QTableWidgetItem
from PySide6.QtGui import QPixmap,QCursor
from PySide6.QtCore import Qt

class VistaProductos:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ui = ventana.ui
        self.categorias = {"CAFE":["images/coffee.png",self.ui.tableWidget],
                           "TE": ["images/te.png",self.ui.layout_te],
                           "CERVEZA":["images/cerveza.png",self.ui.layout_cerveza],
                           "COMIDA":["images/sandwich.png",self.ui.layout_comida],
                           "PASTELERIA":["images/pastel.png",self.ui.layout_pasteleria],
                           "CHOCOLATE":["images/chocolate.png",self.ui.layout_chocolate],
                           "MALTEADAS":["images/batido.png",self.ui.layout_malteada],
                           }
        self.agregar_productos()
    
    def agregar_productos(self):
        productos = TablaProductos().select()
        if not bool(productos):
            return 0
        for producto in productos:
            categoria = producto[-1]
            self.crear_widget(producto[1],producto[-2],self.categorias[categoria][0],self.categorias[categoria][1])

    
    def crear_widget(self,nombre,precio,image,layout):
        if image != "images/coffee.png":
            return 0
        
        layout.setItem(0,layout.columnCount(),item(image,nombre,precio))
        

    def click(self,event):
        if event.button()==Qt.RightButton:
            print("Derecho")
            

def item(image,nombre,precio):
    widget = QWidget()
    layout_widget = QVBoxLayout()
    label = QLabel()
    label.setAlignment(Qt.AlignCenter)
    pixmap = QPixmap(image)
    label.setPixmap(pixmap)
    label.setMaximumWidth(80)
    label.setMaximumHeight(80)
    label.setScaledContents(True)
    layout_widget.addWidget(label)
    label = QLabel(nombre)
    label.setAlignment(Qt.AlignCenter)
    layout_widget.addWidget(label)
    label = QLabel(str(precio))
    label.setAlignment(Qt.AlignCenter)
    
    layout_widget.addWidget(label)
    widget.setLayout(layout_widget)
        
        
    widget.setCursor(QCursor(Qt.PointingHandCursor))
    return widget