def second(Numberlist,n):
    Numberlist.sort()

    index = 0
    while(index < n):
        if (Numberlist[index]==Numberlist[-2]):
            print("it is second largest number",Numberlist[index])
        if (Numberlist[index] == Numberlist[1]):
            print("it is second minimum number",Numberlist[index])
        index = index+1

Numberlist = [35,4,23,3,34,5,9,87]
n = len(Numberlist)
second(Numberlist,n)









