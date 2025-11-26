class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]
        
        return strs[0]
    
s = Solution()
string_exp1 = ["flower","flow","flight"]
string_exp2 = ["dog","racecar","car"]
string_exp3 = ["yyyyy111","yyyy575","yyy128"]
print(s.longestCommonPrefix(string_exp1))
print(s.longestCommonPrefix(string_exp2))
print(s.longestCommonPrefix(string_exp3))

# if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
#     return strs[0][:i]
# # 等价于
# for j in range(1, count):
#     if i == len(strs[j]) or strs[j][i] != c:
#         return strs[0][:i]
