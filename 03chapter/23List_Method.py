list=[22,44,26,28,10]
list1=[1,2,3,4,5]
print(list)
list.append(12)
print(list)
list.sort( reverse=True)
list.reverse()
m=  list.copy()#copy list and prform any operations on it
print(list.count(22))   
print(list)
list.insert(2, 100)
print(list)
list.extend(list1)
print(list)



