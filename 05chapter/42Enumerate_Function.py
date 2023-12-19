marks = [12, 56, 32, 98, 12,  45, 1, 4]

# index = 0# In this method we have to use index variable
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("Harry, awesome!")
#   index +=1

for index, mark in enumerate(marks, start=1):#but in enumerate function we don't have to use index variable
  print(mark)
  if(index == 3):
    print("Harry, awesome!")