from PySide6.QtWidgets import QApplication,QMainWindow
from submain import MainWindow 
from vistas.registrar_clientes import VistaRegistrarClientes
from vistas.registrar_productos import VistaRegistrarProducto
from vistas.productos import VistaProductos
from vistas.actualizar_productos import VistaActualizarProducto
from vistas.divisas import VistaDivisas
from vistas.facturar import VistaFacturar
from vistas.editar_clientes import VistaEditarClientes
from vistas.cierre import VistaCierre
from interfaz.login import Ui_Login
from conexion.tablas import TablaUsuarios
from validaciones.hash import texto_a_hash
from conexion.comprobar_bd import ComprobadorBD
from ventanas import VentanaConfiguracion,VentanaUsuarios
import sys

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton.pressed.connect(self.iniciar)
        self.ui.pushButton_2.pressed.connect(self.close)
        self.show()
        if not ComprobadorBD().comprobar():
            self.cambiar_ventana_configuracion()
        else:
            roles = TablaUsuarios().select_rol()
            if not tuple(filter(lambda x: x[0]==texto_a_hash("SUPERADMIN"+'\x9a\xedd\t\xb3\x80\xa7\xbc:\xd5\xbdW\xcc\x96\xc8\x94'),roles)):
                self.close()
                self.ventana_configurar_usuarios = VentanaUsuarios(self)
                self.ventana_configurar_usuarios.show()
        self.ventana = MainWindow(self)
        self.vistas_ventana()
        
    
    def iniciar(self):
        usuario = TablaUsuarios().select_usuario(texto_a_hash(self.ui.lineEdit.text()))
        if not bool(usuario):
            self.ventana.mostrar_mensaje("Usuario Incorrecto","Usuario no encontrado")
            return 0

        usuario = usuario[0]
        if usuario[2]==texto_a_hash(self.ui.lineEdit_2.text()):
            self.close()
            self.ventana.show()
        else:
            self.ventana.mostrar_mensaje("Usuario Incorrecto","Contraseña Incorrecta")
    
    def vistas_ventana(self):
        self.ventana.vista_registrar_clientes = VistaRegistrarClientes(self.ventana)
        self.ventana.vista_registrar_productos = VistaRegistrarProducto(self.ventana)
        self.ventana.vista_producto = VistaProductos(self.ventana)
        self.ventana.vista_actualizar_producto = VistaActualizarProducto(self.ventana)
        self.ventana.vista_factura = VistaFacturar(self.ventana)
        self.ventana.vista_divisas = VistaDivisas(self.ventana)
        self.ventana.vista_editar_clientes = VistaEditarClientes(self.ventana)
        self.ventana.vista_cierre = VistaCierre(self.ventana)

    def cambiar_ventana(self,rol,id):
        self.close()
        self.venta_principal = MainWindow(rol,self,id)
        self.venta_principal.show()

    def cambiar_ventana_configuracion(self):
        self.close()
        self.ventana_configuracion = VentanaConfiguracion(self)
        self.ventana_configuracion.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    sys.exit(app.exec())