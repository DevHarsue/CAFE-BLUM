from interfaz.configuracion import Ui_Configuracion
from interfaz.register import Ui_Register
from conexion.comprobar_bd import ComprobadorBD
from validaciones.hash import texto_a_hash
from conexion.tablas import TablaUsuarios
from validaciones.validador_lines import Validador
from PySide6.QtWidgets import QMainWindow, QMessageBox

class VentanaConfiguracion(QMainWindow):
    def __init__(self,ventana) -> None:
        super().__init__()
        self.ventana = ventana
        self.ui = Ui_Configuracion()
        self.ui.setupUi(self)
        self.ui.pushButton.pressed.connect(self.conectar)
        self.ui.pushButton_2.pressed.connect(self.volver)
        
    def conectar(self):
        user = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        host = self.ui.lineEdit_3.text()
        puerto = self.ui.lineEdit_4.text()
        if not ComprobadorBD().testear(user,password,host,puerto):
            QMessageBox.information(self,"Error de conexion","Comprueba los datos para conectar a la base de datos.",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            return 0
        
        if not ComprobadorBD().crear_env(user,password,host,puerto):
            QMessageBox.information(self,"Error de configuración","No se pudo crear el archivo env",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            return 0
        
        QMessageBox.information(self,"Conexion establecida","Conexion a la base de datos realizada correctamente.",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
        
        roles = TablaUsuarios().select_rol()
        if not tuple(filter(lambda x: x[0]==texto_a_hash("SUPERADMIN"+'\x9a\xedd\t\xb3\x80\xa7\xbc:\xd5\xbdW\xcc\x96\xc8\x94'),roles)):
            self.close()
            self.ventana_configurar_usuarios = VentanaUsuarios(self.ventana)
            self.ventana_configurar_usuarios.show()
            return 0
        
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
        self.ui.pushButton.pressed.connect(self.guardar_usuarios)
        Validador().usuarios(self.ui.lineEdit)
        self.ui.pushButton_2.pressed.connect(self.volver)
    
    def guardar_usuarios(self):
        usuario = self.ui.lineEdit.text()
        if usuario=="":
            QMessageBox.information(self,"Error de registro","El campo usuario no puede estar vacío.",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            return 0
        
        if bool(TablaUsuarios().select_usuario(texto_a_hash(usuario))):
            QMessageBox.information(self,"Error de registro","El usuario ya existe.",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            return 0
        
        contraseña = self.ui.lineEdit_2.text()
        if not Validador().comprobar_contraseña(contraseña):
            QMessageBox.information(self,"Contraseña Invalida","La contraseña debe contener al menos una letra mayuscula, una minuscula, 2 numeros y un caracter especial",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            return 0

        confirmacion= self.ui.lineEdit_3.text()
        if contraseña!=confirmacion:
            QMessageBox.information(self,"Contraseña Invalida","La contraseñas no coinciden",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
            return 0
        
        rol = self.ui.comboBox.currentText()
        
        usuario = texto_a_hash(usuario)
        contraseña = texto_a_hash(contraseña)
        rol_hash = texto_a_hash(rol+'\x9a\xedd\t\xb3\x80\xa7\xbc:\xd5\xbdW\xcc\x96\xc8\x94')
        TablaUsuarios().insert(usuario,contraseña,rol_hash)
        QMessageBox.information(self,"Registro Exitoso",f"Usuario {rol}, registrado correctamente")
        if rol !="SUPERADMIN":
            existe_super = tuple(filter(lambda x: x[0]==texto_a_hash("SUPERADMIN"+'\x9a\xedd\t\xb3\x80\xa7\xbc:\xd5\xbdW\xcc\x96\xc8\x94'),TablaUsuarios().select_rol()))
            if not bool(existe_super):
                QMessageBox.information(self,"Falta SUPERADMIN","No hay un SUPERADMIN registrado\n Porfavor registre uno",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
                self.reiniciar()
                return 0
        else:
            self.ui.comboBox.removeItem(0)
        
        respuesta = QMessageBox.question(self,"Registrar mas usuarios","¿Desea Registrar mas usuarios?")
        if respuesta == QMessageBox.StandardButton.Yes:
            self.reiniciar()
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