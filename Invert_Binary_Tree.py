# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
       
        def traverse(node,newnode):
            if node.left:
                newnode.right = TreeNode(node.left.val)
                traverse(node.left, newnode.right)
            if node.right:
                newnode.left = TreeNode(node.right.val)
                
                traverse(node.right, newnode.left)
        
        
        if root:
            resultTree = TreeNode(root.val)
            traverse(root,resultTree)
            return resultTree
