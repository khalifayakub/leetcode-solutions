class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        # initializing i and result variable
        result = i = 0
        for number in nums: # looping through numbers
            binaryValue = bin(i) # converting index to binary
            digits = len([x for x in binaryValue if x == '1']) # counting number of set bits
            if k == digits: # if set bits equals k
                result += number # add number on the index to result
            i += 1
        return result