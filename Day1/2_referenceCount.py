import sys

# create object
x = [1, 2, 3]

# get reference count
ref_count = sys.getrefcount(x)

print(f"reference count of x is {ref_count}")


a = [1, 2, 3]
b = [4, 5, 6]
a.append(b)
b.append(a)

ref_count_a = sys.getrefcount(a)
ref_count_b = sys.getrefcount(b)
print("reference count of a is ", ref_count_a)
print("reference count of b is ", ref_count_b)
