def subsetArray(list1,list2,list2_len):
    index = 0
    Bool = True
    while(index<list2_len):
        if (list2[index] not in list1):
            Bool = False
        index=index+1

    if (Bool == True):
        return("list2 subset in list1")
    else:
        return("list2 subset not in list1")

list1  = [2,3,4,12,67,34] 
list2 = [3,4,50,89,56]
list1_len =len(list1)
list2_len = len(list2)

print(subsetArray(list1,list2,list2_len))



