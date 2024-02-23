'''Calculate the factorial of a given integer number'''
import sys

n= int(input("Which number do you want to know the factorial of? "))

if n<0:
  sys.exit ("We don't calculate the factorial of a negative numbers")

nfat= n*(n-1)
n-=1
while n>2:
  nfat=nfat*(n-1)
  n-=1
print (nfat)
