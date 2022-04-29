#assignment 3
h=(float(input("Enter the regular hours: ")))
o=(float(input("Enter the overtime hours: ")))
w=(float(input("Enter the wage: ")))
pay = h*w
ot = o*w*1.5
oPay= pay+ot
print("The total weekly pay is: ", oPay)
