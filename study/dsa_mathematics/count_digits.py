def countDigit(s):

    count = 0

    if s == 0:
        return 1

    while s != 0:
        count += 1

        s = s // 10

    return count


countDigit(123)


# Here we want to count the number of digits in a given number. We define a function
# Then we initialize a container in form of a number, that tracks the count with name "count"
# Then, we write a condition that says if the number is reduced to approximately zero, return 1, because 1 is also a number
# Then,we run a while loop that checks number supplied in the function, if the number is not approximately zero, then we increment our "count" by one unit, then we divide by 10, to move the decimal point further to the left.
# we return the "count"
