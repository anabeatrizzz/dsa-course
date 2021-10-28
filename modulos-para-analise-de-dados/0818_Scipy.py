from scipy import misc
from scipy.fftpack import *
from scipy import optimize
from scipy import stats
from scipy.integrate import quad, dblquad, tplquad
from scipy.integrate import odeint, ode
import matplotlib.pyplot as plt
from numpy import *
from pylab import *

# ----- Processamento de imagens -----
# Lendo uma imagem como array.
# plt.imread('Matplotlib-Mapa.png')

# ----- Integracao Numerica -----
# quad(funcao, limite inferior, limite superior). Computa um integral definido
# exp(array). Calcula o exponencial de todos os elementos da array
val = quad(lambda x: exp(-x ** 2),  Inf, Inf)

def dy(y, t, zeta, w0):
  x, p = y[0], y[1]

  dx = p
  dp = -2 * zeta * w0 * p - w0**2 * x

  return [dx, dp]


y0 = [1.0, 0.0]

# 1000 amostras de numeros de 0 até 9
t = linspace(0, 10, 1000)
w0 = 2 * pi *1.0

# O odeint integra um sistema de equações diferenciais ordinárias.
# odeint(funcao, array, array, args=(argumentos_extras))
y1 = odeint(dy, y0, t, args=(0.0, w0))
y2 = odeint(dy, y0, t, args=(0.2, w0))
y3 = odeint(dy, y0, t, args=(1.0, w0))
y4 = odeint(dy, y0, t, args=(5.0, w0))

# Criando figura
fig, ax = subplots()

# Traçando pontos:
# plot(valores_para_x, valores_para_y, cor, rótlo, comprimento_da_linha)
ax.plot(t, y1[:,0], 'k', label="Não Abafado", linewidth=0.25)
ax.plot(t, y2[:,0], 'r', label="Pouco Abafado")
ax.plot(t, y3[:,0], 'b', label="Criticamente Abafado")
ax.plot(t, y4[:,0], 'g', label="Perigosamente Abafado")
# Adicionando legenda:
ax.legend();

# ----- Fourier Transformation -----
# Variavel que recebe a quantidade de elementos em t
N = len(t)

# Variavel que recebe o elemento na posição 1 menos o elemento na posicão 0
dt = t[1]-t[0]

# fft retorna a transformação de Fourier discreta de sequência real ou complexa.
# fft(array)
F = fft(y2[:,0])

# fftfreq retorna as frequências da amostra transformada com Fourier Discrete.
w = fftfreq(N, dt)

fig, ax = subplots(figsize=(9,3))
# plot(valores_para_x, valores_para_y)
# abs() faz o valor absoluto de F
ax.plot(w, abs(F));

# ----- Álgebra Linear -----
# Criando uma matriz com o metodo array() do numpy
A = array([[1,2,3], [4,5,6], [7,8,9]])

# Criando um vetor com o metodo array() do numpy
b = array([1,2,3])

# O metodo solve() resolve uma equação de matriz linear ou sistema de equações escalares lineares.
x = solve(A, b)

# O metodo rand() faz uma matriz 3x3 com numeros aleatorios
A = rand(3,3)
B = rand(3,3)

# O metodo eig() calcula os valores próprios e os vetores próprios direitos de uma matriz quadrada.
evals, evecs = eig(A)
print(evals)
print(evecs)

# svd significa Decomposição de Valor Singular
# svd(array)
print(svd(A))

# ----- Otimização -----
def f(x): # Função que recebe um parametro
    return 4*x**3 + (x-2)**2 + x**4 # E retorna essa conta, substituindo x

# Criando uma figura
fig, ax  = subplots()

# x recebe 100 amostras de numeros de -5 até 3
x = linspace(-5, 3, 100)

# Traçando os valores de x e dos valores da conta que está dentro da função f
ax.plot(x, f(x));

# O metodo fmin_bfgs() minimiza uma função usando o algoritmo BFGS
# Quando se consegue construir modelos matemáticos, é possível aplicar as técnicas matemáticas
# de otimização para maximizar ou minimizar uma função previamente definida como índice de desempenho (ID)
# visando encontrar uma "solução ótima" do problema, isto é, que resulte no melhor desempenho possível do sistema,
# segundo este critério de desempenho previamente definido (ID)
x_min = optimize.fmin_bfgs(f, -0.5)
print(x_min)

# ----- Estatistica -----
Y = stats.norm()

# Criando 100 amostras de -5 até 5
x = linspace(-5,5,100)

# subplots(nr_linhas, nr_colunas, )
# sharex: Controla o compartilhamento de propriedades entre os eixos x ou y.
# Se true, eixos x ou y serão compartilhados entre todos os subplots
fig, axes = subplots(3,1, sharex=True)

# plot()
# pdf() significa Função Densidade de Probabilidade
# cdf() significa Função de Distribuição Cumulativa
axes[0].plot(x, Y.pdf(x))
axes[1].plot(x, Y.cdf(x));

# Fazendo um histograma.
# rvs() retorna variáveis aleatórias de determinado tamanho
axes[2].hist(Y.rvs(size=1000), bins=50);
