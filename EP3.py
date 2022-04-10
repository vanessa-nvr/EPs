"""
  AO PREENCHER ESSE CABECALHO COM O MEU NOME E O MEU NUMERO USP,
  DECLARO QUE SOU O UNICO AUTOR E RESPONSAVEL POR ESSE PROGRAMA.
  TODAS AS PARTES ORIGINAIS DESSE EXERCICIO PROGRAMA (EP) FORAM
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUCOES
  DESSE EP E QUE PORTANTO NAO CONSTITUEM DESONESTIDADE ACADEMICA
  OU PLAGIO. 
  DECLARO TAMBEM QUE SOU RESPONSAVEL POR TODAS AS COPIAS
  DESSE PROGRAMA E QUE EU NAO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUICAO. ESTOU CIENTE QUE OS CASOS DE PLAGIO E
  DESONESTIDADE ACADEMICA SERAO TRATADOS SEGUNDO OS CRITERIOS
  DIVULGADOS NA PAGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NAO SERAO CORRIGIDOS E,
  AINDA ASSIM, PODERAO SER PUNIDOS POR DESONESTIDADE ACADEMICA.

  Nome :
  NUSP :
  Turma:
  Prof.:

  Referencias: Com excecao das rotinas fornecidas no enunciado
  e em sala de aula, caso voce tenha utilizado alguma refencia,
  liste-as abaixo para que o seu programa nao seja considerado
  plagio ou irregular.
 
  Exemplo:
  - O algoritmo Quicksort foi baseado em http://wiki.python.org.br/QuickSort
"""

# Manter a linha abaixo para impressao com 'end=""' funcionar no Python 2
from __future__ import print_function

import math


# Nao altere esta funcao
def leituraParam1 () :
  N = int(input("Digite N: "))
  Beta = float(input("Digite Beta: "))
  Gama = float(input("Digite Gama: "))
  Tmax = int(input("Digite Tmax: "))
  return N, Beta, Gama, Tmax;

# Nao altere esta funcao
def leituraParam2 () :
  N = int(input("Digite N: "))
  Gama = float(input("Digite Gama: "))
  Tmax = int(input("Digite Tmax: "))
  Beta_MIN = float(input("Digite Beta_MIN: "))
  Beta_MAX = float(input("Digite Beta_MAX: "))
  Beta_delta = float(input("Digite Beta_delta: "))
  return N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta;


def leituraParamViaArquivo (nomeArquivo) :
  # Implementar
  return None


# Nao altere as funcoes abaixo:
def imprimeLista(L) :
  for i in range(len(L)):
    print("%.4f " % L[i], end=""); # usar apenas 4 digitos apos ponto
  print()


def SIR (N, Beta, Gama, Tmax) :
  # Implementar
  return None


def critic_SIR (N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta) :
  # Implementar
  return None


# Gerar o grafico simples PGM e imprimi-lo (tela ou arquivo: imp=1 => grava arquivo "graf_simples.pgm")
def gera_grafico_simples (L, imp) :
  # Implementar
  return None


# Gerar o grafico composto PPM e imprimi-lo (tela ou arquivo: imp=1 => grava arquivo "graf_simples.pgm")
def gera_grafico_composto (S, I, R) :
  # Implementar
  return None


# Opcoes
# 1: Calcular 'SIR' e imprimir os vetores S, I e R - leitura de teclado
# 2: Calcular 'critic_SIR' e imprimir o vetor c_SIR - leitura de teclado
# 3: Calcular 'critic_SIR' e imprimir o vetor c_SIR - leitura de arquivo
# 4: Calcular 'critic_SIR', testar matriz devolvida por 'gera_grafico_simples' - leitura de teclado
# 5: Calcular 'critic_SIR', testar arquivo PGM no disco por 'gera_grafico_simples' - leitura de teclado
# 6: Calcular 'SIR', testar matriz devolvida por 'gera_grafico_composto' - leitura de teclado
# 7: Calcular 'SIR', testar arquivo PPM no disco por 'gera_grafico_composto' - leitura de teclado

# Nao altere esta funcao
def main () :
  Opt = int(input("Digite modo do programa: "))
  if (Opt == 1) : # saida - SIR; entrada - teclado
    N, Beta, Gama, Tmax = leituraParam1();
    S,I,R = SIR(N, Beta, Gama, Tmax)
    print("S = ", end="")
    imprimeLista(S)
    print("I = ", end="")
    imprimeLista(I)
    print("R = ", end="")
    imprimeLista(R)
  elif (Opt == 2) : # saida - critic_SIR; entrada - teclado
    N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta = leituraParam2();
    c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
    imprimeLista(c_SIR)
  elif (Opt == 3) : # saida - critic_SIR; entrada - arquivo
    Dados = raw_input("Digite nome do arquivo: "); # no Python 2 precisa ser 'raw_input' para ler string
    N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta = leituraParamViaArquivo(Dados)
    c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
    imprimeLista(c_SIR)
  elif (Opt == 4) : # grafico simples - critic_SIR; entrada - teclado
    N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta = leituraParam2();
    c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
    M_grafico = gera_grafico_simples(c_SIR, 0)
    print(M_grafico)
  elif (Opt == 5) : # PGM - grafico simples - critic_SIR; entrada - teclado
    N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta = leituraParam2();
    c_SIR = critic_SIR(N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta)
    M_grafico = gera_grafico_simples(c_SIR, 1)
    g = open("graf_simples.pgm", "r")
    print(g.read())
    g.close()
  elif (Opt == 6) : # grafico composto - SIR; entrada - teclado
    N, Beta, Gama, Tmax = leituraParam1();
    S,I,R = SIR(N, Beta, Gama, Tmax)
    M_grafico = gera_grafico_composto(S, I, R)
    print(M_grafico)
  elif (Opt == 7) : # PPM - grafico composto - SIR; entrada - teclado
    N, Beta, Gama, Tmax = leituraParam1();
    S,I,R = SIR(N, Beta, Gama, Tmax)
    M_grafico = gera_grafico_composto(S, I, R)
    g = open("graf_composto.ppm", "r")
    print(g.read())
    g.close()

main()
