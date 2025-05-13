def moda(lista):
    if len(lista) == 0:
        return None
    
    valor_moda = lista[0]
    max_contagem = 0
    contagens = {}

    for i in lista:
        contagens[i] = contagens.get(i, 0) + 1

    for valor, contagem in contagens.items():
        if contagem > max_contagem:
            max_contagem = contagem
            valor_moda = valor

    if list(contagens.values()).count(max_contagem) == len(contagens):
        return "Não existe moda"

    return valor_moda


lista1 = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9]


print("Digite 1 - Para lista1.")

algoritmo_função_moda = ("""Função MODA(lista):
    Se o tamanho da lista for 0:
        Retornar NULO

    valor_moda ← primeiro elemento da lista
    max_contagem ← 0
    contagens ← dicionário vazio

    Para cada elemento i na lista:
        Se i está em contagens:
            contagens[i] ← contagens[i] + 1
        Senão:
            contagens[i] ← 1

    Para cada (valor, contagem) em contagens:
        Se contagem > max_contagem:
            max_contagem ← contagem
            valor_moda ← valor

    Se a quantidade de vezes que max_contagem aparece em contagens for igual ao número de elementos únicos:
        Retornar "Não existe moda"

    Retornar valor_moda""")

algoritmo_programa_principal = ("""Início do Programa:

lista1 ← [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9]

Exibir "Digite 1 - Para lista1."


lista_desejada ← Ler entrada do usuário como número inteiro

Se lista_desejada = 1:
    Exibir "Lista1:", lista1
    Exibir "A moda da lista1 é", MODA(lista1)
	Exibir 	Algoritmo_Função_moda
	Exibir Algoritmo_Programa_Principal
	

Senão:
    Exibir "O número digitado não corresponde a nenhuma lista.""")




lista_desejada = int(input("Digite qual lista você deseja calcular a moda: "))

if lista_desejada == 1:
    print("Lista1:", lista1)
    print(f"A moda da lista1 é {moda(lista1)}\n")
    print("Análise do Algoritmo Lista1:")
    print(algoritmo_função_moda)
    print(algoritmo_programa_principal)
    

else:
    print("O número digitado não corresponde a nenhuma lista.")

