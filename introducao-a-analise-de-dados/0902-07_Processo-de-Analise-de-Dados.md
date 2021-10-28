### Capitulo 9 - Video 4
#### PREPARAÇÃO E EXPLORAÇÃO DE DADOS:

__Identificação das variaveis:__

- Precisa-se definir as variaveis de saida e entrada, definir os tipos de dados e categorias das variaves.
- As variaveis são as colunas em um dataframe, as colunas em uma planilha excel, em uma tabela em um banco de dados, por exemplo.
- É comum que as variaveis estejam mal distribuidas, uma mesma variavel pode estar espalhada por mais de uma coluna e os dados, em formatos diferentes.

__Tratamento de valores missing:__

- São os valores que não estão presentes em determinadas linhas e colunas.
- Podem reduzir o poder dos modelos preditivos e isso pode levar a resultados distorcidos.
- Esses valores podem ser um problema na fonte de dados ou um problema durante o processo de extração e coleta dos dados.
- É importante observar se há um padrão para os valores missing e se eles foram gerados de forma aleatoria ou não.
- Para o tratamento, existem diversas tecnicas, podemos simplesmente remover a linha onde o valor missing aparece ou podemos remover pares de linhas, dependendo da relação entre as variaveis. Cada metodo terá vantagens e desvantagens.
- Durante o processo de extração e coleta, tambem podemos acabar, acidentalmente, gerando valores missing por fazendo a união de diferentes dados.

__Tratamento de outliers:__

- São valores que são muito diferentes da média dos valores, é uma observação que está muito distante do padrão observado naquele conjunto de dados.
- Há os outliers univariados e multivariados.
- Podem ser causados por entrada errada de dados, erros de experimento, podem ser intencionais, mas seja qual for a causa, terão impacto na analise. Podemos removê-los, tratá-los separadamente ou transformá-los.
- Exemplo:
  - Uma operadora de cartão de credito está criando um modelo preditivo para prever possiveis fraudes, nesse tipo de aplicação, a empresa coleta varias transações de cartão de credito e ela percebe, por exemplo, que o usuario gasta, em média, R$100,00 em compras no final de semana, se em determinado momento, esse usuario gastar em média R$8.000,00 reais, isso é um outlier. Esse valor não é padrão.
- Independentemente de qual seja a razão pela criação do outlier, ele deve ser avaliado e alguma ação deve ser tomada.
- Em algumas situações, os outliers devem ser removidos do conjunto de dados, ou seja, não existe uma única técnica que resolva todos os problemas, vai sempre depender do problema que eu estou tentando resolver.

__Tranformação de variaveis:__

- Nesta fase, podemos mudar a escala de uma variável, transformar relacionamentos nao lineares complexos em relacionamentos lineares simples, mudar a simetria da sua distribuição de dados, entre outras opções.
- Muitas escolhas terão que ser feitas e essas escolhas podem influenciar no processo de analise e no resultado final.
- Eu posso ter uma variável distribuida em mais de uma coluna, a variável nesse caso representando uma informação.
- Então imagine por exemplo, a data, eu quero trabalhar com a data de nascimento e temos uma coluna com dia, uma coluna com mês e uma coluna com ano. Podemos concatenar essas três colunas e crio uma quarta coluna chamada DataDeNascimento, ou tambem pode se fazer o contrário.

__Criação de variaveis:__

- Depois que os dados estiverem coletados e explorados, provavelmente isso pode acontecer, nós vamos sentir falta de mais dados que ajudem a gerar relacionamentos ou então definir melhor determinada análise.
- Nesse momento, pode ser necessário criar variáveis, seja transformando variáveis existentes e então gerando uma nova variável, ou a partir da transformação de outras variáveis, ou ainda coletando mais dados. 
- É possivel ainda, aplicar funções às variáveis existentes e o resultado dessa função, gerar uma nova variável.

#### CRIAÇÃO DO MODELO:

- Este modelo ajuda a explicar o relacionamento entre as variáveis e fazer as previsões.
- Primeiro devemos escolher um dos mais de 60 algoritmos de Machine Learning.
- Na sequência, os dados devem ser subdivididos em dados de treino e dados teste, nós vamos praticar isso ao longo dos próximos capítulos e então, realizamos um trabalho iterativo, um trabalho de repetição.
- Acontece a avaliação e o teste do modelo vendo se a precisão está adequada ou não, se não estiver, retornamos, modificamos os dados, alteramos os parâmetros do algoritmo, treinamos de novo, testamos e avaliamos. Esse ciclo vai se repetir algumas vezes.

#### AUTOMATIZAÇÃO DO PROCESSO:

- É fazer com que o modelo fique autonomo, de modo que, ao receber novos conjuntos de dados, seu processo possa ser executado de uma unica vez, de preferencia, sem a interferencia do cientista de dados.
- É nessa fase que nós pensamos como transformar o processo de analise em um produto ou serviço que poderá ser publicado através de um site de compras. Também podemos criar uma aplicação web ou um app para smartphone.

#### APRESENTAÇÃO DO RESULTADO:

- Nesta fase, a habilidade de contar a historia que os dados querem dizer pode ser aplicada. É preciso resumir varios registros em historias que ajudem a contar aquilo que os dados estão querendo dizer.
- É importante resaltar que as visualizações de dados podem ser usadas durante todas as fases do processo, de forma, que ao fim você tenha uma foto clara de como o processo evoluiu.