from CONEXION import*
#-------------------CClientes
#-------------------clase para ingresar troncales nuevas-----------
class Topologias:
    @staticmethod

    def mostrarTroncal(term = ""):
        try:      
            cone = Cconexion.ConexioBaseDeDatos()
            cursor = cone.cursor()
            consulta = f"SELECT * FROM inf_topologias WHERE `Equipo  destino` LIKE '%{term}%'"
            cursor.execute(consulta)
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado
        except mysql.connector.Error as error:
            print("Error al realizar consulta de datos {}".format(error))
    @staticmethod
    def mostrarUltimo():
        try:
            cone = Cconexion.ConexioBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("SELECT * FROM inf_topologias ORDER BY nuevo_id DESC LIMIT 1;") 
            ultimoRegistro = cursor.fetchall()
            cone.commit()
            cone.close()
            return ultimoRegistro
        except mysql.connector.Error as error:
            print("Error al mostrar ultimo dato guardado {}".format(error))
    
    
    
    def ingresarTroncal(Equipo_destino, TrunkDest, TrkROU, Equipo_ROU, TrkRx1, EquipoTx1, TrkTx1, TrkRx2, EquipoTx2, TrkTx2, TrkRx3, EquipoTx3, TrkTx3, TrkRx4, EquipoTx4, TrkTx4, TrkRx5, EquipoTx5, TrkTx5, Tecnologia, UbicaciónDest, UbicaciónRou):
      try:
          cone1 = Cconexion.ConexioBaseDeDatos()
          cursor1 = cone1.cursor()
          #----%s representa un valor de ingreso por el formulario
          sql = "insert into inf_topologias values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,null);"
          valores = (Equipo_destino, TrunkDest, TrkROU, Equipo_ROU, TrkRx1, EquipoTx1, TrkTx1, TrkRx2, EquipoTx2, TrkTx2, TrkRx3, EquipoTx3, TrkTx3, TrkRx4, EquipoTx4, TrkTx4, TrkRx5, EquipoTx5, TrkTx5, Tecnologia, UbicaciónDest, UbicaciónRou)
          cursor1.execute(sql, valores)
          cone1.commit()
          print(cursor1.rowcount, "Registro grabado")
          cone1.close()
      except mysql.connector.Error as error:
          print("Error al ingresar datos {}".format(error))
    @staticmethod
    def modificarTroncal(Equipo_destino,	TrunkDest,	TrkROU,	Equipo_ROU,	TrkRx1,	EquipoTx1,	TrkTx1,	TrkRx2,	EquipoTx2,	TrkTx2,	TrkRx3,	EquipoTx3,	TrkTx3,	TrkRx4,	EquipoTx4,	TrkTx4,	TrkRx5,	EquipoTx5,	TrkTx5,	Tecnologia,	UbicaciónDest,	UbicaciónRou,nuevo_id):
        try:
            cone = Cconexion.ConexioBaseDeDatos()
            cursor = cone.cursor()
            #----%s representa un valor de ingreso por el formulario
            sql = "update inf_topologias set inf_topologias.`Equipo  destino`=%s,inf_topologias.TrunkDest = %s, inf_topologias.TrkROU=%s,inf_topologias.`Equipo ROU`=%s,inf_topologias.TrkRx1=%s,inf_topologias.EquipoTx1=%s,inf_topologias.TrkTx1=%s,inf_topologias.TrkRx2=%s,inf_topologias.EquipoTx2=%s,inf_topologias.TrkTx2=%s,inf_topologias.TrkRx3=%s,inf_topologias.EquipoTx3=%s,inf_topologias.TrkTx3=%s,inf_topologias.TrkRx4=%s,inf_topologias.EquipoTx4=%s,inf_topologias.TrkTx4=%s,inf_topologias.TrkRx5=%s,inf_topologias.EquipoTx5=%s,inf_topologias.TrkTx5=%s,inf_topologias.Tecnologia=%s,inf_topologias.UbicaciónDest=%s,inf_topologias.UbicaciónRou=%s where inf_topologias.nuevo_id=%s;"
            valores = (Equipo_destino,	TrunkDest,	TrkROU,	Equipo_ROU,	TrkRx1,	EquipoTx1,	TrkTx1,	TrkRx2,	EquipoTx2,	TrkTx2,	TrkRx3,	EquipoTx3,	TrkTx3,	TrkRx4,	EquipoTx4,	TrkTx4,	TrkRx5,	EquipoTx5,	TrkTx5,	Tecnologia,	UbicaciónDest,	UbicaciónRou,nuevo_id)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error al Actualizar datos {}".format(error))  
   