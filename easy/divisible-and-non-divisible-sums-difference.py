class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0 # init num1
        num2 = 0 # init num2
        for i in range(1, n + 1):
            if i % m == 0: # if i is divisible by m, it is added to num2
                num2 += i
            else: # if i is not divisible by m, it is added to num1
                num1 += i
        result = num1 - num2 # subtract the sums according to the problem desc
        return result # return result