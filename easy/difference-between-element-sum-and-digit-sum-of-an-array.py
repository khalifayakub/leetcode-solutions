class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(nums) - sum([int(x) for x in ''.join([str(x) for x in nums])]))