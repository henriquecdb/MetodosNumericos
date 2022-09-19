## Implementação
Durante a implementação, com o propósito de organizar o desenvolvimento, optamos por separar o arquivo *main* do arquivo *metodos* com as funções. A linguagem escolhida foi o Python e duas funções adicionais, além dos métodos, foram implementadas para representar a função e sua derivada.
## Falsa Posição e Método de Newton
Os métodos numéricos escolhidos para desenvolver o trabalho foram o Método da Falsa Posição e o Método de Newton.

Com o objetivo de calcular a $\sqrt[4]{78}$, foi escolhida a função $f(x) = x^4 – 78$. Para o método da Falsa Posição, usamos o intervalo $[2,3]$, $\epsilon$ $=0.004$ e $7$ como valor para a iteração máxima. A função retorna o valor de $x$, precisão e valor de $k$.
	
```python:
def  falsa_posicao(a,  b,  tol,  kmax):
...
return  x, er, k
```

Já para o Método de Newton os valores $xo$ $=3$, $\epsilon$ $=0.004$ e $7$ respectivamente como valor de aproximação inicial, precisão e iterações máximas. Como resultado, a função retornou $(2.971824269146067, 8.45790763543817e-05, 3)$ para o primeiro método após $3$ iterações, enquanto que no segundo método a função retornou $(2.9718279446789486, 8.239094412942904e-06, 2)$ após $2$ iterações, mostrando assim, uma eficácia maior para o Método de Newton.

```python:
def  newton(xo,  tol,  itmax):
...
return  xo, f(xo), it
```

Com base na fórmula de erro absoluto $Ea$ $=|A-a|$, onde $A$ é o valor exato e $a$ é o valor aproximado. Com isso, pode-se observar que o Método de Newton tem $Ea=7,84781071e-8$ , enquanto o Método da Falsa posição tem $Ea=0,0000035970547745$. Sendo assim, nota-se que o primeiro erro é menor e com isso tem possivelmente maior confiabilidade.

Já para os erros relativos, usamos $Er=Ea/A \times 100$. Para o primeiro método, encontramos $0.000121038463075\%$ e $2.64073528674e-06\%$ para o segundo.