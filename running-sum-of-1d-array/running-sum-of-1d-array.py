class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        final =[nums[0]]
        cnt = nums[0]
        for i in range(1,len(nums)):
            cnt+=nums[i]
            final.append(cnt)
        return final