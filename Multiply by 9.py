# Turn this into a recursive function

# This program multiplies the golden number (9) by a list of other digits
# and then adds up and digits higher than 9 again to display the end
# result, which is 9.

# Constants
nums = range(1, 999)
golden_number = 9
parse_deep = True
occurances = []

# Puts nums into a list and multiplies them by the golden number
my_list = [n * golden_number for n in nums]
print(my_list)
print('=' * 100)

# Split only if number bigger than 9
with open("numbers.txt", 'w') as number_file:
    for d in my_list:
        if d % golden_number == 0: #

            # splits digits into separate ints
            digits = [int(x) for x in str(d)]  # can try map(int,str(12345))

            # add ints together
            d2 = sum(digits) # d2 is an int

            if d % golden_number == 0 and parse_deep is True:
                digits = [int(x) for x in str(d2)] # digits is a list
                d2 = sum(digits) # d2 is an int

            # append to new list to count occurances when parse_deep is False
            if parse_deep is False:
                occurances.append(d2)

            print("{}: {}".format(d, d2))

    # count how many times occurances happen when parse_deep is False
    if parse_deep is False:
        print("Count for 09: {}".format(occurances.count(9)), file=number_file)
        print("Count for 27: {}".format(occurances.count(27)), file=number_file)
        print("Count for 36: {}".format(occurances.count(36)), file=number_file)
        print("Count for 45: {}".format(occurances.count(45)), file=number_file)

        digits = [int(x) for x in str(occurances.count(9))]  # digits is a list
        d2 = sum(digits) # d2 is an int
        print(d2, file=number_file)
        digits = [int(x) for x in str(occurances.count(27))]  # digits is a list
        d2 = sum(digits) # d2 is an int
        print(d2, file=number_file)
        digits = [int(x) for x in str(occurances.count(36))]  # digits is a list
        d2 = sum(digits) # d2 is an int
        print(d2, file=number_file)
        digits = [int(x) for x in str(occurances.count(45))]  # digits is a list
        d2 = sum(digits) # d2 is an int
        print(d2, file=number_file)

number_file.close
