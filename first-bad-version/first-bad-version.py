# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start,end=1,n
        while start <=end:
            mid=(start+end)//2
            if isBadVersion(mid) == False:
                start=mid+1
            else:
                end=mid-1
        return start