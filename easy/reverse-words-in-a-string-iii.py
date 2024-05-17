class Solution:
    def reverseWords(self, s: str) -> str:
        output = ""
        temp = ""
        for character in s:
            if character == " ":
                output += self.reverse(temp) + " "
                temp = ""
            else:
                temp += character
        return (output + self.reverse(temp))
                
    def reverse(self, s: str) -> str:
        return s[::-1]