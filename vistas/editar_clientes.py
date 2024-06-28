from submain import MainWindow
from validaciones.validador_lines import Validador
from conexion.tablas import TablaClientes,TablaFacturas,TablaDetalles

class VistaEditarClientes:
    def __init__(self,ventana: MainWindow) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_buscar_actualizar.pressed.connect(self.buscar)
        self.ui.line_cedula_actualizar.textChanged.connect(self.reiniciar)
        self.ui.nacionalidad_actualizar.currentIndexChanged.connect(self.reiniciar)
        self.ui.boton_actualizar.pressed.connect(self.actualizar)
        self.ui.boton_borrar.pressed.connect(self.eliminar)
        self.preparar()
        self.cliente = False
        
    def preparar(self):
        Validador().cedulas(self.ui.line_cedula_actualizar)
        Validador().solo_texto(self.ui.line_apellido_actualizar)
        Validador().solo_texto(self.ui.line_nombre_actualizar)
        Validador().numero_telefono(self.ui.line_telefono_actualizar)
        
    def buscar(self):
        self.reiniciar()
        cedula = self.ui.line_cedula_actualizar.text()
        if cedula ==""or len(cedula)<7:
            self.ventana.mostrar_mensaje("Error","Ingrese una cedula valida")
            return 0
        
        nacionalidad = self.ui.nacionalidad_actualizar.currentText()
        self.cliente = TablaClientes().select_cedula(nacionalidad,cedula)
        if not bool(self.cliente):
            self.ventana.mostrar_mensaje("Error","No se encontro el cliente")
            return 0
        self.cliente = self.cliente[0]
        
        self.ui.line_nombre_actualizar.setText(self.cliente[3])
        self.ui.line_apellido_actualizar.setText(self.cliente[4])
        self.ui.line_telefono_actualizar.setText(self.cliente[5])
        self.ui.text_direccion_actualizar.setText(self.cliente[6])

    def reiniciar(self):
        self.ui.line_nombre_actualizar.setText("")
        self.ui.line_apellido_actualizar.setText("")
        self.ui.line_telefono_actualizar.setText("")
        self.ui.text_direccion_actualizar.setText("")
        self.cliente = False
    
    def actualizar(self):
        if not bool(self.cliente):
            self.ventana.mostrar_mensaje("Error","Busque un cliente")
            return 0
            
        cedula = self.ui.line_cedula_actualizar.text()
        nombre = self.ui.line_nombre_actualizar.text()
        apellido = self.ui.line_apellido_actualizar.text()
        telefono = self.ui.line_telefono_actualizar.text()
        direccion = self.ui.text_direccion_actualizar.toPlainText()
        nacionalidad = self.ui.nacionalidad_actualizar.currentText()
        if cedula ==""or len(cedula)<7:
            self.ventana.mostrar_mensaje("Error","Ingrese una cedula valida")
            return 0
        if nombre =="":
            self.ventana.mostrar_mensaje("Error","Ingrese un nombre")
            return 0
        if apellido =="":
            self.ventana.mostrar_mensaje("Error","Ingrese un apellido")
            return 0
        if telefono=="" or len(telefono)<10:
            self.ventana.mostrar_mensaje("Error","Ingrese un telefono valido, debe ser minimo de 10 caracteres")
            return 0
        
        TablaClientes().update(str(self.cliente[0]),{"cliente_nombre":nombre,"cliente_apellido":apellido,"cliente_numero":telefono,"cliente_direccion":direccion})
        self.ventana.mostrar_mensaje("Actualizacion Completada","Cliente Actualizado Exitosamente")
        self.reiniciar()
    
    def eliminar(self):
        if not bool(self.cliente):
            self.ventana.mostrar_mensaje("Error","Busque un cliente")
            return 0
        self.ventana.preguntar("Eliminar Cliente","Se borraran todos los datos asociados a este cliente\n¿Estas seguro de eliminar el cliente?")
        if not self.ventana.respuesta:
            return 0
        
        facturas = TablaFacturas().select_cliente(str(self.cliente[0]))
        if bool(facturas):
            tabla = TablaDetalles()
            for x in facturas:
                tabla.delete_factura(str(x[0]))
            
            
        TablaFacturas().delete_cliente(str(self.cliente[0]))
        TablaClientes().delete(str(self.cliente[0]))
        self.ventana.mostrar_mensaje("Eliminacion Completada","Cliente Eliminado Exitosamente")
        self.reiniciar()