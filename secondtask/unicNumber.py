def unicElement(list,list2):    
    unicNumber = []
    i=0
    while(i<len(list)):
        if (list[i] in list2):
            unicNumber.append(list[i])
        i=i+1

    return unicNumber

list = [2,3,45,4,5,-1,56]
list2 = [45,6,2,-1,56]
print(unicElement(list,list2))


