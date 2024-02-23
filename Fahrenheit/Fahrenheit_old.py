print("De -20°C até 40°C em °F")
C=-20
while C<=40:
  F=((9*C)/5)+32
  print("Para %f, equivalente em °F: %f" %(C,F))
  C+=5
