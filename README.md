# 📘 Projeto: Análise de Grafos e Cálculo da Moda em Listas

Este repositório contém dois programas desenvolvidos em Python com o objetivo de aplicar e consolidar conhecimentos em algoritmos e estruturas de dados. Para melhor compreensão, foi criado também um **pseudo-código** correspondente a cada algoritmo, explicando de forma mais intuitiva a lógica de funcionamento.

---

## 📌 Objetivo

O intuito deste projeto foi praticar e reforçar conceitos importantes como:
- 🔄 Busca em largura (BFS) em grafos representados por matrizes de adjacência
- 📊 Cálculo da moda em listas numéricas
- 💡 Interpretação e transcrição de códigos para pseudo-códigos

---

## 🔍 Descrição dos Códigos

### 1️⃣ `Matriz_Grafo.py`

Este programa solicita ao usuário que selecione um dos três grafos pré-definidos. Em seguida, calcula a **maior distância mínima** (ou seja, o maior caminho entre dois vértices considerando distâncias mínimas via BFS).

- A função `busca_em_largura(grafo, inicio)` realiza a busca em largura.
- A função `maior_distancia(grafo)` itera por todos os vértices, chamando a BFS para calcular as distâncias, e retorna a maior encontrada.

🔗 Pseudo-código correspondente: [`Matriz_Grafo_Pseudo_Código.txt`](Matriz_Grafo_Pseudo_Código.txt)

---

### 2️⃣ `Moda.py`

Este script calcula a **moda** de três listas diferentes fornecidas pelo programa. A moda é o valor mais frequente de uma lista.

- A função `moda(lista)` cria um dicionário de contagem de ocorrências e retorna o valor mais frequente. Caso todos os valores tenham a mesma frequência, retorna `"Não existe moda"`.

🔗 Pseudo-código correspondente: [`Moda_Pseudo_Código.txt`](Moda_Pseudo_Código.txt)

---

## 🧠 Metodologia de Estudo

Para a elaboração dos códigos e pseudo-códigos foram utilizados:

- 📚 Conteúdos de **aulas anteriores**
- 📄 **Materiais de disciplinas passadas**
- 🌐 Pesquisas na **internet** para aprofundamento e resolução de dúvidas
- 🤖 Apoio da **Inteligência Artificial** (ChatGPT)

---

## 🛠️ Como executar

Certifique-se de ter o Python 3 instalado. Para rodar os scripts:

```bash
python Matriz_Grafo.py
