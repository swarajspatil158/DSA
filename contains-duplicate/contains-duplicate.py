class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dir = set()
        for i in nums:
            if i in dir:
                return True
            else:
                dir.add(i)
        return False
                