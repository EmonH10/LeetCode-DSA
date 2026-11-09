# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isIdentical(self,root,subRoot):

        #Base Case
        if root == None or subRoot == None:
            return root == subRoot

        leftTree = self.isIdentical(root.left,subRoot.left)
        rightTree = self.isIdentical(root.right,subRoot.right)

        return leftTree and rightTree and root.val == subRoot.val

    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        if root == None or subRoot == None:
            return root == subRoot

        
        if root.val == subRoot.val and self.isIdentical(root,subRoot):
            return True 

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot) 
        