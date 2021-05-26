# python function to find the number of max consecutive 1's present in the array

l1 = [0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
c=0
max_count=0
for l in l1:
    if l==1:
        c=c+1
    else:
        if c>max_count:
            max_count=c
        c=0
print(max_count)