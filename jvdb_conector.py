import subprocess

class Jvdb:
    def __init__(self,basededatos):
        self.basededatos = basededatos
    def insert(self,coleccion,documento,contenido):
        self.operacion = "insert"
        self.coleccion = coleccion
        self.documento = documento
        self.contenido = contenido
        comando = '"C:\\Users\\laura\\Documents\\GitHub\\jvdb\\jvdb.exe" '+self.operacion+' '+self.basededatos+' '+self.coleccion+' '+self.documento+' '+self.contenido+''
        resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        if resultado.returncode == 0:
            return("ok")
        else:
            return("ko")
        
    def select(self,coleccion,documento,contenido):
        self.operacion = "select"
        self.coleccion = coleccion
        self.documento = documento
        self.contenido = contenido
        comando = '"C:\\Users\\laura\\Documents\\GitHub\\jvdb\\jvdb.exe" '+self.operacion+' '+self.basededatos+' '+self.coleccion+' '+self.documento+' '+self.contenido+''
        resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        if resultado.returncode == 0:
            print(self.contenido)
        else:
            return("ko")
