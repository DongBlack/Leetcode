class Solution(object):
    def subSort(self, array):
        """
        可能是正序或者倒序，所以先判断前两个数字的大小，分别进入正序和倒序模式
        """
        length = len(array)
        if length<=2:
            return [-1,-1]
        head1,tail1 = -1,-1
        head2,tail2 = -1,-1
        list1 = array[:]
        list1.sort()
        for i in range(length):
            if array[i]!=list1[i]:
                head1 = i
                break
            if i==length-1 and head1 == -1:
                return [-1,-1]
        for i in range(length-1,0,-1):
            if array[i]!=list1[i]:
                tail1 = i
                break
        list1.sort(reverse=True )
        for i in range(length):
            if array[i]!=list1[i]:
                head2 = i
                break
            if i==length-1 and head2 == -1:
                return [-1,-1]
        for i in range(length-1,0,-1):
            if array[i]!=list1[i]:
                tail2 = i
                break
        if (tail1-head1)>(tail2-head2):
            return [head2,tail2]
        else:
            return [head1,tail1]
solution = Solution()
print(solution.subSort([]))


