<h1 align="center">EP2</h1>

<h3 align="left">Objetivos</h3>
<p align="left">Neste exercício-programa, você terá que desenvolver várias funções relacionadas com raízes de polinômios. O EP exercitará conceitos de funções e listas/vetores. A tarefa será avaliada automaticamente pelo VPL (assegure-se que sua última versão esteja com nota atribuida pelo avaliador). Para isso dividimos em 7 tarefas, cada uma avaliada por um lote de testes.

Use o modelo aqui disponibilizado para codificar seu EP2. Não apague ou altere qualquer das funções ou cabeçalhos de funções disponibilizadas e nem mesmo altere ordem delas (se a função X aparece antes da Y ela deve continuar assim).
</p>

<h3 align="left">Introdução</h3>
<p align="left">Considere um polinômio p(x)=pnxn+...+p1x1+p0, com n>0 e pn>0, neste caso de grau n. Dizemos que x é uma raíz deste polinômio se p(x)=0.
</p>
<p align="left">Representação: Para armazenar o polinômio p(x), de grau n, usaremos um vetor/lista p[] com n+1 posições, sendo p[i] o coeficiente do termo de potência i de p(x) (ou seja, p[i] = pi). Na tabela abaixo apresentamos alguns polinômios e como seria sua representação vetorial.
</p>

<h3 align="left">Tarefa</h3>
<p align="left">O EP2 está dividido em sete (7) desafios, apresentados abaixo (os primeiros são mais fáceis), 
  sendo indicado o valor aproximado de cada um (proporcional ao número de testes). 
  Seu program deverá ler um inteiro inicial com o número da opção a ser testada, desde 0 até 6:</p>
<p align="left">0. Avaliar um polinômio [4 testes]. Implementar a função de nome 'avaliaPolinomio'.</p>
<p align="left">1. Fazer cópia do polinômio [4 testes]. Implementar a função de nome 'copiaPolinomio'.</p>
<p align="left">2. Obter a forma racional reduzida da um flutuante [5 testes]. Implementar a função de nome 'racionalReduzido'.</p>
<p align="left">3. Testar se é raíz [2 testes]. Implementar a função de nome 'polinomioComRaiz'.</p>
<p align="left">4. Obter o polinômio quociente por divisão na forma p(x)/(x-r) [10 testes]. Implementar a função de nome 'polinomioQuociente'.</p>
<p align="left">5. Obter a lista (canônica) das raízes de um polinômio [25 testes]. Implementar a função de nome 'listaCanonicaDeRaizes'.</p>
<p align="left">6. Obter o polinômio quociente gerado pela divisão p(x)/(x-r) [15 testes]. Implementar a função de nome 'polinomioQuocienteRacional'
</p>
<p align="left">**Não** use funções especiais que não esteja listada como permitida no EP. O EP é de caráter individual e se for detectado plágio, os envolvidos poderão ser punidos.</p>

<h3 align="left">Polinômios</h3>
<p align="left">Um polinômio de grau n pode ter até n raízes reais, por exemplo, se ele for da forma: p(x) = (x-r1)(x-r2)...(x-rn), ele terá como raízes r1, r2 até rn.
Por exemplo, o polinômio p(x) = x2-3x+2 que tem grau 2 tem as raízes 1 e 2 e isso pode ser facilmente observado se notarmos que p(x) = x2-3x+2 = (x-1)(x-2). Para esse polinômio, seu polinômio quociente q(x) por (x-r) é tal que p(x) = q(x)(x-r)+r(x). Abaixo algumas explicações adicionais sobre os itens 2 ao 6.

<p align="left"> 0.avaliaPolinomio: Esta função é essencial para assegurar que está processando corretamente os polinômios, aqui deve-se avaliar o polinômio sobre um conjunto de seis (6) valores ("aplicá-lo" sobre 6 valores a serem lidos).
Os 6 valores também devem ser lidos (via scanf em C ou input em Python), logo após a leitura dos coeficientes do polinômio.
</p> 
  
