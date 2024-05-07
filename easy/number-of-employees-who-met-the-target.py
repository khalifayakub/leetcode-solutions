class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # one liner using python list comprehension
        return len([x for x in hours if x >= target])