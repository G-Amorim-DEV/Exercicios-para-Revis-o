def busca_em_largura(grafo, inicio):
    n = len(grafo)
    visitados = [False] * n
    distancias = [-1] * n
    fila = [inicio]
    visitados[inicio] = True
    distancias[inicio] = 0

    while fila:
        vertice = fila.pop(0)

        for vizinho in range(n):
            if grafo[vertice][vizinho] == 1 and not visitados[vizinho]:
                visitados[vizinho] = True
                fila.append(vizinho)
                distancias[vizinho] = distancias[vertice] + 1

    return distancias

def maior_distancia(grafo):
    n = len(grafo)
    maior_dist = 0

    for i in range(n):
        distancias = busca_em_largura(grafo, i)

        for dist in distancias:
            if dist > maior_dist:
                maior_dist = dist

    return maior_dist


grafo_matriz1 = [[0, 1, 1, 0, 0, 0],
                [1, 0, 1, 1, 0, 1],
                [1, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 1],
                [0, 0, 1, 1, 0, 1],
                [0, 1, 0, 1, 1, 0]]

grafo_matriz2 = [[0, 1, 0, 0, 0, 0],
                [1, 0, 1, 1, 0, 1],
                [0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1],
                [0, 1, 0, 0, 1, 0]]

grafo_matriz3 = [[0, 1, 0, 0, 0, 0],
                [1, 0, 1, 0, 0, 0],
                [0, 1, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 0, 1],
                [0, 0, 0, 1, 1, 0]]

print("Digite 1 - Para o Grafo_Matriz1.")
print("Digite 2 - Para o Grafo_Matriz2.")
print("Digite 3 - Para o Grafo_Matriz3.")

try:
    lista_desejada = int(input("Digite qual Grafo você deseja ver a maior distância: "))

    if lista_desejada == 1:
        maior_distancia1 = maior_distancia(grafo_matriz1)
        print("Grafo_Matriz1:", grafo_matriz1)
        print(f"A maior distância de Grafo_Matriz1 é {maior_distancia1}")

    elif lista_desejada == 2:
        maior_distancia2 = maior_distancia(grafo_matriz2)
        print("Grafo_Matriz2:", grafo_matriz2)
        print(f"A maior distância de Grafo_Matriz2 é {maior_distancia2}")

    elif lista_desejada == 3:
        maior_distancia3 = maior_distancia(grafo_matriz3)
        print("Grafo_Matriz3:", grafo_matriz3)
        print(f"A maior distância de Grafo_Matriz3 é {maior_distancia3}")

    else:
        print("O número digitado não corresponde a nenhum grafo.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro (1, 2 ou 3).")
