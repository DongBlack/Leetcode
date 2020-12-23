#列表中删除元素
class Solution:
    def merge(self, intervals):
        length = len(intervals)
        for i in range(length-1):
            for j in range(length-1-i):
                if intervals[j][0]>intervals[j+1][0]:
                    intervals[j],intervals[j+1] = intervals[j+1],intervals[j]
        flag = 0
        for i in range(length-1):
            if flag != 0:
                i = i- flag
            if intervals[i][1]>=intervals[i+1][0]:
                if intervals[i+1][1]>intervals[i][1]:
                    intervals[i][1] = intervals[i+1][1]
                intervals.pop(i+1)
                length-=1
                if i == length-1:
                    break
                flag += 1
        return intervals

solution = Solution()
solution.merge([[1,4],[4,5]])