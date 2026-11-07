# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:

        if (p == None or q == None):
            return p == q

        isLeftSame = self.isSameTree(p.left,q.left)
        isRightSame = self.isSameTree(p.right,q.right)

        return isLeftSame and isRightSame and p.val == q.val
        