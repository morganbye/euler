"""
A palindromic number reads the same both ways. The largest
palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of
two 3-digit numbers.
"""
"""
Planning
========

Option 1
--------
1) Create i loop starting with largest 3 digit number
    > create j loop for second number, DESC
    > check if product is a palindrome
    
Requires:
> Loop controller
> Palindrome check

Cons:
Slow, linear processing

"""


def is_int_palindrome(value):
    """Checks if a number is a palindrome.

    Parameters
    ----------
    value : int

    Returns
    -------
    bool

    """
    num_forward = list(str(value))
    num_reverse = num_forward.copy()
    num_reverse.reverse()

    if num_forward == num_reverse:
        return True
    else:
        return False


num_of_digits = 3
max_value = int('9' * num_of_digits)

for i in range(max_value, int(max_value / 10), -1):
    for j in range(max_value, int(max_value / 10), -1):
        if is_int_palindrome(i * j):
            print(
                '{i} x {j} = {ij}, is the largest {digits} palidrome '
                'product'.format(
                    i=i,
                    j=j,
                    ij=i * j,
                    digits=num_of_digits
                  )
                )
            # Break out of j-loop
            break
    # Only executed if j-loop didn't break
    else:
        continue
    break
