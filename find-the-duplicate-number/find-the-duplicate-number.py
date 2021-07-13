class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict1 = {}
        for num in nums:
            if num in dict1:
                return num
            dict1[num]=num