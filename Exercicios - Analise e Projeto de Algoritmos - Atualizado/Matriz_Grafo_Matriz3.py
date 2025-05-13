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


grafo_matriz3 = [[0, 1, 0, 0, 0, 0],
                [1, 0, 1, 0, 0, 0],
                [0, 1, 0, 1, 0, 0],
                [0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 0, 1],
                [0, 0, 0, 1, 1, 0]]

algoritmo_função_busca_em_largura = (""" Função BUSCA_EM_LARGURA(grafo, inicio):
    n ← tamanho do grafo
    visitados ← vetor de tamanho n com todos os valores FALSO
    distancias ← vetor de tamanho n com todos os valores -1
    fila ← lista contendo apenas o vértice 'inicio'
    visitados[inicio] ← VERDADEIRO
    distancias[inicio] ← 0

    Enquanto fila não estiver vazia:
        vertice ← remover primeiro elemento da fila

        Para vizinho de 0 até n - 1:
            Se grafo[vertice][vizinho] = 1 E visitados[vizinho] = FALSO:
                visitados[vizinho] ← VERDADEIRO
                adicionar vizinho ao final da fila
                distancias[vizinho] ← distancias[vertice] + 1

    Retornar distancias\n""")

algoritmo_função_maior_distancia = (""" Função MAIOR_DISTANCIA(grafo):
    n ← tamanho do grafo
    maior_dist ← 0

    Para i de 0 até n - 1:
        distancias ← BUSCA_EM_LARGURA(grafo, i)

        Para cada dist em distancias:
            Se dist > maior_dist:
                maior_dist ← dist

    Retornar maior_dist\n""")

algoritmo_programa_principal = ("""Início do Programa:

Exibir "Digite 3 - Para o Grafo_Matriz3."


lista_desejada ← Ler entrada do usuário como número inteiro

Se lista_desejada = 3:
    maior ← MAIOR_DISTANCIA(Grafo_Matriz3)
    Exibir Grafo_Matriz3
    Exibir "A maior distância de Grafo_Matriz3 é", maior
    Exibir (algoritmo_função_busca_em_largura)
    Exibir (algoritmo_função_maior_distancia)
    Exibir (algoritmo_programa_principal)
    


Senão:
    Exibir "O número digitado não corresponde a nenhum grafo.""")



print("Digite 3 - Para o Grafo_Matriz3.")


lista_desejada = int(input("Digite qual Grafo você deseja ver a maior distância: "))

if lista_desejada == 3:
    maior_distancia3 = maior_distancia(grafo_matriz3)
    print("Grafo_Matriz3:", grafo_matriz3)
    print(f"A maior distância de Grafo_Matriz3 é {maior_distancia3}\n")
    print("Análise do Algoritmo Grafo_Matriz3:")
    print(algoritmo_função_busca_em_largura)
    print(algoritmo_função_maior_distancia)
    print(algoritmo_programa_principal)


else:
    print("O número digitado não corresponde a nenhum grafo.")

