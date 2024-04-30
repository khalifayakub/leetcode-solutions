class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # sort the array by length because the shortest word will be the length of max common prefix
        strs = sorted(strs, key=len)
        # get the longest prefix string
        longest_prefix = str(strs[0])
        # this will keep track of common letters following the shortest word
        flip = [1] * len(longest_prefix)

        # dont care about adding the first word cause it will always be common to itself
        for word in strs:  
            word = str(word)
            # for each word, check for characters that are common
            for i in range(len(flip)):
                # Using the & to make sure both letters are correct and same with the longest prefix
                flip[i] &= 1 if (ord(longest_prefix[i]) == ord(word[i])) else 0
             
        result = ""
        # form the longest prefix as text
        for i in range(len(flip)):
            if flip[i] == 1:
                result += longest_prefix[i]
            else:
                return result
        # if result is not found above, that means there is only one word in the array
        return strs[0]