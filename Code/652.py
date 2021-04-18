import collections
from typing import List

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        count = collections.Counter()
        ans = []

        def collect(node):
            if not node: return "#"
            serial = "{},{},{}".format(node, collect(node.left), collect(node.right))
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            return serial

        collect(root)
        return ans

a = TreeNode(4)
b = TreeNode(2, left=a)
c = TreeNode(4)
d = TreeNode(3, left=b, right=c)
e = TreeNode(4)
f = TreeNode(2, left=e)
g = TreeNode(1, left=f, right=d)

sol = Solution()
ans = sol.findDuplicateSubtrees(g)
print(ans)