class Solution:
    def finalString(self, s: str) -> str:
        output = ""
        for letter in s:
            if letter == 'i':
                output = output[::-1]
            else:
                output += letter
        return output