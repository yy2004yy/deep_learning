class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in reversed(s):
            value = roman_numerals[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        
        return total

        
s = Solution();
print(s.romanToInt("III"))      # Output: 3
print(s.romanToInt("IV"))       # Output: 4
print(s.romanToInt("IX"))       # Output: 9     
print(s.romanToInt("LVIII"))    # Output: 58
print(s.romanToInt("MCMXCIV"))  # Output: 1994