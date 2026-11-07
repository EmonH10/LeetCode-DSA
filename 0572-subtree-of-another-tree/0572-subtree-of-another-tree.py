# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isIdentical(self,root,subRoot):

        if root == None or subRoot == None:
            return root == subRoot

        isLeftSame = self.isIdentical(root.left, subRoot.left)
        isRightSame = self.isIdentical(root.right, subRoot.right)

        return isLeftSame and isRightSame and root.val == subRoot.val 
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        if root == None or subRoot == None:
            return root == subRoot
        
        if (root.val == subRoot.val and self.isIdentical(root,subRoot)):

            return True 

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)