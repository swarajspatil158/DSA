class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0
        furthest_reached=0
        last = len(nums)-1
        while furthest_reached >=i and furthest_reached <= last:
            furthest_reached=max(furthest_reached,nums[i]+i)
            i+=1
            print(i)
            print(furthest_reached)
        return furthest_reached >= len(nums)-1
    