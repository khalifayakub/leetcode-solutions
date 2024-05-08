class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # variable to save the maximum words in a sentence
        result = float('-inf')
        for sentence  in sentences: # loop through sentences
            # result will be current max of the number of words in the current
            result = max(result, len(sentence.split()))
        return result