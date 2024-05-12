class Solution:
    def countDigits(self, num: int) -> int:
        # change num to string then loop digits and check if divisible
        return len([x for x in str(num) if num % int(x) == 0])