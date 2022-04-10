from __future__ import print_function;
# FUNCOES OBRIGATORIAS PRONTAS
def listaCoeficientes (p) :
  np = len(p);
  print("[ ", end="");
  for i in range(np) :
    print("%f, " % p[i], end="");
  print(" ]");
  
def sig (nTermAnte,coef) :
  if (nTermAnte > 0 and coef >= 0) :
    return "+"
  else:
    return ""

def polinomioToStringF (p) :
  if (p is None) : return "";
  tam = len(p)-1
  expressao = ""
  for m in range(tam-1):
    if (p[tam-m] != 0) :
      expressao = "%s%s%.4fx^%d" % (expressao, sig(m,p[tam-m]), p[tam-m], tam-m);
  if (tam>0 and p[1] != 0) :
    expressao = "%s%s%.4fx" % (expressao, sig(tam-1,p[1]), p[1])
  if (p[0] != 0) :
    expressao = "%s%s%.4f" % (expressao, sig(tam,p[0]), p[0])
  return expressao

def encontraInteiro (parteFlut) :
  potA = 1;
  if (parteFlut<0) :
    parteFlut = -parteFlut;
  while (parteFlut-int(parteFlut) > 0) :
    potA *= 10;
    parteFlut *= 10;
  return [potA, int(parteFlut)];


# FUNCOES ADICIONAIS

def mdc(b, a):
  while a!= 0:
    c=a
    a=b%a
    b=c
  return b

def remove_rep(p):
  lista=[]
  for i in p:
    if i not in lista:
      lista.append(i)
  lista.sort()
  return lista
  
# FIM DO BLOCO DE FUNCOES ADICIONAIS

# FUNCOES OBRIGATORIAS

def avaliaPolinomio (p,x) :
  soma=0.0
  tp=len(p)
  expoente=0
  for i in range(tp):
    soma+=p[i]*(x**(expoente))
    expoente+=1
  return (soma)

def copiaPolinomio (p1, p2) :
  tp=len(p)
  for i in range(tp):
      p1[i]=p[i]+1
      p2[i]=p[i]
  return p1,p2

def reduzRacional (b, a) :
  maxdivcomum=mdc(b,a)
  b//=maxdivcomum
  a//=maxdivcomum
  
  if a!=1:
    return str(b)+"/"+ str(a)
  else:
    return str(b)

def racionalReduzido (r) :
  parteFlut=r
  x=encontraInteiro(parteFlut)
  b=x[1]
  a=x[0]
  if r<0:
    return (reduzRacional (-b, a))
  else:
    return (reduzRacional (b, a))

def polinomioComRaiz (p,b) :
  x=b
  if avaliaPolinomio (p,x)==0:
    return 1
  else:
    return 0

def polinomioQuociente (p,b):
  cdividendo=list(p)
  n=b[0]
  for i in range(len(p)-(len(b)-1)):
    cdividendo[i]/=n
    coeficiente=cdividendo[i]
    if coeficiente != 0:
      for j in range(1, len(b)):
        cdividendo[i+j] += -b[j]*coeficiente
  rest=-(len(b)-1)
  quociente=cdividendo[:rest]
  resto=cdividendo[rest:]
  return quociente, resto

def listaCanonicaDeRaizes (p):
  raizes=[]
  for (x,z) in zip(range(0,-1000,-1),range(999)):
      polinomio=avaliaPolinomio(p,x)
      ppolinomio=avaliaPolinomio(p,z)
      if polinomio==0.000000:
          raizes.append(x)
      if ppolinomio==0.000000:
          raizes.append(z)
  return raizes

def polinomioQuocienteRacional (p,b,a) :
  x=[b*(-1),a]
  resul=polinomioQuociente (p,x)
  return resul

# FIM DO BLOCO DE FUNCOES OBRIGATORIAS

# INICIO DO BLOCO DE FUNCOESPARA EXECUTAR CADA OPCAO
opcao=int(input("Digite opcao: "))
if opcao==0 or opcao==1 or opcao==3 or opcao==5 or opcao==6:
  grau=int(input("Digite o grau: "))
  cgrau=grau+1
if opcao==0 or opcao==1 or opcao==3 or opcao==5 or opcao==6:
  p = [float(p) for p in raw_input("Digite os %s coeficientes: " %(grau+1)).split()]  

def opcao0():
  valores=[float(v) for v in raw_input("Digite os 6 valores: ").split()]
  resultados=[]
  for i in range(len(valores)):
    x=avaliaPolinomio (p,valores[i])
    resultados.append(x)
  for j in range(len(valores)):
    print ("p(%.6f) = %.6f" % (valores[j],resultados[j]))

def opcao1():
  p1=p[:]
  p2=p[:]
  copiaPolinomio (p1, p2)
  print("p+1=",polinomioToStringF (p1))
  print("p=",polinomioToStringF (p2))

def opcao2():
  v=[float(v) for v in raw_input("Digite os 5 valores: ").split()]
  for i in range(5):
    print(racionalReduzido (v[i]))
    
def opcao3():
  v=[float(v) for v in raw_input("Digite os 8 valores: ").split()]
  op3=[]
  for i in range(len(v)):
    x=polinomioComRaiz (p,v[i])
    op3.append(x)
  for j in range(len(v)):
    print ("p(%.6f) = %s" % (v[j],op3[j]))

def opcao4():
  entrada=[float(v) for v in raw_input("\nDigite o grau:").split()]
  t=len(entrada)
  v=entrada[t-1]
  if v==0:
    x=[v,1]
  else:
    x=[v*(-1),1]
  pol=[]
  for i in range(1,t-1):
    pol.append(entrada[i])  
  resultado=polinomioQuociente (pol,x)
  qx=resultado[0]
  print("\nDigite os %s coeficientes: Digite uma raiz r para fatorar por (x-r):%.6f : %s" % ((int(entrada[0]+1)), v, polinomioToStringF (qx)))
    
def opcao5():
  a=listaCanonicaDeRaizes (p)
  b=remove_rep(a)
  t=len(b)
  if t>0:
    print("A(s) %s raiz(es):"% (t)) 
    for i in range(t):
      print("p(%.6f) = 0.000000" % (b[i]))
  else:
    print("Sem raizes")

def opcao6():
  v=[float(v) for v in raw_input("Digite a e b: ").split()]
  a=v[0]
  b=v[1] 
  resultado=polinomioQuocienteRacional (p,b,a)
  qx=resultado[0]
  resto=resultado[1]
  print("r=%.6f : " % (resto[0]),end="")
  listaCoeficientes (qx)      
  
    
# FIM DO BLOCO DE FUNCOES PARA EXECUTAR CADA OPCAO
# FUNCAO MAIN
def main () :
  if opcao==0:
    opcao0()
  if opcao==1:
    opcao1()
  if opcao==2:
    opcao2()
  if opcao==3:
    opcao3()
  if opcao==4:
    opcao4()
  if opcao==5:
    opcao5()
  if opcao==6:
    opcao6()
    
# FIM DA FUNCAO MAIN

# CHAMADA DA FUNCAO MAIN
if __name__ == "__main__":
  main()
# FIM DO BLOCO DE CHAMADA DA FUNCAO MAIN
