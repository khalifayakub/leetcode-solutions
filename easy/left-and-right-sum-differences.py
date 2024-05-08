class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # length of array
        n = len(nums)
        # init answer array to return result
        answer = [0] * n
        # init left and right sum
        left_sum = 0
        # prefix sum of nums array is right sum 
        right_sum = sum(nums)
        for i in range(n):
            # remove current number cause right of number does not include it
            right_sum -= nums[i]
            # get the difference
            answer[i] = abs(left_sum-right_sum)
            # add current number to left since you are going right of it,
            # meaning it is left (pun intended)
            left_sum += nums[i]
        # return answer
        return answer 