class Solution(object):
    def longestCommonSubstring(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        words = len(strs)
        strs = sorted(strs, key=len)
        longest_prefix = str(strs[0])

        flip = [1] * len(longest_prefix)

        for word in strs:
            word = str(word)
            for i in range(len(flip)):
                flip[i] &= 1 if (ord(longest_prefix[i]) == ord(word[i])) else 0
             
        result = ""
        temp = ""
        for i in range(len(flip)):
            if flip[i] == 1:
                temp += longest_prefix[i]
            if flip[i] == 0:
                if len(temp) > len(result):
                    result = temp
                    temp = ""

        return temp if len(temp) > len(result) else result 