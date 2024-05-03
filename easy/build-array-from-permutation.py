class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # save length of nums array
        n = len(nums)
        # init ans array (we know length is same as n)
        ans = [0] * n
        for i in range(n):
            # follow the problem description
            ans[i] = nums[nums[i]]
        # return ans array
        return ans