class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        repeat = collections.defaultdict(int)
        num = 0
        # for every element in nums
        for v in nums:    
            # count number of pairs based on duplicate values
            num += repeat[v]
            # increment the number of counts
            repeat[v] += 1
            # number has not been seen before
        # return
        return num