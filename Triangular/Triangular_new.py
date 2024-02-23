'''Program to find of if a given number is triangular i.e. it is the sum of subsequent numbers from 0'''
'''Note that for some reason I did not use the usual definition of what a triangular number is for the "old" version, instead being "A number that is the product of any three subsequent numbers"'''
n= int(input("Let's figure out if your number is triangular: "))

a=0
cont=1
while a<n:
  a+=cont
  cont+=1

if a==n:
  print ("Yes, your number is triangular, in fact, it is the %dth one." %(cont))
else:
  print ("Your number is not triangular.")
