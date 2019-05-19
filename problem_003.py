"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
"""
Planning
========

Option 1
--------
1) Create a loop for 1 to x,
2) If x % loop counter then add it to list
3) Max the list

Pros:
> Logical

Cons:
> Slow at finding the largest.

Option 2
--------
Repeat option 1 loop, but descend from x.

Pros:
> Slightly faster

Cons:
> Still linear time.

Option 3
--------
Run the loop of option 1, but as the loop increments up,
we actually want to return the compliment partner of the
modulo operator, i.e.

If, x % 2 == x/2 and isinstance(x/2, int) == True

Then x/2 must be the largest factor.

"""

x = 600851475143

for y in range(2, x, 1):
    if not x % y:
        print(str(int(x / y)))
        break

"""
Using ints gives an answer of 8462696833 (multiply by 71).
"""


