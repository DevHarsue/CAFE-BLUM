from interfaz.configuracion import Ui_Configuracion
from interfaz.register import Ui_Register
from conexion.comprobar_bd import ComprobadorBD
from interfaz.message import Ui_Message
from interfaz.question import Ui_Question
from validaciones.hash import texto_a_hash
from conexion.tablas import TablaUsuarios
from validaciones.validador_lines import Validador
from PySide6.QtWidgets import QMainWindow, QMessageBox,QDialog
from PySide6.QtCore import Signal

class VentanaConfiguracion(QMainWindow):
    def __init__(self,ventana) -> None:
        super().__init__()
        self.ventana = ventana
        self.ui = Ui_Configuracion()
        self.ui.setupUi(self)
        self.mensaje = Mensaje()
        self.ui.pushButton.pressed.connect(self.conectar)
        self.ui.pushButton_2.hide()
        self.ui.pushButton_2.pressed.connect(self.volver)
        
    def conectar(self):
        user = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        host = self.ui.lineEdit_3.text()
        puerto = self.ui.lineEdit_4.text()
        if not ComprobadorBD().testear(user,password,host,puerto):
            self.mensaje.mostrar("Error de conexion","Comprueba los datos para conectar a la base de datos.")
            return 0
        
        if not ComprobadorBD().crear_env(user,password,host,puerto):
            self.mensaje.mostrar("Error de configuración","No se pudo crear el archivo env")
            return 0
        
        self.mensaje.mostrar("Conexion establecida","Conexion a la base de datos realizada correctamente.")
        
        roles = TablaUsuarios().select_rol()
        if not tuple(filter(lambda x: x[0]==texto_a_hash("SUPERADMIN"+'\x9a\xedd\t\xb3\x80\xa7\xbc:\xd5\xbdW\xcc\x96\xc8\x94'),roles)):
            self.close()
            self.ventana_configurar_usuarios = VentanaUsuarios(self.ventana)
            self.ventana_configurar_usuarios.show()
            return 0
        
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit_4.setText("")
        
        self.close()
        self.ventana.show()
        
    def volver(self):
        self.close()
        self.ventana.show()

class VentanaUsuarios(QMainWindow):
    def __init__(self,ventana) -> None:
        self.ventana = ventana
        super().__init__()
        self.ui = Ui_Register()
        self.ui.setupUi(self)
        self.mensaje = Mensaje()
        self.pregunta = Preguntar()
        self.pregunta.respuesta.connect(self.responder)
        self.ui.pushButton.pressed.connect(self.guardar_usuarios)
        Validador().usuarios(self.ui.lineEdit)
        self.ui.pushButton_2.hide()
        self.ui.pushButton_2.pressed.connect(self.volver)
    
    def responder(self,respuesta):
        if not respuesta:
            self.respuesta=False
        else:
            self.respuesta=True
    
    def guardar_usuarios(self):
        usuario = self.ui.lineEdit.text()
        if usuario=="":
            self.mensaje.mostrar("Error de registro","El campo usuario no puede estar vacío.")
            return 0
        
        if bool(TablaUsuarios().select_usuario(texto_a_hash(usuario))):
            self.mensaje.mostrar("Error de registro","El usuario ya existe.")
            return 0
        
        contraseña = self.ui.lineEdit_2.text()
        if not Validador().comprobar_contraseña(contraseña):
            self.mensaje.mostrar("Contraseña Invalida","La contraseña debe ser de minimo 8 caracteres, contener al menos una letra mayuscula, una minuscula, 2 numeros y un caracter especial")
            return 0

        confirmacion= self.ui.lineEdit_3.text()
        if contraseña!=confirmacion:
            self.mensaje.mostrar("Contraseña Invalida","La contraseñas no coinciden")
            return 0
        
        rol = self.ui.comboBox.currentText()
        
        usuario = texto_a_hash(usuario)
        contraseña = texto_a_hash(contraseña)
        rol_hash = texto_a_hash(rol+'\x9a\xedd\t\xb3\x80\xa7\xbc:\xd5\xbdW\xcc\x96\xc8\x94')
        TablaUsuarios().insert(usuario,contraseña,rol_hash)
        self.mensaje.mostrar("Registro Exitoso",f"Usuario {rol}, registrado correctamente")
        if rol !="SUPERADMIN":
            existe_super = tuple(filter(lambda x: x[0]==texto_a_hash("SUPERADMIN"+'\x9a\xedd\t\xb3\x80\xa7\xbc:\xd5\xbdW\xcc\x96\xc8\x94'),TablaUsuarios().select_rol()))
            if not bool(existe_super):
                self.mensaje.mostrar("Falta SUPERADMIN","No hay un SUPERADMIN registrado\n Porfavor registre uno")
                self.reiniciar()
                return 0
        else:
            self.ui.comboBox.removeItem(0)
        
        self.pregunta.mostrar("Registrar mas usuarios","¿Desea Registrar mas usuarios?")
        respuesta = self.respuesta
        if respuesta:
            self.reiniciar()
            self.ui.pushButton_2.show()
            return 0
        
        self.close()
        self.ventana.show()

    def reiniciar(self):
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit_2.setText("")
        
    def volver(self):
        self.close()
        self.ventana.show()
        


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