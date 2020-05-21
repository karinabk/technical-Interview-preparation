#Kth Smallest Element in a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from heapq import heappop,heappush
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        minheap=[]
        def traverseToHeap(node):
            heappush(minheap, node.val)
            if node.left:
                traverseToHeap(node.left)
            if node.right:
                traverseToHeap(node.right)
        traverseToHeap(root)
        for i in range(k):
            result = heappop(minheap)
        return result
