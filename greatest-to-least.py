pint1 = int(input("Enter the first number: "))
pint2 = int(input("Enter the second number: "))
pint3 = int(input("Enter the third number: "))

def compare(int1, int2, int3):
    if compare_more(int1, int2) and compare_more(int1, int3):
        if compare_more(int2, int3):
            print("%s, %s, %s" % (int1, int2, int3))
        else:
            print("%s, %s, %s" % (int1, int3, int2))

def compare_more(int1, int2):
    return int1 > int2

compare(pint1, pint2, pint3)
compare(pint2, pint1, pint3)
compare(pint3, pint1, pint2)