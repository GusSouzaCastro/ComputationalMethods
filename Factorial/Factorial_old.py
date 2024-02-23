import sys
n= float(input("n="))
if n<0:
  sys.exit ("Não se calcula fatorial de número negativo!")
nfat= n*(n-1)
n-=1
while n>2:
  nfat=nfat*(n-1)
  n-=1
print (nfat)
