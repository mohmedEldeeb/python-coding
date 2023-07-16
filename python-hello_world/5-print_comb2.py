#!/usr/bin/python3
for i in range(10):
    for x in range(10):
        if i != 9 and x != 9:
            print("{:02d},".format(i), end=" ")
        else:
            print("{:02d}".format(i), end="\n")
