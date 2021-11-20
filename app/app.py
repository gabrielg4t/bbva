import pandas as pd

datos = pd.read_csv('data.csv', header=0, parse_dates=['id'])

while True:
    print("Ingresa un valor para filtrar la información:")
    entrada = input()
    resultado = datos[datos['id'] == entrada]
    if entrada == 'x':
        break
    else:
        print(resultado)
        resultado.to_json(r'salida.json')
        print("\n Presiona x para salir")
