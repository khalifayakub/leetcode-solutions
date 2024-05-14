class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1, n + 1):
            # this gives you the sum of digits from 1..i
            first_range = (i * (i + 1)) // 2
            # to get sum of digits from i..n,
            # you get the sum of 1..n and subtract from the sum
            # of 1..i-1
            second_range = ((n * (n + 1)) // 2) - ((i * (i - 1)) // 2)
            # according to problem statement, if range from 1..i == i..n
            # return i
            if first_range == second_range:
                return i
        return -1