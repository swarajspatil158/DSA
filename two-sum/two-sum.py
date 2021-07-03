class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index in range(len(nums)):
            val2 = target - nums[index]
            if val2 in dict:
                return [dict[val2], index]
            dict[nums[index]] = index
        