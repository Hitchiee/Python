def generate(dagar,undregr,övregr):
    from random import uniform
    for I in range((4*dagar)):
        a = uniform(undregr,övregr)
        templist.append(a)
        
def putheader(dagar):
    print("Temperaturer:")
    print("Tid     ",end=" ")
    for I in range(dagar):
        print("Dag {}".format(I+1), end="   ")
    print("")

def display(templist, timelist):
    for I in range(4):
        print(timelist[I], end="")
        for A in range(I,(len(templist)),4):
            print("{0:4.1f}".format(templist[A]), end="    ")
        print("")
    print("")

def getaverage(templist,avgtemplist):
    a=0
    for I in range(0,len(templist),4):
        for B in range(4):
            a = sum(templist[I:I+1])
            averagetemplist.append(a)
    
        
print("Välkommen till meteorologsprogrammet!", end="\n\n")

dagar = int(input("Mata in antalet dagar: "))
undregr = int(input("Mata in undre gräns: "))
övregr = int(input("Mata in övre gräns: "))
print("")

#Pre-determined lists
timelist = ["07:00    ", "12:00   ", "19:00   ","02:00  "]
templist = []
averagetemplist = []

generate(dagar,undregr,övregr)
putheader(dagar)
display(templist, timelist)
getaverage(templist, averagetemplist)
print(averagetemplist)
warmest_day(getaverage)

