# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        path = set()
        ps = []
        if not root.left and not root.right:
            return 1
        def pathPermutation(node, path, ps):
            
            
            path = path.copy()
            if node.val in path:
                path.remove(node.val)
            else:
                path.add(node.val)
            if not node.left and not node.right:
                return path
            if node.left:
                setleft = pathPermutation(node.left, path, ps)
                ps.append(setleft)
            if node.right:
                setright = pathPermutation(node.right, path, ps)
                ps.append(setright)
            return ps
        perms = pathPermutation(root, path, ps)
        
        count = 0
        
        for perm in perms:
            if len(perm) <= 1:
                count += 1
        return count
        
                
        
        
    
