class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
            cnt = prev = 0
            for cur in nums:
                if cur <= prev:
                    prev += 1
                    cnt += prev - cur
                else:
                    prev = cur
            return cnt
    
	# for(int i = 1; i < size(nums); i++)
	# 	if(nums[i] <= nums[i - 1]) {  
	# 		cnt += (nums[i - 1] - nums[i] + 1), // nums[i] must be made atleast equal to nums[i-1]+1
	# 		nums[i] = nums[i - 1] + 1;
	# 	}
	# return cnt;