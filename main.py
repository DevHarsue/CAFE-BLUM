from PySide6.QtWidgets import QApplication,QMainWindow
from submain import MainWindow 
from vistas.registrar_clientes import VistaRegistrarClientes
from vistas.registrar_productos import VistaRegistrarProducto
from vistas.productos import VistaProductos
from vistas.actualizar_productos import VistaActualizarProducto
from vistas.divisas import VistaDivisas
from vistas.facturar import VistaFacturar
from vistas.editar_clientes import VistaEditarClientes
from vistas.configuracion import VistaConfiguracion
from vistas.editar_facturas import VistaEditarFacturas
from vistas.actualizar_usuarios import VistaActualizarUsuarios
from vistas.cierre import VistaCierre
from interfaz.login import Ui_Login
from conexion.tablas import TablaUsuarios
from validaciones.hash import texto_a_hash
from conexion.comprobar_bd import ComprobadorBD
from ventanas import VentanaConfiguracion,VentanaUsuarios,Mensaje
from validaciones.validador_lines import Validador
import sys

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.pushButton.pressed.connect(self.iniciar)
        self.ui.pushButton_2.pressed.connect(self.close)
        self.mensaje = Mensaje()
        Validador().usuarios(self.ui.lineEdit)
        self.show()
        self.salt = '\x9a\xedd\t\xb3\x80\xa7\xbc:\xd5\xbdW\xcc\x96\xc8\x94'
        
        if not ComprobadorBD().comprobar():
            self.cambiar_ventana_configuracion()
        else:
            roles = TablaUsuarios().select_rol()
            if not tuple(filter(lambda x: x[0]==texto_a_hash("SUPERADMIN"+self.salt),roles)):
                self.close()
                self.ventana_configurar_usuarios = VentanaUsuarios(self)
                self.ventana_configurar_usuarios.show()
            
        
    
    def iniciar(self):
        usuario = TablaUsuarios().select_usuario(texto_a_hash(self.ui.lineEdit.text()))
        if not bool(usuario):
            self.mensaje.mostrar("Usuario Incorrecto","Usuario no encontrado")
            return 0

        usuario = usuario[0]
        if usuario[2]==texto_a_hash(self.ui.lineEdit_2.text()):
            rol = ""
            if usuario[3] == texto_a_hash("SUPERADMIN"+self.salt):
                rol = "SUPERADMIN"
            elif usuario[3] == texto_a_hash("ADMIN"+self.salt):
                rol = "ADMIN"
            else:
                rol = "USUARIO"
            self.close()
            self.ventana = MainWindow(self,rol)
            self.vistas_ventana()
            self.ventana.show()
            self.ui.lineEdit.setText("")
            self.ui.lineEdit_2.setText("")
        else:
            self.mensaje.mostrar("Usuario Incorrecto","Contraseña Incorrecta")
    
    def vistas_ventana(self):
        self.ventana.vista_registrar_clientes = VistaRegistrarClientes(self.ventana)
        self.ventana.vista_registrar_productos = VistaRegistrarProducto(self.ventana)
        self.ventana.vista_producto = VistaProductos(self.ventana)
        self.ventana.vista_actualizar_producto = VistaActualizarProducto(self.ventana)
        self.ventana.vista_factura = VistaFacturar(self.ventana)
        self.ventana.vista_divisas = VistaDivisas(self.ventana)
        self.ventana.vista_editar_clientes = VistaEditarClientes(self.ventana)
        self.ventana.vista_cierre = VistaCierre(self.ventana)
        self.ventana.vista_configuracion = VistaConfiguracion(self.ventana)
        self.ventana.vista_actualizar_usuarios = VistaActualizarUsuarios(self.ventana)
        self.ventana.vista_editar_facturas = VistaEditarFacturas(self.ventana)

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