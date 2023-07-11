import sys, json

datos = sys.argv[1]
di = json.loads(datos)
# VARIABLES ACUMULADORES DE PUNTOS SEGÚN SU TIPO
A = 0
F = 0
C = 0
D = 0
P = 0
B = 0
N = 0
R = 0
T = 0



# ACUMULACIÓN DE PUNTOS SEGÚN EL TIPO DE HOTEL
for valor in di:
 A += int(valor["A"])
 F += int(valor["F"])
 C += int(valor["C"])
 D += int(valor["D"])  
 P += int(valor["P"])
 B += int(valor["B"])
 N += int(valor["N"])
 R += int(valor["R"])
 T += int(valor["T"])

# Establece las posiciones de cada tipo de hotel
gustos = {
  0: A,
  1: F,
  2: C,
  3: D,
  4: P,
  5: B,
  6: N,
  7: R,
  8: T
}

 # SE ORDENA LAS VALORES DE TODAS LAS CLAVES - MAYOR A MENOR
gustos_ordenados = dict(sorted(gustos.items(), key=lambda x: x[1], reverse=True))

 # ESTA LISTA CONTENDRÁ LAS 2 CLAVES DE MAYOR VALOR
resultado = []

 # BUCLE PARA COGER Y ALMACENAR ESAS 2 CLAVES
contador = 0
for clave, valor in gustos_ordenados.items():
  # SE ALMACENAN ESAS CLAVES [POSICIONES]
 resultado.append(clave)
 contador += 1
 if contador >=2:   
  break

print(resultado)
