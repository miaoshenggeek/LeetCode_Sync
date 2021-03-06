# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(preorder,inorder):
            if not preorder or not inorder:
                return
            a=preorder[-1]
            root=TreeNode(a)    
            preorder.pop()
            b=inorder.index(a)
            root.left=helper(preorder,inorder[:b])
            root.right=helper(preorder,inorder[b+1:])
            return root
        preorder.reverse()
        return helper(preorder,inorder)
        