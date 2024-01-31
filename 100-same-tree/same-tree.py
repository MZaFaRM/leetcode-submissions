# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def multiple_dfs (p, q):
            if not p and not q:
                return True
            elif not p or not q or p.val != q.val:
                return False
            return multiple_dfs(p.left, q.left) and multiple_dfs(p.right, q.right)

        return multiple_dfs(p, q)