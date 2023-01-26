
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
            if root is None:
                return False
            if root.left is None and root.right is None:
                return targetSum == root.val
            return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val) 

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def maxDepth(self, root: 'Node') -> int:
            if not root:
                return 0
            if not root.children:
                return 1
            return 1 + max(self.maxDepth(child) for child in root.children)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        self.dfs(image, sr, sc, image[sr][sc], color)
        return image
    def dfs (self, image, i, j, oldColor, newColor):
        if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != oldColor:
            return
        image[i][j] = newColor
        self.dfs(image, i+1, j, oldColor, newColor)
        self.dfs(image, i-1, j, oldColor, newColor)
        self.dfs(image, i, j+1, oldColor, newColor)
        self.dfs(image, i, j-1, oldColor, newColor)

    