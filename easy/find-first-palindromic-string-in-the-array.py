class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
        return ""

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]