from Conexion import*

class Funcion(Conexion):

    def insertar(self, idusuario, nombre, apellido, usuario, telefono, correo, contraseña):
        cnx = self.conectar()
        # Creamos el cursor con el objeto conexion
        cur = cnx.cursor()
        # Ejecutamos una consulta
        cur.execute("INSERT INTO registro VALUES ('"+idusuario+"', '"+nombre+"', '"+apellido+"', '"+usuario+"', '"+telefono+"', '"+correo+"', '"+contraseña+"')")
        cnx.commit()
        self.cerrarConexion(cnx)

