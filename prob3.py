#Assume s is a string of lower case characters.
#Write a program that prints the longest substring of s in which the
#letters occur in alphabetical order.
#For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd',
#then your program should print
#Longest substring in alphabetical order is: abc




s = 'azcbobobegghakl'
alph = 'abcdefghijklmnopqrstuvwxyz'
ans1 = ''  #make final answer
ans2 = ''  #storage var 
#/chars can bool!

for i in range(len(s)-1):       #to fix s-1.
    if s[i] <= s[i+1]:
        ans2 = ans2 + s[i]

        
    elif s[i] > s[i+1]:
        if len(ans2) > len(ans1):
                ans1 = ans2
                ans2 = ''

print(ans2)

#expected answer: beggh
 


#Examples

#s = 'cgihonzy'
#Longest substring in alphabetical order is: cgi
#s = 'tzngslbgsrroi'
#Longest substring in alphabetical order is: bgs
#s = 'osmssycalvnqckwieyucnj'
#Longest substring in alphabetical order is: mssy
#s = 'gklmvxomrexfemqnrzxam'
#Longest substring in alphabetical order is: gklmvx

