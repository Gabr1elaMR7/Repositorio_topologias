#----------conectar con sql y base de datos---

import mysql.connector
class Cconexion:                                          
          
    def ConexioBaseDeDatos():
     try:
        conexion = mysql.connector.connect(user = 'root' ,password= '1234',host='127.0.0.1',
                                           database='troncales',
                                           port='3306')
        print("Conexion exitosa")
        return conexion

     except mysql.connector.Error as error:
        print("Error al conectar con la base de datos {}".format(error))        
        return conexion                                      
        
    ConexioBaseDeDatos()