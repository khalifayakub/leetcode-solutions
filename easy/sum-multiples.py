class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # filter the numbers that are divisible in the range then sum it
        return sum([number for number in range(1, n+1) if self.divisible(number)])

    def divisible(self, x: int) -> bool:
        # return number divisible by any of the 3 numbers in desc
        return True if x % 3 == 0 or x % 5 == 0  or x % 7 == 0 else False
    
    