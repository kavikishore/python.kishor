print("kishor computer mart")

print ("mariyyaman street, melpettai post")

print(".........................")

print("      Bill reciept")

print(".........................")

no=int (input("Enter the item no:"))
prt=input("Enter the particular:")
rate=int(input ("Enter the rate:"))
qty=int (input("Enter the quantity:"))
total=rate*qty
print("Total amount is rupees", total)
if (total>=100000):
    gst=total*10/100
elif (total>=50000):
     gst=toatl*5/100
elif (total>=30000):
    gst=total *3/100
elif (total>=10000):
    gst=total*2/100
else:
    gst=total*1/100
    print("Gst (gat (good & service tax",gst)
    amount=total+gst
    print("Amount to be paid", amount)
