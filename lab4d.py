#!/usr/bin/env python3
# Author ID: [mrdhakal]
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(new_str):
    # Place code here - refer to function specifics in section below
    return new_str[:5]

def last_seven(new_str):
    # Place code here - refer to function specifics in section below
    return new_str[-7:]

def middle_number(new_num):
    # Place code here - refer to function specifics in section below
    our_num = str(new_num)
    return our_num[1:3]

def first_three_last_three(str_one, str_two):
    # Place code here - refer to function specifics in section below
    return str_one[:3] + str_two[-3:]


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))