#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s.
#For example, if s = 'azcbobobegghakl', then your program should print:
#Number of times bob occurs is: 2

#s = 'bobobfpbobobbobboboobobobobbbbobb'
total = 0

for i in range(len(s)-2):

    char = s[i]
    x = s[i]+s[i+1]+s[i+2] 
    if char == 'b':
        if x == 'bob':
            total += 1
        else:
            continue
print(total)


        

#Tested as correct
