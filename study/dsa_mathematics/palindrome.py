def is_palindrome(num):
    if num < 0:
        return False
    num_str = str(num)

    start = 0
    end = len(num_str) - 1

    while start < end:

        if num_str[start] != num_str[end]:
            return False

        start += 1
        end -= 1

    return True


def isPalindrome(num):

    if num < 0:
        return False

    length_digits = 0
    temp = num
    while temp != 0:
        temp //= 10
        length_digits += 1

    left, right = num, num
    for i in range(length_digits // 2):
        left_digit = left // (10 ** (length_digits - i - 1)) % 10
        right_digit = right % 10

        if left_digit != right_digit:
            return False

        left %= 10 ** (length_digits - i - 1)
        right //= 10

    return True


def is_palindrome2(num):

    if num < 0:
        return False

    reversed_num = 0
    original_num = num

    while num > 0:

        last_digit = num % 10

        reversed_num = reversed_num * 10 + last_digit

        num //= 10

    return original_num == reversed_num


is_palindrome(123454321)
isPalindrome(123454321)
is_palindrome2(123454321)
