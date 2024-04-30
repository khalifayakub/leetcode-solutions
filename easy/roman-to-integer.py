class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # initialize the values for the roman numerals
        values = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, "IV": 4, "IX": 9,
                    "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        # array to use to convert roman to values
        numbers = []
        # substitute values for numbers
        for i in range(n):
            if i != 0 and values.get(str(s[i-1] + s[i])):
                numbers.pop()
                numbers.append(values.get(str(s[i-1] + s[i])))
            else:
                numbers.append(values[s[i]])
        # The sum of the numbers is the result
        return sum(numbers)
        