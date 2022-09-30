#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="\n" if i == x - 1 else "")
        except:
            print()
            break
        counter += 1
    return counter
