from flask import Flask, request, jsonify
app = Flask(__name__)
import subprocess

@app.route('/ruta_flask/', methods=['GET'])
def sumarNumerosEnFlask():
 data=request.args.get('data')
 niveles=int(request.args.get('pasos'))
 
 if niveles == 1:
  resultado = subprocess.run(['python', 'algoritmo1.py', data], capture_output=True, text=True)
  salida = eval(resultado.stdout.strip())
  return jsonify(salida)
   
 elif niveles == 2:
  resultado = subprocess.run(['python', 'algoritmo2.py', data], capture_output=True, text=True)
  salida = eval(resultado.stdout.strip())
  return jsonify(salida)
   
 elif niveles == 3:
  resultado = subprocess.run(['python', 'algoritmo3.py', data], capture_output=True, text=True)
  salida = eval(resultado.stdout.strip())
  return jsonify(salida)

if __name__ == '__main__':
 app.run( host='0.0.0.0', port=8000)
