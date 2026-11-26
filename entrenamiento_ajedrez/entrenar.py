import json
import math
import random

from caracteristicas import caracteristicas

ARCHIVO = "muestra.jsonl"
POSICIONES = 30000
RONDAS = 15
TASA = 0.001
TOLERANCIA = 0.02
MAX_INTENTOS = 1000

# esto define el numero de capas (cada numero es una capa)
# esto define el numero de perceptrones (9 entradas, 16, 8 y 1)
CAPAS = [9, 16, 8, 1]


# lee las posiciones y su valor esperado
def leer_datos():
    datos = []
    for linea in open(ARCHIVO, encoding="utf-8"):
        d = json.loads(linea)

        mejor = d["evals"][0]
        for e in d["evals"]:
            if e["depth"] > mejor["depth"]:
                mejor = e
        pv = mejor["pvs"][0]

        if "cp" in pv:
            objetivo = math.tanh(pv["cp"] / 400)
        elif pv["mate"] > 0:
            objetivo = 1
        else:
            objetivo = -1

        datos.append((caracteristicas(d["fen"]), objetivo))
        if len(datos) % 1000 == 0:
            print("leidas", len(datos))
        if len(datos) >= POSICIONES:
            break
    return datos


# pesos y bias iniciales al azar
pesos = []
bias = []
# este es el ciclo de cada capa
for c in range(1, len(CAPAS)):
    entradas = CAPAS[c - 1]
    limite = math.sqrt(1 / entradas)
    capa = []
    # este es el ciclo de cada perceptron
    for p in range(CAPAS[c]):
        w = []
        for i in range(entradas):
            w.append(random.uniform(-limite, limite))
        capa.append(w)
    pesos.append(capa)
    bias.append([0.0] * CAPAS[c])


# calcula la salida de cada capa: tanh(w1*x1 + ... + wn*xn + b)
def calcular(entrada):
    salidas = [entrada]
    # este es el ciclo de cada capa
    for c in range(len(pesos)):
        x = salidas[-1]
        nueva = []
        # este es el ciclo de cada perceptron
        for p in range(len(pesos[c])):
            z = bias[c][p]
            for i in range(len(x)):
                z += pesos[c][p][i] * x[i]
            nueva.append(math.tanh(z))
        salidas.append(nueva)
    return salidas


# ajusta todos los pesos una vez para una posicion
def ajustar(entrada, objetivo):
    salidas = calcular(entrada)
    resultado = salidas[-1][0]
    error = resultado - objetivo

    # delta del perceptron final
    deltas = [error * (1 - resultado * resultado)]

    # este es el ciclo de cada capa, de la ultima a la primera
    for c in range(len(pesos) - 1, -1, -1):
        x = salidas[c]

        # deltas de la capa anterior (el error se pasa hacia atras)
        anteriores = []
        if c > 0:
            for i in range(len(x)):
                suma = 0
                for p in range(len(pesos[c])):
                    suma += deltas[p] * pesos[c][p][i]
                anteriores.append(suma * (1 - x[i] * x[i]))

        # este es el ciclo de cada perceptron
        for p in range(len(pesos[c])):
            for i in range(len(x)):
                pesos[c][p][i] -= TASA * deltas[p] * x[i]   # delta de w
            bias[c][p] -= TASA * deltas[p]                  # delta de b

        deltas = anteriores


def error_promedio(datos):
    total = 0
    for entrada, objetivo in datos:
        error = calcular(entrada)[-1][0] - objetivo
        total += error * error
    return total / len(datos)


datos = leer_datos()
print("error inicial:", round(error_promedio(datos), 4))

# este es el ciclo de cada ronda
for ronda in range(1, RONDAS + 1):
    random.shuffle(datos)
    # este es el ciclo de cada posicion
    for entrada, objetivo in datos:
        error = calcular(entrada)[-1][0] - objetivo
        intentos = 0
        # repite hasta que salga
        while abs(error) > TOLERANCIA and intentos < MAX_INTENTOS:
            ajustar(entrada, objetivo)
            error = calcular(entrada)[-1][0] - objetivo
            intentos += 1
    print("ronda", ronda, "error promedio:", round(error_promedio(datos), 4))


# guarda los pesos para pegarlos en Processing
archivo = open("pesos_processing.txt", "w")
for c in range(len(pesos)):
    filas = []
    for w in pesos[c]:
        filas.append("{" + ", ".join("%.6f" % v for v in w) + "}")
    archivo.write("float[][] W%d = {\n  %s\n};\n" % (c + 1, ",\n  ".join(filas)))
    archivo.write("float[]   B%d = {%s};\n" % (c + 1, ", ".join("%.6f" % v for v in bias[c])))
archivo.close()
print("pesos guardados en pesos_processing.txt")
