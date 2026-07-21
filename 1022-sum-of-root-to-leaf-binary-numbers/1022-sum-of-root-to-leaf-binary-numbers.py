# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root) -> int:
        def dfs(node, current_val):
            # 1. Base case: If the node is None, return 0 to prevent the crash
            if not node:
                return 0
                
            # 2. Now it is completely safe to access node.val
            current_val = (current_val << 1) | node.val
            
            # 3. If it's a leaf node, return the completed binary number
            if not node.left and not node.right:
                return current_val
                
            # 4. Continue down both paths and sum their results
            return dfs(node.left, current_val) + dfs(node.right, current_val)
            
        return dfs(root, 0)