class Solution(object):
    def isAnagram(self, s, t):
        """
        docstring
        """
        dict_s = {}
        for char in s:
            if char in dict_s:
                dict_s[char] += 1
            else:
                dict_s[char] = 1
        dict_t = {}
        for char in s:
            if char in dict_t:
                dict_t[char] += 1
            else:
                dict_t[char] = 1
        print(dict_s)
        print(dict_t)
        return dict_t==dict_s


solution = Solution()
print(solution.isAnagram("a", "b"))
