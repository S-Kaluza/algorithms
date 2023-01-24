

def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

# Given a n-ary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def maxDepth(self, root: 'Node') -> int:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        return 1 + max(self.maxDepth(child) for child in root.children)

def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if image[sr][sc] == color:
        return image
    def bfs(sr, sc, color):
        queue = [(sr, sc)]
        while queue:
            r, c = queue.pop(0)
            image[r][c] = color
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == oldColor:
                    queue.append((nr, nc))
