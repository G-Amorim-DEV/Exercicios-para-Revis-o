def moda(lista):
    if len(lista) == 0:
        return None
    
    moda = lista[0]
    max_contagem = 0
    contagens = {}

    for i in lista:
        contagens[i] = contagens.get(i, 0) + 1

    for valor, contagem in contagens.items():
        if contagem > max_contagem:
            max_contagem = contagem
            moda = valor

    if list(contagens.values()).count(max_contagem) == len(contagens):
        return "Não existe moda"

    return moda



lista1 = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9]
lista2 = [i//10 for i in range(100, -10, -1)] + [10,11,12,13,14,5,16,17,18,19]
lista3 = [(i**3)//1000 for i in range(100, -10, -1)]


print("Digite 1 - Para lista1.")
print("Digite 2 - Para lista2.")
print("Digite 3 - Para lista3.")

try:
    lista_desejada = int(input("Digite qual lista você deseja calcular a moda: "))

    if lista_desejada == 1:
        print("Lista1:", lista1)
        print(f"A moda da lista1 é {moda(lista1)}")

    elif lista_desejada == 2:
        print("Lista2:", lista2)
        print(f"A moda da lista2 é {moda(lista2)}")

    elif lista_desejada == 3:
        print("Lista3:", lista3)
        print(f"A moda da lista3 é {moda(lista3)}")

    else:
        print("O número digitado não corresponde a nenhuma lista.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro (1, 2 ou 3).")