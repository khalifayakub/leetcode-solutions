class Solution:
    def minimumSum(self, num: int) -> int:
        # sort the numbers
        string_num = sorted(str(num))
        # since we are always going to have four numbers
        # the minimum sum will always be the smallest number and the biggest number
        # recursively
        return int(string_num[0] + string_num[3]) + int(string_num[1] + string_num[2])
    
        