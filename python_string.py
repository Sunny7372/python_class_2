# creating a string in python
str1 = "iNeuron"
print(str1)

str2 = "sunny's"
print(str2)

str3 = 'he is a "Good" boy'
print(str3[0])
print(str3[1])
print(str3[2])

print(str3)

# use length function
print("length of str3:",len(str3))

# how to write multiline string
str4 = '''sunny is not 
going to
attend seminar'''
print(str4)

# string concatenation
str5 = "sunny"
str6 = "mishra"
print(str5+str6)

# string comparison?
str7 = "sunny"
str8 = "sunny"
print(str7==str8)

# how to print the each character from the string

for ch in str8:
    print(ch)

# slicing
print(str5[:])
print(str5[0:])
print(str5[0:4])
print(str5[0: : 2])
print(str5[-1: :-1])
print(str5[-2: : -1])


#update the 4th character in the string by M
str9 = "Sunny"
res=str9.replace('n','M')
print(res)
# string is immutable data types so we can't directly 
# make change in str variable

# convert string into lower case

print(str9.lower())

# convert string into upper case
print(str9.upper())


