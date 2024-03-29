from typing import List
import collections

"""                                                              
定义树节点                                                            
"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
1. 二叉树的最大深度: 4
"""
def maxDepth1(root):
    """dfs + 递归"""
    if not root: return 0
    return 1 + max(maxDepth1(root.left), maxDepth1(root.right))

def maxDepth2(root):
    """bfs + 迭代"""
    stack = []
    if root: stack.append((1, root))
    depth = 0
    while stack:
        cur_depth, root = stack.pop()
        if root:
            depth = max(depth, cur_depth)
            stack.append((cur_depth+1, root.left))
            stack.append((cur_depth+1, root.right))
    return depth


"""
2. 二叉树的最小深度: 3
"""
def minDepth1(root):
    """dfs"""
    if not root: return 0
    if not root.left and not root.right: return 1
    depth = 10 ** 9
    if root.left:
        depth = min(minDepth1(root.left), depth)
    if root.right:
        depth = min(minDepth1(root.right), depth)
    return depth + 1

def minDepth2(root):
    """bfs"""
    if not root: return 0
    #queue = [(root, 1)]
    queue = collections.deque([(root, 1)])
    while queue:
        #node, depth = queue.pop(0)
        node, depth = queue.popleft()
        if not node.left and not node.right:
            return depth
        if node.left:
            queue.append((node.left, depth+1))
        if node.right:
            queue.append((node.right, depth+1))
    return 0

"""
112. 路径总和 - 判断是否等于sum的路径
"""
def hasPathSum1(root, sum):
    """dfs + 递归"""
    if not root: return False
    if not root.left and not root.right:
        return root.val == sum
    return hasPathSum1(root.left, sum-root.val) or hasPathSum1(root.right, sum-root.val)


def hasPathSum2(root, sum):
    """bfs"""
    if not root: return False
    queue = collections.deque()
    queue.append((root, root.val))
    while queue:
        node, path = queue.popleft()
        if not node.left and not node.right and path == sum:
            return True
        if node.left:
            queue.append((node.left, path + node.left.val))
        if node.right:
            queue.append((node.right, path + node.right.val))
    return False

def hasPathSum3(root, sum):
    def traverse(node):
        """遍历所有路径和"""
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]
        left, right = [], []
        if node.left:
            left = [node.val + x for x in traverse(node.left)]
        if node.right:
            right = [node.val + x for x in traverse(node.right)]
        return left + right

    if sum in traverse(root): return True
    else: return False

"""
113. 路径总和 II - 找出路径总和等于sum的路径
"""
def pathSum(root, sum):
    """dfs"""
    ans = []  #记录最后结果
    path = []  #记录每条路径
    def dfs(root, total):
        if not root: return
        path.append(root.val)
        total -= root.val
        if not root.left and not root.right and total==0:
            ans.append(path[:])
        dfs(root.left, total)
        dfs(root.right, total)
        path.pop()
    dfs(root, sum)
    return ans


"""
101. 对称二叉树
"""
def isSymmetric1(root):
    """递归"""
    if not root: return True
    def dfs(left, right):
        # if not (left or right):
        if not left and not right:  #两个节点都为空
            return True
        # if not (left and right):
        if not left or not right: #一个结点为空
            return False
        if left.val != right.val: #两个节点值不同
            return False
        return dfs(left.left, right.right) and dfs(left.right, right.left)
    return dfs(root.left, root.right)


def isSymmetric2(root):
    """迭代"""
    if not root or not (root.left or root.right):
        return True
    queue = [(root.left, root.right)]
    while queue:
        left, right = queue.pop(0)
        if not(left or right): continue
        if not(left and right): return False
        if left.val != right.val: return False
        queue.append((left.left, right.right))
        queue.append((left.right, right.left))
    return True

"""                               
#测试用例1                                

c = TreeNode('C')
e = TreeNode('E')
h = TreeNode('H')
d = TreeNode('D', left=c, right=e)
a = TreeNode('A')
b = TreeNode('B', left=a, right=d)
h = TreeNode('H')
i = TreeNode('I', left=h)
g = TreeNode('G', right=i)
f = TreeNode('F', left=b, right=g)

ans = maxDepth1(f)
print("maxDepth: ", ans)
ans = maxDepth2(f)
print("maxDepth: ", ans)
ans = minDepth1(f)
print("minDepth: ", ans)
ans = minDepth2(f)
print("minDepth: ", ans)
"""


#测试用例2：对称二叉树

d = TreeNode(3)
e = TreeNode(4)
f = TreeNode(4)
g = TreeNode(3)
b = TreeNode(2, left=d, right=e)
c = TreeNode(2, left=f, right=g)
a = TreeNode(1, left=b, right=c)

ans = isSymmetric1(a)
print("is symmetric: ", ans)
ans = isSymmetric2(a)
print("is symmetric: ",ans)
ans = hasPathSum1(a, sum=7)
print("has path sum: ", ans)
ans = hasPathSum2(a, sum=7)
print("has path sum: ", ans)
ans = pathSum(a, 6)
print(ans)


"""
#测试用例3
a = TreeNode(7)
b = TreeNode(2)
c = TreeNode(11, left=a, right=b)
d = TreeNode(4, left=c)
e = TreeNode(13)
f = TreeNode(1)
g = TreeNode(4, right=f)
h = TreeNode(8, left=e, right=g)
i = TreeNode(5, left=d, right=h)

ans = hasPathSum3(i, 22)
print(ans)
ans = pathSum(i, 22)
print(ans)
"""
