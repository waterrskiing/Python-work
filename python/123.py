import os, sys

folder = "D:\mcu-sdk-2.0-origin\\bin\generator\\records\ksdk\sdk_example\\frdmk22f.yml"

file_data = open(folder,'rb').readlines()
# print file_data
# file_data2 = file_data [:]
# print file_data2
# path = os.path.dirname(folder)
# os.chdir(path)
# print path
# print os.path.basename(path)

# for root, dirs, files in os.walk(path):
#     print "root:"
#     print root
#     print "dirs:"
#     print dirs
#     print "files:"
#     print files


" String"
string = "Freescale_K1x_K10DN512M10\r\n "

"String.strip(char): remove char from beginning or end of string"
print string.strip()
# "->Freescale_K1x_K10DN512M10"

# print string[2:4]
# "->Fre"

"String.split"
# string2 = string.split('_')
# print string2
# string3 = string2[2][:4]
# print string3
# print string
# print string.isalpha()

"String with index"
# for index, line in enumerate (file_data):
#     if line.count('ksdk/sdk_example/common/demo_app.yml'):
#         file_data = file_data[index+9]
#         print "index+9:",file_data


"Function definition"
# # Function definition is here
# def printme( str ):
#    "This prints a passed string into this function"
#    print str.upper()
#    return str

# # Now you can call printme function
# printme("I'm first call to user defined function!")
# printme("Again second call to the same function")


"Check type of file: file.endswith"
"Replace 2 string:"
# data1[2], data2[2] = data2[2], data1[2]

"isalpha():This method returns true if all characters in the string are alphabetic and there is at least one character, false otherwise."
str1 = "hello_world:";  # No space & digit in this string
# print str1[0].isalpha()

str4 = "abc"
print str4.split('_')
