class Solution:
    def trap(self, height: List[int]) -> int:
        right = [0]* len(height)
        left = [0]* len(height)
        if not height:
            return 0
        max_l = height[0]
        max_r = height[-1]
        for ind in range(len(height)):
            if height[ind] >= max_l:
                max_l = height[ind]
            left[ind] = max_l
            
            if height[len(height)-ind-1] >= max_r:
                max_r = height[len(height)-ind-1]
            right[len(height)-ind-1] = max_r
        return sum([min(left[i],right[i]) - height[i] for i in range(len(height))])        