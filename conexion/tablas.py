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
    
    def select_ultima_factura(self):
        return self.bd.consultar(f"SELECT * FROM facturas ORDER BY factura_id DESC LIMIT 1;")
    
    def select_cliente(self, id):
        return self.bd.consultar(f"SELECT * FROM facturas WHERE cliente_id='{id}'")
    
    def delete_cliente(self,id):
        return self.bd.ejecutar(f"DELETE FROM facturas WHERE cliente_id='{id}';")

class TablaProductos(Tabla):
    def __init__(self):
        super().__init__("productos")
    
    def select_nombre(self,nombre):
        return self.bd.consultar(f"SELECT * FROM productos WHERE producto_nombre LIKE '{nombre}%';")
    def select_nombre_categoria(self,nombre,categoria):
        return self.bd.consultar(f"SELECT * FROM productos WHERE producto_nombre LIKE '{nombre}%' AND producto_categoria='{categoria}';")

class TablaDetalles(Tabla):
    def __init__(self):
        super().__init__("factura_detalles")
    
    def delete_factura(self,id):
        return self.bd.ejecutar(f"DELETE FROM factura_detalles WHERE factura_id='{id}';")
        
class TablaUsuarios(Tabla):
    def __init__(self):
        super().__init__("usuarios")

    def select_usuario(self,nombre):
        return self.bd.consultar(f"SELECT * FROM usuarios WHERE usuario_nombre='{nombre}';")
    
    def select_rol(self):
        return self.bd.consultar(f"SELECT usuario_rol FROM usuarios;")

class TablaTotales(Tabla):
    def __init__(self):
        super().__init__("totales_diarios")
    
    def select_fecha(self,fecha):
        return self.bd.consultar(f"SELECT * FROM totales_diarios WHERE total_fecha='{fecha}';")
    
    def calcular_diario(self,fecha):
        return self.bd.consultar(f"CALL calcular_diario('{fecha}');")