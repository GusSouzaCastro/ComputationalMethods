n= float(input("Vamos descobrir se seu número é triangular:"))
a=1
b=a+1
c=b+1
while n!=a*b*c and c<n/3:
  a+=1
  b=a+1
  c=b+1
if n==a*b*c:
  print ("Sim, seu número é triangular, é multiplicação de %d, %d e %d" %(a,b,c))
else:
  print ("Seu número não é triangular")
