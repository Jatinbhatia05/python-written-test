#function in python which will return max exam score and username

dict1 = {1:'name1',2:'name2',3:'name3'}
dict2 = {1:50,2:60,3:70}
inverse= dict([(value,key)for(key,value) in dict2.items()])
max_score=max(inverse)
best_student=inverse[max_score]

result= {}
result[best_student]=max_score
print(result)