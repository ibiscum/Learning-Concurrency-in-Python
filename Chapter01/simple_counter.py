""" Learning Concurrency in Python - Chapter 01 - simple counter """

# This is an example of a single-threaded program
# we simply print out the numbers 0-9
print("Single Threaded Counter")
for i in range(10):
    print(f"The Current Counter is {i}")
    print("-------------------------")
