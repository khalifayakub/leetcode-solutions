class Solution(object):
    def theMaximumAchievableX(self, num, t):
        """
        :type num: int
        :type t: int
        :rtype: int
        """
        # we perform 2 actions simultaneously based on t.
        # any number will take 2x operations to be equal to num
        return num + (2 * t)