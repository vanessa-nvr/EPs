<h1 align="center">EP1</h1>

<h3 align="left">Objetivos</h3>
<p align="left">Neste exercício-programa, você terá que desenvolver várias funções relacionadas com um modelo de simulação de contaminação por vírus. 
A função main() já está sendo fornecida pronta. Também são fornecidos os protótipos/cabeçalhos das funções a serem desenvolvidas. 
**NÂO apague e nem altere a função main()**. Não altere os protótipos/cabeçalhos das funções (isto é, nome das funções e sua relação de parâmetros). 
Você deve preencher o corpo das funções solicitadas. Funções auxiliares adicionais podem também ser escritas.
</p>

<h3 align="left">Introdução</h3>
<p align="left">O modelo SIR foi publicado em 1927 por Kermack e McKendrick (Proc. R. Soc. Lond. A, 115:700-721). 
Ele é um modelo determinístico relativamente simples utilizado até hoje para estimar a evolução de epidemias.
Em sua forma original, o modelo considera três variáveis básicas S, I e R que representam, respectivamente, indivíduos Suscetíveis mas ainda não infectados, 
indivíduos Infectados (ou seja, doentes) e indivíduos Recuperados, que são removidos do modelo (ou seja, que tiveram a doença no passado e agora não mais a transmitem 
– porque se curaram e adquiriram imunidade ou porque faleceram). 
Ele considera, ainda, uma população fixa sob análise de N indivíduos e duas constantes β e γ que representam, respectivamente, 
fatores de infecção e de recuperação característicos da doença.
Com estes parâmetros (β e γ), o modelo descreve a evolução temporal das variáveis S, I e R usando equações diferenciais codependentes:
</p>
<p align="left">Este modelo não é suficiente para descrever em detalhes a evolução de uma epidemia como, por exemplo, a de COVID-19 que estamos vivenciando. 
Ele serve, entretanto, para descrever em linhas gerais como uma epidemia evolui. Um dos grandes problemas da aplicação do modelo ao caso do COVID-19 
é que ele identifica o grupo dos infectados ao dos doentes, mas não prevê a existência dos assintomáticos: indivíduos infectados que contraem o vírus mas não desenvolvem sintomas. Vários estudos de populações bem demarcadas têm apontado que cerca de metade da população infectada adquire imunidade sem apresentar sintomas, mas em presídios norte-americanos que sofreram um teste massivo verificou-se que 96% da população já infectada era de assintomáticos 
(Daniel P. Oran, AM, Eric J. Topol, MD, Prevalence of Asymptomatic SARS-CoV-2 Infection, Annals of Internal Medicine, 3 Jun 2020).
A população e sua respectiva cardinalidade N deve considerar grupos que tenham possibilidade de contato e os parâmetros β e γ devem corresponder aos valores observados empiricamente e capazes de representar, respectivamente, quão transmissível se apresenta a doença e o tempo requerido para a recuperação de infectados. A transmissibilidade é determinada por características da doença em si e padrões de comportamento da população (distanciamento social, padrões de higiene, etc.). 
Para simular este modelo computacionalmente, pode ser construída uma versão “episódica” em que o tempo é discretizado para poder ser tratado como uma sequência de números naturais (que podem representar, por exemplo, dias). As equações nesta versão “episódica” ficam assim:
</p>
<p align="left">
Neste EP produziremos um simulador SIR episódico e extrairemos alguns dados dele.
</p>  
  
<h3 align="left">Tarefa 1</h3>
<p align="left">Construa uma função SIR(S, I, R, N, Beta, Gama, Tmax) que receba como parâmetros:

S, o vetor com os dados discretizados da função S(.)
I, o vetor com os dados discretizados da função I(.)
R, o vetor com os dados discretizados da função R(.)
N, o tamanho da população (int)
Beta, o parâmetro correspondente a quão transmissível é a doença (float)
Gama, o parâmetro correspondente ao tempo necessário para se recuperar da doença (float)
Tmax, o valor máximo para a variável tempo a ser considerado nas simulações (int)
Esta função deverá devolver como resposta três listas contendo Tmax elementos, correspondendo respectivamente às variáveis S, I e R em cada instante de tempo da lista 0, 1, 2, ..., ( Tmax-1).
</p>

<h3 align="left">Tarefa 2</h3>
<p align="left">Construa uma função critic_SIR(cSIR, S, I, R, N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta) que receba como parâmetros:

