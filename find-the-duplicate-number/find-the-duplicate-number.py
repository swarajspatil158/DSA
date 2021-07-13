class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr= [0 for i in range(len(nums)+1)]
        for i in range(len(nums)):
            arr[nums[i]]+=1
        print(arr)
        for i in range(1,len(arr)):
            if arr[i]>1:
                return i