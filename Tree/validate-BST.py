# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def check(root, low_range=float('-inf'), high_range=float('inf')):
            if not root:
                return True
            elif not low_range < root.val < high_range:
                return False
            
            return check(root.left, low_range, root.val) and check(root.right, root.val, high_range)
        
        return check(root)