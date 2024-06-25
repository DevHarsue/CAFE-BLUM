from interfaz.interfaz_principal import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox
from vistas.registrar_clientes import VistaRegistrarClientes
from vistas.registrar_productos import VistaRegistrarProducto
from vistas.productos import VistaProductos
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.vista_registrar_clientes = VistaRegistrarClientes(self)
        self.vista_registrar_productos = VistaRegistrarProducto(self)
        self.vista_producto = VistaProductos(self)
        self.asignar_botones()
        self.show()
    
    def asignar_botones(self):
        self.ui.boton_v_facturar.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_facturar))
        self.ui.boton_v_productos.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_productos))
        self.ui.boton_v_registrar_cliente.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_registrar_cliente))
        self.ui.boton_v_registrar_producto.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_registrar_producto))
        # self.ui.boton_v_editar_clientes.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget())
    
    
    def mostrar_mensaje(self,titulo,mensaje):
        QMessageBox.information(self,titulo,mensaje,QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())