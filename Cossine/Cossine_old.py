from math import factorial, cos,pi
n= [0,1,2]
x= [pi/6, pi/3]
for y in x: #ao invés de repetir todo o código para "pi/3", foi criada outra
 cosseno=0 #lista com os valores, acreditando que isso seria mais otimizado
 for N in n:
  cosseno+= (((-1)**N)/factorial(2*N))*y**(2*N)
  '''comparativamente, os resultados são parecidos, só não idênticos
  pois a expansão só segue até o índice 2,
  isso pode ser conferido pondo valores consecutivos na linha de "n="'''
 print ("Cosseno calculado:", cosseno)
 print ("Cosseno segundo função:", cos(y))
