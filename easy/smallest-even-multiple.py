class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # n is always a multiple of itself and if n is divisible by 2, matches constraint
        # else just return a number that is divisible by 2 cause n will always divide itself
        # n * 2 = 2 * n
        return n if n % 2 == 0 else n*2