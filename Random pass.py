import random
import string 
s1 = string.ascii_lowercase
s2= string.ascii_uppercase
s3= string.digits
s4= ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~',
		'*', '(', ')']
plen = int(input ("Enter password length : "))
m=[]
m.extend(list(s1))
m.extend(list(s2))
m.extend(list(s3))
m.extend(list(s4))
    # print(m)
random.shuffle(m)
    # print(m)


if(plen<12):
    print("Password must contain 12 digits or more otherwise password not generated")
elif (plen>=12):
    #print("Password: ")
    print("Password is created:\n","".join(m[0:plen]),"\nPasword stregth is good")
