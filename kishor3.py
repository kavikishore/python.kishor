print("Governement of TamiNadu")
print("Electricity Board")
print("-------------------------------------------")
eb=input("Enter the EB-NO:")
name=input("Enter the customer name:")
pre =int(input("Reading for pervious month:"))
cur =int(input("Reading for  current month:"))
total =cur - pre
print("Total unit consumed:",total)
paid =total*5
print("Amount to be paid :RS.",paid)
