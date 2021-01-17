# Your task is to make a function that can take any 
# non-negative integer as an argument and return it with its 
# digits in descending order. Essentially, rearrange the digits 
# to create the highest possible number.

# Examples:

# Input: 42145 Output: 54421
# Input: 145263 Output: 654321
# Input: 123456789 Output: 987654321



def descending_order(num):
    # Bust a move right here

    #converting the integer into string or numbers
    str_num = str(num)
    #creating a blank list for storing the numbers of the string
    descended_list_num = []
    #creating a blank string variable for storing the descended string number
    descended_str_num = ''

    # loops through the str_num and adds the numbers to a list for better accessebility
    for i in str_num:
        descended_list_num.append(i)
        
    # here we sort the list based on biggest to smallest number in the list    
    descended_list_num.sort(reverse=True)

    # now we loop through the list and add the list items/numbers to the blank string variable for integer conversion
    for j in descended_list_num:
        descended_str_num = descended_str_num + j

    # here we conver the final string into a integer 
    descended_num = int(descended_str_num)

    # here we return the integer
    return descended_num


# 1201 should equal 2110
# Test Passed
# Completed in 0.08ms
# Random tests
# Test Passed
# 8342 should equal 8432
# 4185968 should equal 9886541
# 716261 should equal 766211
# Test Passed
# Test Passed
# 99924445 should equal 99954442
# 564 should equal 654
# Test Passed
# 499643342 should equal 996444332
# Test Passed
# 892514917 should equal 998754211
# Test Passed
# 17026 should equal 76210
# 1617356498 should equal 9876654311
# Test Passed
# 958629 should equal 998652
# Test Passed
# 603343408 should equal 864433300
# 447562 should equal 765442
# 770687713 should equal 877776310
# 16484933 should equal 98644331
# 823215 should equal 853221
# 4408459 should equal 9854440
# 1373796 should equal 9776331
# Test Passed
# 74207 should equal 77420
# 3355493 should equal 9554333
# 616697632 should equal 976666321
# 719905 should equal 9975100
# 477729 should equal 9777420
# 9367156 should equal 9766531
# 46 should equal 64
# 637 should equal 763
# 396370599 should equal 999765330
# 45667 should equal 76654
# Test Passed
# 7322344706 should equal 7764433220
# 34179 should equal 97431
# 9428 should equal 9842
# 83915 should equal 98531
# 26903 should equal 96320
# Test Passed
# Test Passed
# 620818828 should equal 888862210
# 750491213 should equal 975432110
# 414902036 should equal 964432100
# 210339 should equal 933210
# 35500315 should equal 55533100
# 553760706 should equal 776655300
