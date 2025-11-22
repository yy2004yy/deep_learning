class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        origin = x
        if(x < 0):
            return False
        else:
            y = 0
            while(x > 0):
                y = y * 10 + x % 10
                x = x // 10
            if(y == origin):
                return True
            else:
                return False
# test
s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))