<p align="left"> 1.copiaPolinomio: Esta função é útil para outras funções (como em listaCanonicaDeRaizes). Ela para fazer cópiar/duplicar um dado polinômio (seu coeficientes).
Em C não existe outra opção a não ser implementá-la, mas o Python fornece "de graça" um modo direto que esconde a existência do laço necessário para a cópia. Assim, atenção pessoal do Python, desejamos que vocês implementem a sua função de "copia".
Nesta função deve-se usar a função fornecida polinomioToStringF para imprimir os polinômios (um com soma de uma unidade a cada coeficiente de p(x) e depois p(x) original).
</p>
  
<p align="left"> 2.racionalReduzido: A função racionalReduzido recebe como parâmetros um valor real ("ponto flutuante") e deve computar sua forma equivalente racional. A forma como devolve a resposta depende da linguagem usada, para aqueles de Python é via um comando return, enquanto que em C é via passagem por referência (isso é fácil de identificar, pois todas as funções obrigatórias tem seus cabeçalho no modelo - modelo C modelo Python).
Por exemplo: racionalReduzido(0) deve devolver a '0';
racionalReduzido(-2.0) deve devolver a '-2';
racionalReduzido(-0.6) deve devolver a '-3/5';
racionalReduzido(0.75) deve devolver a '3/4';
racionalReduzido(0.07692307692307693) deve devolver a '1/13';
</p>

<p align="left"> 3.polinomioComRaiz: A função polinomioComRaiz recebe como parâmetros um polinômio p e um real x (o número e forma dos parâmetros depende da linguagem, confira o modelo Python ou o modelo C) e deve devolver 1 se x é raíz de p (i.é., p(x)=0) ou 0 em caso contrário (i.é., p(x)!=0).
Após a leitura dos coeficientes do polinômio, sua função deve requisitar a leitura exatamente oito (8) valores reais (via scanf em C ou input em Python), para testar se são ou não raízes de p(x).
Por exemplo, para o polinômio p(x)=x2-3.5x+3:
polinomioComRaiz com coeficiente (3, -3.5, 1) e x=1.5 deve devolver 1;
polinomioComRaiz com coeficiente (3, -3.5, 1) e x=-1.5 deve devolver 0.
</p> 
  
<p align="left"> 4.polinomioQuociente: A função polinomioQuociente recebe como parâmetro um polinômio p(x) e um real r (o número e forma dos parâmetros depende da linguagem, confira o modelo Python ou o modelo C) e deve devolver (dependendo da linguagem via parâmtro) o polinômio quociente q(x) resultado da divisão de p(x) por (x-r).
Imagem ilustrativa de quociente e resto

Suponha que tem grau ao menos 1 (não é necessário verificar). Por exemplo, para os polinômios de graus 2 e 3, abaixo indicados deve devolver o que é mostrado:
    p(x)=x2-3.5x+3 dividido por (x-1.5) (logo r=1.5) deve devolver os coeficientes (-2,1), pois p(x)=x2-3.5x+3=x2-7/2x+3 e (x-2)(x-3/2)=x2-7/2x+3=p(x);
    p(x)=x3-x2+2 dividido por (x+1) (logo r=-1.0) deve devolver os coeficientes (2,-2,1), pois (x2-2x+2)(x+1) = x3-2x2+2x +x2-2x+2 = x3-x2+2 = p(x).
Note que se a divisão não for exata, então sobrará polinômio resto, como em p(x)=x3-x+1 dividido por (x+1), pois q(x)(x+1) + r(x) = (x2-x)(x+1) + 1 = x3-x + 1 = p(x).
Na opção 4, como saída dever ser impresso r e o polinômio quociente usando a função polinomioToStringF, usando o formatador %f (vide modelo). Assim, no primeiro exemplo acima (p(x)=x2-3.5x+3 dividido por (x-1.5)) deve-se imprimir: 1.500000 : 1.0000x-2.0000.
</p>

