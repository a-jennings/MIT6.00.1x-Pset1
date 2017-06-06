#Assume s is a string of lower case characters.
#Write a program that prints the longest substring of s in which the
#letters occur in alphabetical order.
#For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd',
#then your program should print
#Longest substring in alphabetical order is: abc
#abcdefghijklmnopqrstuvwxyz


#s = 'azcbobobegghakl'
#s = 'cgihonzy'
#Longest substring in alphabetical order is: cgi
#s = 'tzngslbgsrroi'
#Longest substring in alphabetical order is: bgs
#s = 'osmssycalvnqckwieyucnj'
#Longest substring in alphabetical order is: mssy
#s = 'gklmvxomrexfemqnrzxam'
#Longest substring in alphabetical order is: gklmvx

long_string = ''
temp_string = ''

for i in range(len(s)-1):

    first_char = s[i]
    sec_char = s[i+1]
    if sec_char >= first_char:
        temp_string += first_char
    elif sec_char <= first_char:
        temp_string += first_char
        if len(temp_string) > len(long_string):
            long_string = temp_string
            temp_string = ''
        else:
            temp_string = ''
print(long_string)




