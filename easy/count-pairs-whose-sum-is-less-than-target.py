class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        result = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i,n):
                if i != j:
                    if nums[i] + nums[j] < target:
                        result += 1
        
        return result