N, Gama e Tmax como na Tarefa 1

Beta_MIN, Beta_MAX e Beta_delta (float) para representar o intervalo de valores
B={βMIN, βMIN+Δ, βMIN+2Δ, ..., βMAX}, sendo Beta_MIN=βMIN, Beta_MAX=βMAX e Beta_delta=Δ.

Esta função deverá devolver como resposta uma lista representando, para cada valor de β dentro do intervalo B, o valor máximo da variável I produzido pela função da Tarefa 1.

Exemplo de chamada da função critic_SIR  com saídas correspondentes esperadas: 

- critic_SIR(cSIR, S, I, R, 10, 0.1, 10, 0.05, 0.50, 0.05)
- imprimeLista(cSIR, 10)  --- função fornecida pronta no EP3.py
1.0000  1.0000  1.2663  1.7439  2.3103  2.9424  3.6023  4.2421  4.8139  5.2803 


Nas duas próximas tarefas utilizaremos os formatos PGM e PPM para produção de gráficos para apresentar visualmente resultados numéricos. Uma descrição detalhada destes formatos de arquivo, que são utilizados para o armazenamento de imagens, pode ser encontrada no seguinte link: https://www.ime.usp.br/~mac2166/ep3-2020/pgm_ppm.pdf
</p>

<h3 align="left">Tarefa 3</h3>
<p align="left">Construa uma função gera_grafico_simples(L) que receba como parâmetro uma lista L de valores (float) e construa um gráfico X-Y em que o eixo Y tenha como limite inferior o valor Y_MIN=0 e como limite superior o inteiro Y_MAX definido pelo teto do valor máximo encontrado em L, e o eixo X tenha como limite inferior o valor X_MIN=0 e como limite superior X_MAX a quantidade de elementos de L menos um. Este gráfico deve apresentar uma representação dos valores em L. O gráfico corresponderá a uma matriz M de dimensão m x n, sendo o número de linhas dado por m = Y_MAX-Y_MIN+1 e o número de colunas dado por n = X_MAX-X_MIN+1=len(L). Os valores da matriz devem ser padronizados como 255 (branco) para pontos que representem os valores contidos na lista L e 0 (preto) para os demais pontos na imagem. Ou seja, cada ponto (x,y) = (k,L[k]) deverá ser registrado em uma posição M[i][j] da matriz, sendo o índice i obtido por arredondamento de Y_MAX-L[k] para o inteiro mais próximo e x=k=j. Além de devolver a matriz resultante, a função deverá gravar o gráfico gerado na matriz M em um arquivo no formato PGM, com o nome padronizado “graf_simples.pgm”.

Exemplo de chamada da função gera_grafico_simples com saídas correspondentes esperadas: 

