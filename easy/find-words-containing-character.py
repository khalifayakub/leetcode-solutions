class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        i = 0 # init i which would hold the position of words
        ans = [] # init ans array
        for word in words:
            if x in word: # if word has the letter
                ans.append(i) # add index to array
            i += 1 # increment i
        # return ans
        return ans