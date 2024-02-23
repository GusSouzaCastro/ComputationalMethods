import sys
print("Checking if a given point belongs to the H region, H being the quarter circle in the first quadrant i.e., the region x²+y²<=1.")
x= float(input("Type the x coordinate (a positive value) of the point: "))
if x<0:
  sys.exit ("Remember: x must be >0. Run the program again.")
y= float(input("Type the y coordinate (a positive value) of the point: "))
if y<0:
  sys.exit ("Remember: y must be >0. Run the program again.")
if x**2+y**2<=1:
  print ("Yes, your point (%f,%f) belongs to the H region :)" %(x,y))
else:
  print ("Unfortunately your point does not belong to the H region :(" %(x,y))
