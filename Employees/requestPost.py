"""
Obtenemos los datos de un archivo .txt, y los procesamos para mandarlos a una aplicacion de Spring.
"""
import requests

# Definimos la clase Employees.

class Employees:
    
    def __init__(self):
        try:
            self.archivo = open("Archivos\Clientes.txt", "r", encoding="utf-8")
        
        except Exception as e:
            print(e.message, e.args)
        
    def post(self):
        try:
            # Formamos dos listas y separamos sus elementos por coma.
            
            lectura = self.archivo.read().split('\n')
            
            empleado1 = lectura[0].split(sep=', ')
            empleado2 = lectura[1].split(sep=', ')
            
            url = "http://localhost:8080/employee/apiv1/clientes/add"
            
            diccionarioEmpleado1 = {"surname": empleado1[1], "firstname": empleado1[0],  "country": empleado1[2], "language": empleado1[3], "airport": empleado1[4]}        
            diccionarioEmpleado2 = {"surname": empleado2[1], "firstname": empleado2[0],  "country": empleado2[2], "language": empleado1[3], "airport": empleado2[4]}
                        
            resp1 = requests.post(url, json=diccionarioEmpleado1) # print(resp1)
            resp2 = requests.post(url, json=diccionarioEmpleado2) # Devuelve una respuesta 200 (resp1 y resp2)
            
            print("Los datos han sido procesados correctamente. " + "\n" + str(resp1))
            return diccionarioEmpleado1, diccionarioEmpleado2
            
        except Exception as e:
            print(e.message, e.args)
        
# Creamos una instancia de la clase

objeto = Employees()
objeto.post()