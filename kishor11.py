print("takshashila university")
print("ongur,tindivanam")
print("-----0-------0-----")
print("student mark list")
print("-----0-------0-----")
no1=int(input("enter the python mark:"))
no2=int(input("enter the DBMS mark:"))
no3=int(input("enter the industry mark:"))
totalmark=no1+no2+no3
print("total mark:",totalmark)
agmark=totalmark/3
print("avarage mark:",agmark)
if(no1>=40 and no2>=40 and no3>=40):
    print("result:pass")
else:
    ("result:fail")
if(totalmark>=250):
    print("grade:O grade")
elif(totalmark>200):
    print("grade:A+ grade")
elif(totalmark>=150):
    print("grade:A grade")
else:
    print("grade:B grade")
