import mariadb
from dotenv import load_dotenv
import os

class BaseDatos:
    def __init__(self) -> None:
        load_dotenv()
        self.configuracion = {
            "user":os.getenv("USER"),
            "password": os.getenv("PASSWORD"),
            "host": os.getenv("HOST"),
            "port": int(os.getenv("PORT")),
            "database": os.getenv("DATABASE")}
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
        self.columna_id = self.columnas[0]
    
    def select(self,id=-1):
        if id == -1:
            condicion = "TRUE"
        else:
            condicion = f"{self.columna_id} = {id}"
        return self.bd.consultar(f"SELECT * FROM {self.nombre_tabla} WHERE {condicion};")
    def insert(self,*datos):
        self.columnas.pop(0)
        if len(datos) != len(self.columnas):
            return False
        
        sql = f"INSERT INTO {self.nombre_tabla}({','.join(self.columnas)}) VALUES ('{"','".join(datos)}');"        
        self.columnas.insert(0,self.columna_id)

        return self.bd.ejecutar(sql)
    
    def update(self,id,datos):
        columnas_existen = all(tuple(map(lambda x: tuple(filter(lambda y: x==y,self.columnas)),datos.keys())))
        if not columnas_existen:
            return False
        datos = str([str(x)+"="+f"'{y}'" for x,y in zip(datos.keys(),datos.values())])[1:-1].replace('"',"")
        sql = f"UPDATE {self.nombre_tabla} SET {datos} WHERE {self.columna_id}={id};"
        return self.bd.ejecutar(sql)
        
    
    def delete(self,id):
        return self.bd.ejecutar(f"DELETE FROM {self.nombre_tabla} WHERE {self.columna_id}={id};")
        
