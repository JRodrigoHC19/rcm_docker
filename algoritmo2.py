import sys, json

datos = sys.argv[1]
di = json.loads(datos)

hoteles_valoraciones = {}

def calcular_raiting():
 for clave in di:
  hoteles_valoraciones[clave['ruc_hotel']] = (clave['cal_hab'] + clave['cal_ins'] + clave['cal_pre'] + clave['cal_rep'] + clave['limp'] + clave['rcm_hot'])/6

if __name__ == "__main__":
 calcular_raiting()
 print(hoteles_valoraciones)
