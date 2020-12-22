#重新排列字符串

# 字符串与列表的转化  list "".join
class Solution:
    def restoreString(self, s, indices) -> str:
        s_ = list(s)
        for i in range(len(s)):
            s_[indices[i]] = s[i]
        return "".join(s_)


solution = Solution()
result = solution.restoreString("codeleet",[4,5,6,7,0,2,1,3])
print(result)