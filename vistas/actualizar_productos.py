from submain import MainWindow
from conexion.tablas import TablaProductos
from validaciones.validador_lines import Validador

class VistaActualizarProducto:
    def __init__(self,ventana: MainWindow) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_actualizar_eproducto.pressed.connect(self.actualizar)
        self.ui.boton_borrar_eproducto.pressed.connect(self.borrar)
        Validador().solo_texto_productos(self.ui.line_nombre_eproducto)
    
    def cargar(self,datos):
        self.datos = datos
        self.ui.line_nombre_eproducto.setText(self.datos[1])
        self.ui.text_descripcion_eproducto.setText(self.datos[2])
        self.ui.combo_eproducto.setCurrentText(self.datos[-1])
        self.ui.double_precio_eproducto.setValue(float(self.datos[3]))
    
    def actualizar(self):
        id = self.datos[0]
        nombre = self.ui.line_nombre_eproducto.text()
        descripcion = self.ui.text_descripcion_eproducto.toPlainText()
        precio = self.ui.double_precio_eproducto.value()
        categoria = self.ui.combo_eproducto.currentText()
        
        if nombre == "":
            self.ventana.mostrar_mensaje("Error", "El nombre no puede estar vacío")
            return 0
        if precio<=0:
            self.ventana.mostrar_mensaje("Error", "El precio debe ser mayor a 0")
            return 0
        
        self.ventana.preguntar("Actualizar producto","¿Estas seguro de Actualizar el Producto?")
        if not self.ventana.respuesta:
            return 0
        TablaProductos().update(id,{"producto_nombre":nombre,"producto_descripcion":descripcion,"producto_precio":precio,"producto_categoria":categoria})
        self.ventana.mostrar_mensaje("Producto Actualizado","Producto Actualizado Correctamente")
        self.ui.stacked_widget.setCurrentWidget(self.ui.widget_productos)
        self.ventana.vista_producto.agregar_productos()
        for x in range(self.ui.table_productos_facturar.rowCount()):
            if self.ui.table_productos_facturar.item(x,0).text() == str(self.datos[0]):
                self.ui.table_productos_facturar.item(x,1).setText(nombre)
                self.ui.table_productos_facturar.item(x,2).setText(str(precio))
                self.ui.table_productos_facturar.item(x,4).setText(str(precio*int(self.ui.table_productos_facturar.item(x,3).text())))
                self.ventana.vista_factura.calcular()
                self.ventana.vista_factura.calcular_dolar()
                self.ventana.vista_factura.calcular_bs()
                self.ventana.vista_factura.calcular_cop()
    
    def borrar(self):
        self.ventana.preguntar("Borrar Producto","¿Estas seguro de borrar el producto?")
        if not self.ventana.respuesta:
            return 0
        TablaProductos().delete(self.datos[0])
        self.ventana.mostrar_mensaje("Producto Borrado","El producto ha sido borrado exitosamente")
        self.ui.stacked_widget.setCurrentWidget(self.ui.widget_productos)
        self.ventana.vista_producto.agregar_productos()
        for x in range(self.ui.table_productos_facturar.rowCount()):
            if self.ui.table_productos_facturar.item(x,0).text() == str(self.datos[0]):
                self.ui.table_productos_facturar.removeRow(x)
                self.ventana.vista_factura.calcular()
                self.ventana.vista_factura.calcular_bs()
                self.ventana.vista_factura.calcular_cop()
                self.ventana.vista_factura.calcular_dolar()
                break