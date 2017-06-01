#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s.
#For example, if s = 'azcbobobegghakl', then your program should print:
#Number of times bob occurs is: 2

s = 'bobobfpbobobbobboboobobobobbbbobb'
total = 0

for i in range(len(s)):
    char = s[i]
    if char == 'b':
        if s[i]+s[i+1]+s[i+2] == 'bob':
            total += 1
        elif IndexError:
            break
print(total)
        

