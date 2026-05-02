# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l1=self.helper(p)
        l2=self.helper(q)
        return l1 == l2
        
    def helper(self,root):
        q=collections.deque()
        q.append(root)
        res=[]
        while q:
            level=[]
            for i in range (len(q)):
                node=q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)
                else:
                    level.append("null")
            res.append(level)
        return res
            

            