- critic_SIR(cSIR, S, I, R, 10, 0.1, 10, 0.05, 0.50, 0.05)
- gera_grafico_simples(cSIR, 10)
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 255, 255], [0, 0, 0, 0, 0, 0, 255, 255, 0, 0], [0, 0, 0, 0, 0, 255, 0, 0, 0, 0], [0, 0, 0, 255, 255, 0, 0, 0, 0, 0], [255, 255, 255, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
Abaixo é exibido o conteúdo do arquivo PGM correspondente “graf_simples.pgm”:
Para visualizar a imagem "graf_simples.pgm", você deve rodar seu programa diretamente no seu computador. No VPL não é possível visualizar as imagens.  Para visualizar a imagem, você deve abrir o arquivo "graf_simples.pgm" resultante com algum programa de edição/visualização de imagens, que entenda o formato PGM.  Abaixo é mostrado um exemplo de visualização no Gimp, usando critic_SIR(cSIR, S,I,R, 100, 0.2, 100, 0.05, 0.90, 0.05)  e depois gera_grafico_simples(cSIR).
</p>  

<h3 align="left">Tarefa 4</h3>
<p align="left">Construa uma função gera_grafico_composto(S,I,R) que receba como parâmetros três listas de valores (float) e construa um gráfico X-Y em que o eixo Y tenha como limite inferior o valor Y_MIN=0 e como limite superior o inteiro Y_MAX definido pelo teto do valor máximo encontrado em S∪I∪R, e o eixo X tenha como limite inferior o valor X_MIN=0 e como limite superior X_MAX a quantidade de colunas de S menos um. Este gráfico deve apresentar uma representação dos valores em S, I e R, em formato de linhas superpostas com cores distintas. O gráfico deverá ser registrado em um arquivo no formato PPM, com o nome padronizado “graf_composto.ppm”. A função deverá, também, devolver como resposta o conteúdo do arquivo PPM no formato de uma matriz de valores inteiros. Estes valores devem ser também padronizados como:

“255 0 0” (vermelho) para pontos que representem os valores contidos na lista correspondente aos valores de S, 
“0 255 0” (verde) para pontos que representem os valores contidos na lista correspondente aos valores de I, 
“0 0 255” (azul) para pontos que representem os valores contidos na lista correspondente aos valores de R e
“0 0 0” (preto) para os demais pontos na imagem.
No caso de sobreposição das curvas, as cores devem ser somadas (exemplo, sobreposição de S e I gera cor “255 255 0” (amarelo)).
Exemplo de chamada da função gera_grafico_composto com saídas correspondentes esperadas: 

- SIR(S,I,R, 10, 0.5, 0.1, 4)
- gera_grafico_composto(S, I, R, 10)
[[255, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 255, 0], [0, 255, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0], [0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255]]
Abaixo é exibido o conteúdo do arquivo PPM correspondente “graf_composto.ppm”:

Para visualizar a imagem "graf_composto.ppm", você deve rodar seu programa em Python diretamente no seu computador. No VPL não é possível visualizar as imagens. Para visualizar a imagem, você deve abrir o arquivo "graf_composto.ppm" resultante com algum programa de edição/visualização de imagens, com suporte para o formato PPM. Abaixo é mostrado um exemplo de visualização no Gimp, usando SIR(S,I,R, 100, 0.5, 0.2, 100) e depois gera_grafico_composto(S, I, R, 100).
</p>

<h3 align="left">Tarefa 5</h3>
<p align="left">Construa uma função leitura_de_valores(nome_de_arquivo ...) (em Python pode devolver N, Gama,Tmax, Beta_MIN, Beta_MAX, Beta_delta e em C deve passar todos via referência) que receba como parâmetro um nome de arquivo e retorne valores para as seguintes variáveis: N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta, que deverão ser lidas de um arquivo texto com o nome indicado em nome_de_arquivo. O arquivo texto deve ter um valor para cada uma das variáveis de retorno. Os valores devem ser fornecidos um em cada linha e devem ser transformados para o tipo de dados apropriado (int ou float, dependendo da variável). A função leitura_de_valores(nome_de_arquivo ...) é chamada pela função main() do seguinte modo:
Python: N, Gama, Tmax, Beta_MIN, Beta_MAX, Beta_delta = leitura_de_valores(Dados)

C: leitura_de_valores(Dados, &N, &Gama, &Tmax, &Beta_MIN, &Beta_MAX, &Beta_delta)

Exemplos de arquivos de entrada podem ser vistos nas abas "dados1.txt", "dados2.txt", "dados3.txt", "dados4.txt" e "dados5.txt". Não edite esses arquivos, pois eles serão usados nos testes automáticos do VPL.
</p>

<h3 align="left">Programa principal:</h3>
<p align="left">A função main() está sendo fornecida pronta e não deve ser alterada. Ela possui 7 modos de operação diferentes, visando testar as diferentes partes do seu programa. Os modos são:
</p>
<p align="left">1. Calcula 'SIR' e imprime os vetores S, I e R - leitura dos parâmetros via teclado.</p>
<p align="left">2. Calcula 'critic_SIR' e imprimir o vetor resultante - leitura dos parâmetros via teclado.</p>
<p align="left">3. Calcula 'critic_SIR' e imprimir o vetor resultante - leitura dos parâmetros de um arquivo fornecido.</p>
<p align="left">4. Calcula 'critic_SIR' e testa matriz devolvida por 'gera_grafico_simples' - leitura dos parâmetros via teclado.</p>
<p align="left">5. Calcula 'critic_SIR' e testa arquivo PGM no disco por 'gera_grafico_simples' - leitura dos parâmetros via teclado.</p>
<p align="left">6. Calcula 'SIR' e testa matriz devolvida por 'gera_grafico_composto' - leitura dos parâmetros via teclado.</p>
<p align="left">7. Calcula 'SIR' e testa arquivo PPM no disco por 'gera_grafico_composto' - leitura dos parâmetros via teclado.</p>
