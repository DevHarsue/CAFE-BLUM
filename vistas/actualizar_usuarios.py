from submain import MainWindow
from validaciones.validador_lines import Validador
from validaciones.hash import texto_a_hash
from conexion.tablas import TablaUsuarios

class VistaActualizarUsuarios:
    def __init__(self, ventana: MainWindow):
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_buscar_actualizar_usuario.pressed.connect(self.buscar_usuario)
        self.validador = Validador()
        self.validador.usuarios(self.ui.line_actualizar_usuario)
        self.ui.line_actualizar_usuario.textChanged.connect(self.reiniciar)
        self.ui.boton_actulizar_usuario.pressed.connect(self.actualizar)
        self.usuario = False
    
    def buscar_usuario(self):
        usuario = self.ui.line_actualizar_usuario.text()
        usuario = texto_a_hash(usuario)
        usuario = TablaUsuarios().select_usuario(usuario)
        if not bool(usuario):
            self.ventana.mostrar_mensaje("El usuario no existe","el usuario no existe")
            return 0
        
        self.usuario = usuario[0]
        
        if self.usuario[-1] == texto_a_hash("SUPERADMIN"+self.ventana.salt):
            if not self.ventana.rol == "SUPERADMIN":
                self.ventana.mostrar_mensaje("SIN permisos","No puedes editar este usuario")
                return 0
        
        self.ui.line_contrasena_usuario.setEnabled(True)
        self.ui.line_confirmar_usuario.setEnabled(True)
        self.ui.boton_actulizar_usuario.setEnabled(True)
        
    def reiniciar(self):
        self.ui.line_contrasena_usuario.setText("")
        self.ui.line_confirmar_usuario.setText("")
        self.ui.line_contrasena_usuario.setEnabled(False)
        self.ui.line_confirmar_usuario.setEnabled(False)
        self.ui.boton_actulizar_usuario.setEnabled(False)
    
    def actualizar(self):
        contraseña = self.ui.line_contrasena_usuario.text()
        if not Validador().comprobar_contraseña(contraseña):
            self.ventana.mostrar_mensaje("Contraseña Invalida","La contraseña debe contener al menos una letra mayuscula, una minuscula, 2 numeros y un caracter especial")
            return 0

        confirmacion= self.ui.line_confirmar_usuario.text()
        if contraseña!=confirmacion:
            self.ventana.mostrar_mensaje("Contraseña Invalida","La contraseñas no coinciden")
            return 0
        
        TablaUsuarios().update(str(self.usuario[0]),{"usuario_clave":texto_a_hash(contraseña)})
        self.ventana.mostrar_mensaje("Contraseña Cambiada","Contraseña Cambiada Exitosamente")
        self.reiniciar()
