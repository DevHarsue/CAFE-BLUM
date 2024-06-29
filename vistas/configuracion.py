from submain import MainWindow
from ventanas import VentanaConfiguracion,VentanaUsuarios

class VistaConfiguracion:
    def __init__(self,ventana: MainWindow) -> None:
        self.ventana = ventana
        self.ui = ventana.ui
        self.ui.boton_configurar_bd.pressed.connect(self.configurar_bd)
        self.configurar = VentanaConfiguracion(self.ventana)
        self.configurar.ui.pushButton_2.show()

        self.ui.boton_registrar_usuarios.pressed.connect(self.registro)
        self.usuarios = VentanaUsuarios(self.ventana)
        self.usuarios.ui.comboBox.removeItem(0)
        self.usuarios.ui.pushButton_2.show()
        
        self.ui.boton_actualizar_usuarios.pressed.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.widget_actualizar_usuarios))
    
    def registro(self):
        self.usuarios.reiniciar()
        self.usuarios.show()
        self.ventana.close()
    
    def configurar_bd(self):
        self.configurar.ui.lineEdit.setText("")
        self.configurar.ui.lineEdit_2.setText("")
        self.configurar.ui.lineEdit_3.setText("")
        self.configurar.ui.lineEdit_4.setText("")
        self.configurar.show()
        self.ventana.close()