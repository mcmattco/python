# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from operator import itemgetter

possible_palidrome_combos = []

for a in range(100, 1000):
    for b in range(100, 1000):
        if (str(a * b)) == (str(a * b)[::-1]):
            possible_palidrome_combos.append([a, b, a * b])

biggest_pal = (sorted(possible_palidrome_combos, key=itemgetter(2)))[-1]
print(
    f"the largest palindrome made from the product of two 3-digit numbers is\
{biggest_pal[2]}, which is {biggest_pal[0]} x {biggest_pal[1]}"
)
