class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # it is basically asking for how many elements are less than k
        return len([x for x in nums if x < k])