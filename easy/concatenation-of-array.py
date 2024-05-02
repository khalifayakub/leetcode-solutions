class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # variable to save the length
        n = len(nums)
        # init array for storing the concatenation
        ans = [0] * (2*n)
        for i in range(n):
            # fill the ans array according to problem description
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        # return concatenated array
        return ans