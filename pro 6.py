a=int(input("Enter the first side of triangle:\n"))
b=int(input("Enter the second side of triangle:\n"))
c=int(input("Enter the third side of triangle:\n"))
if a>=c+b:
  print("no")
elif b>=a+c:
  print("no")
elif c>=a+b:
  print("no")  
else:
  print("yes")  