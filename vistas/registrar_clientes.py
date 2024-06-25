from validaciones.validador_lines import Validador
from conexion.tablas import TablaClientes

class VistaRegistrarClientes:
    def __init__(self,ventana) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_registrar.pressed.connect(self.registrar_clientes)
        self.preparar()
        
    def preparar(self):
        validador = Validador()
        validador.cedulas(self.ui.line_cedula)
        validador.solo_texto(self.ui.line_nombre)
        validador.solo_texto(self.ui.line_apellido)
        validador.numero_telefono(self.ui.line_telefono)
        
    def registrar_clientes(self):
        nacionalidad = self.ui.nacionalidad.currentText()
        cedula = self.ui.line_cedula.text()
        nombre = self.ui.line_nombre.text()
        apellido = self.ui.line_apellido.text()
        numero = self.ui.line_telefono.text()
        descripcion = self.ui.text_direccion.toPlainText()
        
        if cedula=="" or len(cedula)<7:
            self.ventana.mostrar_mensaje("Cedula Invalida","Introduzca una cedula valida")
            return 0
        if nombre=="":
            self.ventana.mostrar_mensaje("Nombre Invalido","Nombre invalido")
            return 0
        if apellido=="":
            self.ventana.mostrar_mensaje("Apellido Invalido","Apellido invalido")
            return 0
        if numero=="" or len(numero)<10:
            self.ventana.mostrar_mensaje("Numero de Telefono Invalido","El numero de telefono debe ser minimo de 10 digitos")
            return 0
        tabla = TablaClientes()
        if bool(tabla.select_cedula(nacionalidad,cedula)):
            self.ventana.mostrar_mensaje("Cedula ya existe","El cliente ya ha sido registrado")
            return 0

        tabla.insert(nacionalidad,cedula,nombre,apellido,numero,descripcion)
        self.ventana.mostrar_mensaje("Registro Exitoso","Cliente Registrado Exitosamente")
        self.reiniciar()
        self.ui.stacked_widget.setCurrentWidget(self.ui.widget_facturar)
    
    def reiniciar(self):
        self.ui.nacionalidad.setCurrentIndex(0)
        self.ui.line_cedula.setText("")
        self.ui.line_nombre.setText("")
        self.ui.line_apellido.setText("")
        self.ui.line_telefono.setText("")
        self.ui.text_direccion.setText("")
        
        