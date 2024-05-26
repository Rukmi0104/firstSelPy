string_1 = "Hello world"

# we can not modify the string as it is immutable, however we can work with them as list and truen them to string as needed
empty_list = []
for char in string_1:
    print(char)
    empty_list.append(char)
print(empty_list)
empty_list[6] = 'z'
print(empty_list)
string_1 = "".join(empty_list)
print(string_1)

# convert string to number
string_3 = "45"
str_to_num = int(string_3)
print(str_to_num)


# swapcase()> converts upper case to lower and lowercase to upper
string_3 = string_1.swapcase()
print(string_3)

string_4 = string_3.swapcase()
print(string_4)





