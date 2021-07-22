class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        p1=0
        p2=n
        arr=[]
        for i in range(n):
            arr.append(nums[i])
            arr.append(nums[n+i])
        return arr