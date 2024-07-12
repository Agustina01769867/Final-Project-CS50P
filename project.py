import matplotlib.pyplot as plt
import numpy as np
import random as random
import math
import pandas as pd
import sys
from urllib.error import HTTPError


def calcular_beta1(x, y):
    first_sum = 0
    third_sum = sum(x)

    # Algoritmo para beta1 (pendiente m)
    for i in range(len(y)):
        first_sum += x[i] * y[i]

    nxy = len(x) * np.mean(x) * np.mean(y)

    second_sum = sum([xi ** 2 for xi in x])

    m = (first_sum - nxy) / (second_sum - ((1/len(x)) * (third_sum ** 2)))
    return m


def calcular_beta0(x, y, m):
    sum_y = sum(y)
    sum_x = sum(x)
    second_sum = sum([xi ** 2 for xi in x])
    sumx_sqr = sum_x ** 2

    # Algoritmo para beta0 (intersección b)
    denominator = (len(x) * second_sum) - sumx_sqr

    if denominator == 0:
        raise ValueError("Denominador es cero en el cálculo de beta0")

    # Algoritmo para beta0 (intersección b)
    b = ((second_sum * sum_y) - (sum_x * sum([x[i] * y[i] for i in range(len(x))]))) / denominator
    return b


def get_csv(company):
    try:
        url = f"https://query1.finance.yahoo.com/v7/finance/download/{company}?period1=1688958542&period2=1720580942&interval=1d&events=history&includeAdjustedClose=true"
        df = pd.read_csv(url)
        return df
    except HTTPError as e:
        sys.exit(f"HTTP Error {e.code}: {e.reason}")


def main():
    if len(sys.argv) < 2:
       sys.exit("Company not provided")

    df = get_csv(sys.argv[1])

    close_values = df['Close'].tolist()
    days = list(range(1, len(close_values) + 1))

    #Cálculo de rendimientos del activo
    rendimientos = []

    for i in range(1, len(close_values)):
        rendimientos.append(math.log(close_values[i]/close_values[i-1]))

    # Listas de intervalo de confianza
    x1 = list(range(1, len(close_values)))
    y1 = rendimientos

    # Calcular beta1 y beta0
    m = calcular_beta1(x1, y1)
    b = calcular_beta0(x1, y1, m)

    # Buscar intervalo de confianza
    for i in range(len(x1)):
        parametro = (calcular_beta1(x1, y1) * days[-1]) / calcular_beta0(x1, y1, m)

        if abs(parametro) <= 0.15:
            promedio = np.mean(x1)
            std = np.std(x1)

            contador = 0

            for j in x1:
                if (promedio - std) <= j <= (promedio + std):
                    contador += 1

            if (contador / len(y1)) > 0.60:
                break

        else:
            x1.pop(0)
            y1.pop(0)


    # Inicia simulación del activo
    m1 = calcular_beta1(x1, y1)
    mu = calcular_beta0(x1, y1, m)

    sigma = np.std(y1)
    a = np.zeros(10000)

    for i in range(len(a)):
        a[i] = random.gauss(mu,sigma)

    v0 = close_values[-1]

    performance = np.zeros((100,10)) # 100 caminos diferentes en 10 dias
    assets = np.zeros((100,11)) # valor de los activos + día 0 (v0)

    for i in range(100):
        for k in range(10):
            performance[i, k] = random.gauss(mu,sigma)

    for i in range(100):
        assets[i,0] = v0

    for i in range(100):
        for k in range(1,11):
            assets[i, k] = v0*math.exp(sum(performance[i, 0:k-1]))


    #Graficar rendimientos despues de intervalo de confianza
    plt.scatter(days_rendimientos, rendimientos, color='blue', label='Intevalo de confianza de rendimientos')
    plt.plot(days_rendimientos, [m1 * xi + mu for xi in days_rendimientos], color='red')
    plt.xlabel('Tiempo')
    plt.ylabel('Rendimiento')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
