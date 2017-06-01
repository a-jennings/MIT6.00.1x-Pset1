#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5

#s = 'azcbobobegghakl'
total = 0

for i in range (len(s)):
    char = str(s[i])
    if char in 'aeiou':
        total += 1
print(total)

#Tested as correct    


