# -*- coding: utf-8 -*-
"""algoritmo_moedas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yrzpMRw17QQmjvCVSOg9wDWQFKTMfRpe
"""

def printMoedasUsadas(moedasUsadas, troco):
  valor = troco #Começa sempre do fim para o inicio, por isso mostra em ordem decrescente os valores
  while(valor>0):
    moedaAtual = moedasUsadas[valor] #Pegando a moeda usada 
    print(moedaAtual)
    valor = valor - moedaAtual #A moeda usada diz quantas casas temos de voltar para saber a prox moeda usada, além de informar qual moeda a compõe :D

def slTroco(moedas, troco, listaQtd, moedasUsadas):
  #Percorrer todos os valores do troco, de 0 até ele(troco)
  for valor in range(troco+1):
    #Vai começar com a solução trivial: quantidade minima = total do troco e a moeda usada = 1 centavo
    minMoedas = valor
    moedaUsada = 1
    # print("Calculando para", valor)
    #Usando um for para percorrer somente as moedas que podem compor o valor em questão, o loop se renova a cada incremento de valor(For anterior) 
    for j in [m for m in moedas if m <= valor]: #Setar o j até a maior moeda disponivel
      # print('Moeda atual: ', j, "Pos(sub): ", valor-j, 'acesso=', listaQtd[valor-j]+1)
      if (listaQtd[valor-j]+1 < minMoedas): #Sempre fica com o primeiro menor
        minMoedas = listaQtd[valor-j]+1 # o 1 se refere a moeda atual sendo acrescida ao total anterior
        moedaUsada = j
    listaQtd[valor] = minMoedas
    moedasUsadas[valor] = moedaUsada
  return listaQtd[troco] #Retorna na posição exata do troco com a quantidade de total de moedas usadas

def main():#Função principal
  moedas = [1, 2, 8, 14, 25]
  troco = int(input("Qual o valor em centavos de troco? "))
  #Montando as listas de zeros com base no valor do troco
  moedasUsadas = [0]*(troco+1)
  listaQtd = [0]*(troco+1)
  
  print("Para fornecer R$ 0,", troco, "de troco, precisamos de")
  print(slTroco(moedas,troco,listaQtd,moedasUsadas),"moedas")
  print("Sendo elas:")
  printMoedasUsadas(moedasUsadas,troco)
  print("============================INFO============================")
  print("Lista de moedas usadas:")
  print(moedasUsadas)
  print('Lista de quantidades')
  print(listaQtd)

main()