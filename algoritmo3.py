import sys, json
from max_heap import *

datos = sys.argv[1]
di = json.loads(datos)

di_recomen = {}


def obtener_clave(diccionario, valor_buscado):
 for clave, valor in diccionario.items():
  if valor == valor_buscado:
   diccionario[clave] = 10
   return clave
 return None  # Si no se encuentra el valor, se devuelve None o se puede lanzar una excepción




if __name__ == "__main__":
 for clave in di:
  di_recomen[clave['email']] = clave['valoracion']

 sorted(di_recomen.items(), key=lambda x: x[1], reverse=True)
  
 maxHeap = MaxHeap(len(di_recomen))

 for clave, valor in di_recomen.items():
  maxHeap.insert(valor)

 respuesta = {}
   
 for elemento in maxHeap.Heap:
  clave = obtener_clave(di_recomen, elemento)
  if clave is None:
   pass
  else:
   respuesta[clave] = elemento
 print(respuesta)