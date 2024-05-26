# any text or log file can be handled
# operations - create new, open existing, update, delete

#########################################
# write -> if file is already exist then it will be overwritten with new text. If not exist then new file will be
# created and the perform write operation
# fh = open("text1.txt", 'w')  # -> w indicates write operation
# fh.write("this is first line in text1\n")
# fh.write("this is second line in text1\n")
# fh.write("this is third line in text1\n")
# fh.write("this is 4th line in text1\n")
# fh.close()


#########################################
# append -> if file is already exist then it will append with new text. If not exist then new file will be
# created and then add the text in the end of file

# fh = open("text2.txt", 'a')
# fh.write("this is first line in text2\n")
# fh.write("this is second line in text2\n")
# fh.write("this is third line in text2\n")
# fh.write("this is 4th line in text2\n")
# fh.close()


###############################
# read() -> this is default mode.
# if file is exist then it will read all the file's contents into a string.
# If it doesn't exist then throws FileNotFoundError as below.

# ex.1
fh = open("text1.txt")
# print(fh.read())        # read existing file

# ex.2
# ############################## read() -> You can also give read() an optional argument, which designates the number
# of characters to read from the file
# print(fh.read(14))      # o/p -> "this is first "

# ##############################
# ex.3
# fh2 = open("text1.txt", "r")
# print(fh2.read())


# ##############################

# fh1 = open("text5.txt")
# fh1.read()      # read unknown file.
    # FileNotFoundError: [Errno 2] No such file or directory: 'text5.txt'

###############################
# check type of file
# print(type(fh.read()))  #o/p -> <class 'str'>
# meaning file contents are in string form.
# if we want to extract it line by line, then we can use readLine() method
# readline reads just a single line from the file. readline just reads the next line
# with readline(), by default 'enter' is pressed after reading the line

# line1 = fh.readline()
# line2 = fh.readline()
# print(line1)
# print(line2)

# if we want to extract all lines, then we can use readLines() method

# readAllLines = fh.readlines()
# print(readAllLines)

# ##############################
# readlines using for loop

# list2 = fh.readlines()
# print(list2)
#
# for line in list2:
#     if 'second' in line:
#         print(line)
    # else:
    #     print("line does not contain word 'second'")


# ##############################
# file handling using with

# with open('text4.txt', 'w') as fh3:
# #     # print numbers from 0 to 9
#     for i in range(10):
#         fh3.write(str(i) + "\n")

    # using above list, print reverse numbers from 10 to 0

# with open("text5.txt", 'w') as fh:
#     for line in line_list[::-1]:
#         fh.write(line)

#############
# create new file "text5.txt" and write 2 line content and save it in a list using readlines()
with open("text5.txt", "a") as fh4:
    fh4.write("heelo\n")
    fh4.write("heelo1\n")
with open("text5.txt") as fr:
    line_list = fr.readlines()
    print(line_list)

#################
# create new file, write number from 1 to 10 using for loop. Reverse the number and append in the same file
# step1-> create new file and write 1 to 10
# with open("text6.txt", "w") as fw:
#     for i in range(10):
#         fw.write(str(i)+"\n")

# step 2 -> read all lines in file and save in a list
# with open("text6.txt") as fr:
#     line_list = fr.readlines()
# print(line_list)

# step3 -> reverse the numbers and print in a same file
# with open("text6.txt", "a") as fa:
#     for i in line_list[::-1]:
#         fa.write(i)





