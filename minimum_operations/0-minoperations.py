#!/usr/bin/python3
"""
Minimum Operations: Calculates the fewest number of operations needed
to result in exactly n H characters using Copy All and Paste.
"""


def minOperations(n):
    """Return minimum operations to reach n H's, else 0 if not possible."""
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations

