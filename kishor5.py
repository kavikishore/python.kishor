print("kishor international [p] ltd.")
print("NO.15,nagapara dist, banglore")
print("------------------------------")
print("Employee payroll system")
print("------------------------------")
ID =int(input("enter the Employee ID:"))
name =input("enter the Employee name:")
salary =int(input("enter the salary:"))
print("income")
bonus =salary *20/100
print("bonus(20percentage);",bonus)
overtime =salary *10/100
print("overtime (10 percentage):",7)
TA =salary *5/100
print("travel allowance(5percentage):",TA)
gpay=salary+bonus+overtime+TA
print("grosspay in rupees:",gpay)
