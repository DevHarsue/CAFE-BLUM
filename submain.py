from interfaz.interfaz_principal import Ui_MainWindow
from interfaz.message import Ui_Message
from interfaz.question import Ui_Question
from PySide6.QtWidgets import QMainWindow,QMessageBox,QDialog
from PySide6.QtCore import Signal

class MainWindow(QMainWindow):
    def __init__(self,login):
        super().__init__()
        self.login = login
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.asignar_botones()
        self.mensaje = Mensaje()
        self.pregunta = Preguntar()
        self.pregunta.respuesta.connect(self.responder)
        self.ui.stacked_widget.setCurrentWidget(self.ui.widget_facturar)
    
    def asignar_botones(self):
        self.ui.boton_v_facturar.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_facturar))
        self.ui.boton_v_productos.pressed.connect(self.cambiar_vista_producto)
        self.ui.boton_v_registrar_cliente.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_registrar_cliente))
        self.ui.boton_v_registrar_producto.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_registrar_producto))
        self.ui.boton_v_divisas.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.widget_divisas))
        self.ui.boton_v_editar_clientes.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.widget_editar_clientes))
        self.ui.boton_v_cierre.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.widget_cierre_diario))
        self.ui.boton_cerrar_sesion.pressed.connect(self.cerrar)
        # self.ui.boton_v_editar_clientes.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget())
    
    def cambiar_vista_producto(self):
        self.ui.stacked_widget.setCurrentWidget(self.ui.widget_productos)
        self.vista_producto.compra = False
    
    def mostrar_mensaje(self,titulo,mensaje):
        self.mensaje.mostrar(titulo,mensaje)
        
    def preguntar(self,titulo,texto):
        self.pregunta.mostrar(titulo,texto)

    def responder(self,respuesta):
        if not respuesta:
            self.respuesta=False
        else:
            self.respuesta=True
    
    def cerrar(self):
        self.close()
        self.login.show()
    

class Mensaje(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.ui = Ui_Message()
        self.ui.setupUi(self)
        self.ui.pushButton.pressed.connect(self.close)
    
    def mostrar(self,titulo,mensaje):
        self.ui.pushButton.setDefault(True)
        self.setWindowTitle(titulo)
        self.ui.label.setText(mensaje)
        self.exec_()

class Preguntar(QDialog):
    respuesta = Signal(bool)
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.ui = Ui_Question()
        self.ui.setupUi(self)
        self.ui.pushButton.pressed.connect(self.si)
        self.ui.pushButton_2.pressed.connect(self.no)
    
    def mostrar(self,titulo,mensaje):
        self.ui.pushButton.setDefault(True)
        self.setWindowTitle(titulo)
        self.ui.label.setText(mensaje)
        self.exec_()
    
    def si(self):
        self.respuesta.emit(True)
        self.close()
    
    def no(self):
        self.respuesta.emit(False)
        self.close()