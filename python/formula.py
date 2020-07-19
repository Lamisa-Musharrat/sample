a=float(input())
b=float(input())
c=float(input())
x=((-b+((b**2)-(4*a*c))**(1/2))/2*a)
y=((-b-((b**2)-(4*a*c))**(1/2))/2*a)
  print("R1 =%.4f"%x)
  print("R2 =%.4f"%y)
else:
  print("Impossivel calcular")  
