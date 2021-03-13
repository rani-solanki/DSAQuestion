def sequencArray(array):
    i=0
    temp1 =0
    while(i< len(array)):
        j =0
        while(j< len(array)):
            if (array[i]< array[j]):
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
            j=j+1
        i=i+1
    return array
array = [ ]

user = int(input("enter the number"))
for num in range(0,user):
    Num = int(input("enter the number"))
    array.append(Num)
print(sequencArray(array))



