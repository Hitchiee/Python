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
        print(timelist[I], end="  ")
        for A in range(I,(len(templist)),4):
            print("{0:4.1f}".format(templist[A]), end="    ")
        print("")
    print("")

def getaverage(templist,avgtemplist):
    for I in range(0,len(templist),4):
        a=0
        for B in range(I,I+4,4):
            a = a+sum(templist[B:B+4])
        a=a/4
        averagetemplist.append(a)
        
def warmest_day(lst):
    avg=0
    for I in range(1,len(lst),1):
        if lst[I]>lst[I-1] and lst[I]>avg:
            avg=lst[I]
        elif lst[0]>lst[I] and lst[0]>avg:
            avg=lst[0]
        else:
            avg=avg
    day=lst.index(avg)
    return avg,day

def get_day(lst,day):
    for I in range(4*day,(4*day)+4,1):
        warmestdaylist.append(lst[I])

def get_median(lst):
    lst2=sorted(lst)
    a=int(len(lst2)/2)
    med = lst2[a]
    return med

def printresults(day, avg, tlst, wdlst, med):
    print("Mediantemperatur: {:1.1f}".format(med),end="\n\n")    
    print("Varmaste dagen: Dag {},".format(day+1), "medeltemp: {0:0.1f}".format(average))
    print("Kl ", end="")
    for I in range(4):
        print("{}".format(tlst[I]), end=" ")
    print("")
    for I in range(4):
        print("    ", end="")
        print("{:4.1f}".format(wdlst[I]), end="")
        
print("Välkommen till meteorologsprogrammet!", end="\n\n")

dagar = int(input("Mata in antalet dagar: "))
undregr = int(input("Mata in undre gräns: "))
övregr = int(input("Mata in övre gräns: "))
print("")

#List declaration
timelist = ["07:00  ", "12:00  ", "19:00  ","02:00  "]
templist = []
averagetemplist = []
warmestdaylist = []

generate(dagar,undregr,övregr)
putheader(dagar)
display(templist, timelist)
getaverage(templist, averagetemplist)
average,day = warmest_day(averagetemplist)
get_day(templist,day)
median = get_median(templist)
printresults(day, average, timelist, warmestdaylist, median)

