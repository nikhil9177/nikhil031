
hun=100
tho=1000
fhun=500
b=print("1-balance enquiry")
c=print("2-cash with drawl")
d=print("3-generate pin")
e=print("4-change pin")
f=int(input("choose an option"))
print(f)
if f==2:
    given_amount=int(input("enter the amount"))
    if given_amount%100!=0:
        print("cannot dispense")

    elif given_amount in range(100,500):
        x= given_amount / 100
        if x<=4:
            print("collect cash",x*hun)
            print("number of hundred notes collected",x)
            exit()

    elif given_amount in range(500,1000):
        l=int(given_amount/100)
        if l>=5:
            print("collect cash",fhun)
            print("five hundred notes 1")
            y=(given_amount)-fhun
            j=y/100
            print("collect ",j*hun)
            print("hundred notes",j)
            exit()

    elif given_amount in range(1000,40000):
        z=int(given_amount / 1000)
        if z>=1:
            print("collect ",z*tho)
            print("thousand notes",z)
            rem_ammount= given_amount-(z * tho)
        if rem_ammount==0:
            exit()
        else:
            u= rem_ammount / 100
            if u>=5:
                print("collect cash",fhun)
                print("five hundred notes 1")
                i=given_amount-(fhun+(z*tho))
                b=i/100
                print("collect cash",b*hun)
                print("hundred notes",b)
            else:
                print("hundred notes ",u)
    elif given_amount>40000:
        print("please visit bank")
        exit()