<p align="left"> 5.listaCanonicaDeRaizes: A função listaCanonicaDeRaizes recebe como parâmetros um polinômio p e deve computar e devolver de forma distinta, de acordo com a linguagem (confira o modelo Python ou o modelo C) a lista canônica de raízes inteiras de p(x). A lista canônica das raízes inteiras de um polinômio p(x), de grau n, é b1, b2,..., bn insteiros de modo que existe um polinômio q(x), de grau n-m que não tem raízes inteiras e
p(x) = q(x)(x-b1(x-b2)...(x-bn).
Para o EP2 gera a lista canônica de raízes b1, b2,..., bn em ordem crescente de valores absolutos, com as raízes negativas precedendo raízes positivas de mesmo valor absoluto.
Por exemplo, para os polinômios p(x) indicados abaixo por seus coeficientes deve devolver:
    listaCanonicaDeRaizes com coeficiente (6, -5, 1) deve devolver (2, 3);
    listaCanonicaDeRaizes com coeficiente (2, -2, 1) deve devolver nada (a forma disso depende da linguagem).
    listaCanonicaDeRaizes com coeficiente (2, 0, -1, 1) deve devolver (-1).
    listaCanonicaDeRaizes com coeficiente (0, 0, 36, 0, -13, 0, 1) deve devolver (0, 0, -2, 2, -3, 3).
Abaixo está uma justificativa para cada uma das quatro listas de raízes acima.
Polinômio	   	Lista canônica de raízes inteiras	   	Verificação
p(x)=x2-5x+6		{2, 3}		Note que p(x)=(x-2)(x-3)
p(x)=x2-2x+2		vazio		Note que p(x)=x2-2x+2 não tem raízes reais (discriminante é negativo)
p(x)=x3-x2+2		{-1}		Note que p(x)=x3-x2+2 = (x+1)(x2-2x2+2) e como visto na linha acima x2-2x2+2 não tem raíz real
p(x)=x6-13x4+36x2		{0, 0, -2, 2, -3, 3}		Note que p(x)=x x (x+2)(x-2)(x+3)(x-3)
A função listaCanonicaDeRaizes deve usar as anteriores quando necessário e devolve nada (dependendo da linguagem, vide seu modelo) se não há raízes inteiras.
Para as saídas, se o polinômio tem alguma raíz, para cada uma deve-se imprimir a raíz e testar com a função avaliaPolinomio, como ilustrado abaixo para os dois primeiros exemplos acima:
Polinômio	   	Saídas
p(x)=x2-5x+6		A(s) 2 raiz(es):
p(2.000000) = 0.000000
p(3.000000) = 0.000000	
p(x)=x2-2x+2		Sem raizes
</p>
 
<p align="left"> 6.polinomioQuocienteRacional: A função polinomioQuocienteRacional recebe como parâmetros um polinômio p, um real b e um inteiro a e deve computar (e devolver de forma distinta, de acordo com a linguagem, confira o modelo Python ou o modelo C) o polinômio q que representa o polinômio quociente q(x) e o resto da divisão r tais que p(x)=q(x)(ax-b).
Isto naturalmente pressupõe que p(x) tenha grau ao menos 1. Caso contrário, a função deve devolver -1.
Por exemplo, para os polinômios p(x) indicados abaixo por seus coeficientes deve devolver:
    polinomioQuocienteRacional com coeficiente (6, -7, 2), b=3 e a=2 deve devolver (-2.0, 1.0) e resto 0.0;
    polinomioQuocienteRacional com coeficiente (6, -7, 2), b=-3 e a=2 deve devolver (-5.0, 1.0) e resto 21.0;
    polinomioQuocienteRacional com coeficiente 4), b=2 e a=1 deve devolver (nada) e resto -1;
Na tabela abaixo ilustramos a razão das devoluções para os três exemplos acima.
p(x)	gerado por (6, -7, 2) é 2x2-7x+6, com b=3 e a=2 deve devolver (-2.0, 1.0) e resto 0.0, pois:
p(x)=2x2-7x+6 = q(x)(ax-b) + r = (x-2)(2x-3) + 0
p(x)	gerado por (6, -7, 2) é 2x2-7x+6, com b=-3 e a=2 deve devolver (-5.0, 1.0) e resto 21.0, pois:
p(x)=2x2-7x+6 = q(x)(ax-b) + r = (x-5)(2x+3) + 21
p(x)	gerado por (4) é 4, com b=2 e a=1 deve devolver (nada) e resto -1, pois:
p(x)=4 tem grau 0
Atenção não coloque comandos para leitura e nem para impressão dentro das sete (7) funções acima.
</p>
