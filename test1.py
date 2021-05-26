#python program to find sum of all the numbers in the list

list = [10,15,20,18,30]
def sumoflist(list,size):
    if (size==0):
        return 0
    else:
        return list[size-1]+ sumoflist(list,size-1)

total= sumoflist(list,len(list))
print("Sum of all the numbers in given list: ",total)