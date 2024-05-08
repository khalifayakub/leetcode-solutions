class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        if ch in word: # check if character is in word
            index_of_ch = word.index(ch) # get index of first occurrence of character
            # reverse the string from prefix to index of character and append to rest of word
            return word[0:index_of_ch+1][::-1] + word[index_of_ch+1:]
        # do nothing if character is not in word
        return word