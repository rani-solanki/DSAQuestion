def DuplicateNUm(Nums):
    Nums.sort()
    for i in range(len(Nums)):
        if (Nums[i] == Nums[i-1]):
            print(Nums[i])



Array = [6,4,3,2,2,3,34,1,7]
DuplicateNUm (Array)

# Time complexity o(n) 




