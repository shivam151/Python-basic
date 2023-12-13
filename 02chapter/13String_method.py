#String are inmutable in the python
s= "shivam! !!!!!!"
print(len(s))
print(s.upper())
print(s.lower())
print(s.split(" "))
print(s.strip("!"))#remove the ! from the string
print(s.replace("!","@"))#It will replace the value of the string
print(s.find("s"))
print(s.capitalize())
print (s.count("s"))
print(s.center(20,"*"))


print(s.isalnum())#this is used A-Z and a-z 0-9 value in the string and return the true or false
print(s.isalpha()) #this is used A-Z and a-z value in the string and return the true or false
