       # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        # lst = []        
        # def preorder(node):        
        #     if not node: return
        #     nonlocal lst
        #     lst.append(node.val)
        #     preorder(node.left)
        #     preorder(node.right)
        # preorder(node)
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return None
        if root.val == val: return root
        if val < root.val: return self.searchBST(root.left,val)
        if val > root.val: return self.searchBST(root.right,val)
        return None