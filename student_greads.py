
totalAmount=0

coin10rs=input("Enter total no of 10Rs coin\n")

coin10rsType=coin10rs.isdigit()

if coin10rsType==True:
    totalAmount += (10*int(coin10rs))

if coin10rsType==False:
    print("not valid input")
    exit()
    
coin5rs=input("Enter total no of 5 Rs coin\n")
coin5rsType=coin5rs.isdigit()

if coin5rsType==True:
    totalAmount += (5*int(coin5rs))

if coin5rsType==False:
    print("not valid input")
    exit()
coin2rs=input("Enter total no of 2 Rs coin\n")
coin2rsType=coin2rs.isdigit()

if coin2rsType==True:
    totalAmount += (2*int(coin2rs))

if coin2rsType==False:
    print("not valid input")
    exit()
coin1rs=input("Enter total no of 1 Rs coin\n")
coin1rsType=coin1rs.isdigit()

if coin1rsType==True:
    totalAmount += (1*int(coin1rs))

if coin1rsType==False:
    print("not valid input")
    exit()
    
print("Total amount in Yes-Bank:",totalAmount)
