import sys
print("Conferindo se um ponto pertence ao 1/4 de cícrulo: x²+y²<=1. Tal área será nomeada H")
x= float(input("Digite a coordenada x do ponto, certamente o valor deve ser positivo:"))
if x<0:
  sys.exit ("Seu valor deve ser positivo, tente de novo!")
y= float(input("Digite a coordenada y do ponto, certamente o valor deve ser positivo:"))
if y<0:
  sys.exit ("Seu valor deve ser positivo, tente de novo!")
if x**2+y**2<=1:
  print ("Sim, o seu ponto (%f,%f) pertence a área H :)" %(x,y))
else:
  print ("Infelizmente seu ponto (%f,%f) não pertence a área H :(" %(x,y))
