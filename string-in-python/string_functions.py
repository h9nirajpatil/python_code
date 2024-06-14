a = " Hello World! "
print(a.upper())#to covert to all uppercase
print(a.capitalize())#to capatize the first letter
print(a.lower())#to covert to all lowercase
print(a.split())#The split() method splits the string into substrings if it finds instances of the separator
print(a.startswith('H'))#check whetter the string starts with h
print(a.endswith('d'))#check whetter the string end with d
print(a.strip())#The strip() method removes any whitespace from the beginning or the end:
print(a.lstrip())#removes space from left
print(a.rstrip())#removes space from right
print(a.replace("H","h"))#The replace() method replaces a string with another string
print(a.index('W'))#If the string is unknown it gives an error message
print(a.find('e'))#If the string is unknown it gives a negative value
print(a.find('a'))
# print(a.index('b'))
print(a.count('o'))#it count no. of time occurs in string

s='hello1234'
print(s.isalnum())#alphanumeric it can have aplabet or numeric
s1='hii'
print(s.isalpha())#only alpabets

s2='123'
print(s2.isdigit())

s3='65'
print(s3.isascii())