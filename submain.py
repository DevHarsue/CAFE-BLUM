from interfaz.interfaz_principal import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from ventanas import Mensaje,Preguntar

class MainWindow(QMainWindow):
    def __init__(self,login,rol):
        super().__init__()
        self.login = login
        self.rol = rol
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.asignar_botones()
        self.mensaje = Mensaje()
        self.pregunta = Preguntar()
        self.pregunta.respuesta.connect(self.responder)
        self.ui.stacked_widget.setCurrentWidget(self.ui.widget_facturar)
        self.salt = '\x9a\xedd\t\xb3\x80\xa7\xbc:\xd5\xbdW\xcc\x96\xc8\x94'
        self.ajustar()
    
    def asignar_botones(self):
        self.ui.boton_v_facturar.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_facturar))
        self.ui.boton_v_productos.pressed.connect(self.cambiar_vista_producto)
        self.ui.boton_v_registrar_cliente.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_registrar_cliente))
        self.ui.boton_v_registrar_producto.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_registrar_producto))
        self.ui.boton_v_divisas.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.widget_divisas))
        self.ui.boton_v_editar_clientes.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.widget_editar_clientes))
        self.ui.boton_v_cierre.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.widget_cierre_diario))
        self.ui.boton_cerrar_sesion.pressed.connect(self.cerrar)
        self.ui.boton_v_editar_facturas.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_editar_facturas))
        self.ui.boton_v_configuracion.pressed.connect(lambda:self.ui.stacked_widget.setCurrentWidget(self.ui.widget_configuracion))
    
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
    
    def ajustar(self):
        if self.rol=="USUARIO":
            self.ui.boton_v_registrar_producto.hide()
            self.ui.boton_v_editar_clientes.hide()
            self.ui.boton_v_editar_facturas.hide()
            self.ui.boton_v_configuracion.hide()
            self.ui.boton_rehacer.hide()
        elif self.rol=="ADMIN":
            self.ui.boton_configurar_bd.hide()
        
        self.ui.boton_v_editar_facturas.hide()
