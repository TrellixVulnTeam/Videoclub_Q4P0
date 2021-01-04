import sys
import psycopg2
from psycopg2 import errorcodes

class Conexion:

    def conectar(self):
        try:
            conexion = psycopg2.connect(host="localhost",
                                        database="Videoclub",
                                        user="postgres",
                                        password="i637 jack")
            print("Conectado correctamente")
            return conexion
        except psycopg2.Error as e:
            if e.pgerror == errorcodes.DATABASE_DROPPED:
                print("La base de datos no existe")
            else :
                print ("Unable to connect!")
                print (e.pgerror)
                print (e.diag.message_detail)
                sys.exit(1)

    def cerrarConexion(self, conexion):
        print("Cerrando conexion")
        conexion.close()
        print("Conexion cerrada")


