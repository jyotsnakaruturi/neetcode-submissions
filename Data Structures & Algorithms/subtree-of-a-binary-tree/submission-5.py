# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val == q.val:
                return sametree(p.left,q.left) and sametree(p.right,q.right)
            else:
                return False
        def helper(p,q):
            if not p:
                return False
            return helper(p.left,q) or helper(p.right,q) or sametree(p,q)
        return helper(root,subRoot)
                 