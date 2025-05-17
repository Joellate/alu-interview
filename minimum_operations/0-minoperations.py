def minOperations(n):
    """
    Calculates the minimum number of operations needed
    to get exactly n 'H' characters using Copy All and Paste.
    Returns 0 if n is impossible (e.g., n < 2).
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        # While divisor divides n, reduce n and count operations
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

