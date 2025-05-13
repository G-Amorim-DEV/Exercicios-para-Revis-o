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


lista3 = [(i**3)//1000 for i in range(100, -10, -1)]

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

algoritmo_programa_principal = (""" Início do Programa:

lista3 ← lista onde cada elemento é o cubo de i dividido por 1000 (parte inteira), para i de 100 até 0, decrescendo de 1 em 1

Exibir "Digite 3 - Para lista3."


lista_desejada ← Ler entrada do usuário como número inteiro

   	
Se lista_desejada = 3:
    Exibir "Lista3:", lista3
    Exibir "A moda da lista3 é", MODA(lista3)
	Exibir 	Algoritmo_Função_moda
	Exibir Algoritmo_Programa_Principal
	

Senão:
    Exibir "O número digitado não corresponde a nenhuma lista.
                                Fim do Programa """)




print("Digite 3 - Para lista3.")

lista_desejada = int(input("Digite qual lista você deseja calcular a moda: "))

if lista_desejada == 3:
    print("Lista3:", lista3)
    print(f"A moda da lista3 é {moda(lista3)}")
    print("Análise do Algoritmo Lista3:\n")
    print(algoritmo_função_moda)
    print(algoritmo_programa_principal)

else:
    print("O número digitado não corresponde a nenhuma lista.")

