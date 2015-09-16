#Write a program that detect a "palindrome" string

# print "Give me a string!"
# s = raw_input('Give me a string! ')
# for i in range(len(s) / 2 - 1):
#     if s[i] != s[len(s) - i - 1]:
#         print "It's not a palindrome string!"
#         break
#     print "It's a PALINDROME string!"
    

#Or using reverse Function
s = raw_input("Give me a string! ")
rvs = s[::-1]
if rvs == s:
    print "It's a PALINDROME string!"
else:
    print "It's not a palindrome string!"