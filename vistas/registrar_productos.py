from validaciones.validador_lines import Validador
from conexion.tablas import TablaProductos

class VistaRegistrarProducto:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_registrar_producto.pressed.connect(self.registrar_producto)
        self.preparar()
    
    def preparar(self):
        Validador().solo_texto(self.ui.line_nombre_producto)
    
    def registrar_producto(self):
        nombre = self.ui.line_nombre_producto.text()
        descripcion = self.ui.text_descripcion.toPlainText()
        valor = self.ui.double_precio.value()
        categoria = self.ui.combo_categoria.currentText()
        
        if nombre=="":
            self.ventana.mostrar_mensaje("Nombre Invalido","El Nombre es Invalido")
            return 0
        if valor <= 0:
            self.ventana.mostrar_mensaje("Precio Invalido","El Precio debe ser mayor a 0")
            return 0

        TablaProductos().insert(nombre,descripcion,str(valor),categoria)
        self.ventana.mostrar_mensaje("Registro Exitoso","Producto registrado correctamente")
        self.reiniciar()
        self.ui.stacked_widget.setCurrentWidget(self.ui.widget_facturar)
        self.ventana.vista_producto.crear_widget(nombre,str(valor),self.ventana.vista_producto.categorias[categoria][0],self.ventana.vista_producto.categorias[categoria][1])

    
    def reiniciar(self):
        self.ui.line_nombre_producto.setText("")
        self.ui.text_descripcion.setText("")
        self.ui.double_precio.setValue(0)
        self.ui.combo_categoria.setCurrentIndex(0)
        