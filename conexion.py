from jvdb_conector import Jvdb

#Conexion1= Jvdb("miempresa")
#Conexion1.insert("clientes", "clientes8", "este es otro contenido de prueba")

Conexion2= Jvdb("miempresa")
Conexion2.select("clientes", "cliente8", "este es otro contenido de prueba")
