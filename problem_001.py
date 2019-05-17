"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def get_modulo_list(start, end, divisible):
    """Get a list of natural numbers that are divisible.

    Parameters
    ----------
    start : int
    end : int
    divisible : int

    Returns
    -------
    list

    """
    result = []

    for x in range(start, end):
        if not x % divisible:
            result.append(x)

    return result


def merge_lists(a, b):
    """Merge lists whilst removing dups.

    Parameters
    ----------
    a : list of int
    b : list of int

    Returns
    -------
    list

    """
    result = list(set(a + b))

    return result


start = 0
end = 1000

multiples_of_3 = get_modulo_list(start, end, 3)
multiples_of_5 = get_modulo_list(start, end, 5)

merged_multiples = merge_lists(multiples_of_3, multiples_of_5)

result = sum(merged_multiples)

print(str(result))
