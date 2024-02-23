'''I believe the point of this exercice was to utilize the "while" loop, so I'm keeping it that way'''
print("From -20°C to 40°C in °F in increments of 5°C")
C=-20
while C<=40:
  F=((9*C)/5)+32
  print("For %f°C, we have %f °F" %(C,F))
  C+=5
