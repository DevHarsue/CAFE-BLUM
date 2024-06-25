from conexion.conexion_bd import Tabla

class TablaClientes(Tabla):
    def __init__(self):
        super().__init__("clientes")
    
    def select_cedula(self,nacionalidad,cedula):
        return self.bd.consultar(f"SELECT * FROM clientes WHERE cliente_nacionalidad='{nacionalidad}' AND cliente_cedula={cedula};")

class TablaDivisas(Tabla):
    def __init__(self):
        super().__init__("divisas")
        
class TablaFacturas(Tabla):
    def __init__(self):
        super().__init__("facturas")

class TablaProductos(Tabla):
    def __init__(self):
        super().__init__("productos")

class TablaDetalles(Tabla):
    def __init__(self):
        super().__init__("factura_detalles")

class TablaRoles(Tabla):
    def __init__(self):
        super().__init__("roles")
        
class TablaUsuarios(Tabla):
    def __init__(self):
        super().__init__("usuarios")
