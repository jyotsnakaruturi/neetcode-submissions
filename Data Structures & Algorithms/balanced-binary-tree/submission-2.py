# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bfs(root):
            if not root:
                return 0,True
            left_h,l_b=bfs(root.left)
            right_h,r_b=bfs(root.right)
            if not l_b or not r_b:
                return 0,False
            if abs(left_h-right_h)>1:
                return 0,False
            return 1+max(left_h,right_h),True
        return bfs(root)[1]

            