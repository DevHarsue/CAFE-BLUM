import mariadb

class BaseDatos:
    def __init__(self) -> None:
        self.configuracion = {"user":"user","password":"9999","host":"localhost","port":3306,"database":"cafe_blum"}

    def conexion(self):
        conexion = mariadb.connect(**self.configuracion)
        cursor = conexion.cursor()
        return conexion,cursor
    
    def consultar(self,sql):
        try:
            conexion,cursor = self.conexion()
            cursor.execute(sql)
            resultado = cursor.fetchall()
            conexion.close()
            return resultado
        except Exception:
            return False

    def ejecutar(self,sql):
        try:
            conexion,cursor = self.conexion()
            cursor.execute(sql)
            conexion.commit()
            conexion.close()
            return True
        except Exception as e:
            print(e)
            return False
    
    
            
class Tabla:
    def __init__(self,nombre_tabla):
        self.bd = BaseDatos()
        self.nombre_tabla = nombre_tabla
        self.definir()
    
    def definir(self):
        self.columnas = self.bd.consultar(f"DESCRIBE {self.nombre_tabla};")
        self.columnas = [x[0] for x in self.columnas]
        self.columnas_id = self.columnas[0]
        
    def insert(self,*datos):
        self.columnas.pop(0)
        sql = f"INSERT INTO {self.nombre_tabla}({','.join(self.columnas)}) VALUES ();"
        self.columnas.insert(0,self.columnas_id)
        print(sql)
        

tabla = Tabla("clientes")
tabla.insert()