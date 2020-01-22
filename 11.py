a=int(input("Masukan angkamu : "))
for i in range(a) :
    if i==0 or i==a-1:
        print ("0"*a)
    else:
        print ("0 "+"*"*(a-1)+"0")
