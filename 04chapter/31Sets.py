#sets does not contain the depilcate value and it is unordered sets
#sets does not support indexing
#sets are mutable
#sets are unindexed
#sets are unordered

s={12,45,"shivam","sagar",12}
#This is the union opertertion in sets
s1={12,45,35,1,51,8,51,32}
s2={21,12,16,97,78,3,45}
s4=s1.union(s2)
s5=s1.intersection(s2)
s6=s1.difference(s2)
print(s4)
print(s5)
print(s6)
print(s.isdisjoint(s1))

