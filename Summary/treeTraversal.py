from typing import List

"""
定义树节点
"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
1. 前序遍历：F-B-A-D-C-E-G-I-H
根结点 - 左子树 - 右子树
"""
def preorderTraversal1(root:TreeNode) -> List[int]:
    """递归"""
    res = []
    def preorder(root):
        if not root: return
        res.append(root.val)
        preorder(root.left)
        preorder(root.right)
    preorder(root)
    return res

def preorderTraversal2(root:TreeNode) -> List[int]:
    """迭代"""
    res = []
    def preorder(root):
        stack = [root]
        while stack:
            s = stack.pop()
            if s:
                res.append(s.val)
                stack.append(s.right) #先压右节点
                stack.append(s.left) #再压左结点
    preorder(root)
    return res

"""
2. 中序遍历：A-B-C-D-E-F-G-H-I
左子树 - 根结点 - 右子树
"""
def inorderTraversal1(root: TreeNode) -> List[int]:
    """递归"""
    res = []
    def inorder(root):
        if not root: return
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)
    inorder(root)
    return res

def inorderTraversal2(root: TreeNode) -> List[int]:
    """迭代"""
    res = []
    def inorder(root):
        stack = []
        while stack or root:
            while root:  #一直搜索到左子树最深层的左结点
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
    inorder(root)
    return res

"""
3. 后序遍历 - A-C-E-D-B-H-I-G-F
左子树 - 右子树 - 根结点
"""
def postorderTraversal1(root: TreeNode) -> List[int]:
    """递归"""
    res = []
    def postorder(root):
        if not root: return
        postorder(root.left)
        postorder(root.right)
        res.append(root.val)
    postorder(root)
    return res

def postorderTraversal2(root: TreeNode) -> List[int]:
    res = []
    def postorder(root):
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                if root.left:
                    root = root.left
                else:
                    root = root.right
            s = stack.pop()
            res.append(s.val)
            if stack and s == stack[-1].left:
                root = stack[-1].right
            else:
                root = None
    postorder(root)
    return res

"""
4. 层序遍历(BFS): F-B-G-A-D-I-C-E-H
"""
def levelorderTraversal1(root):
    res = []
    def dfs(root, level):
        """递归"""
        if not root: return
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        if root.left:
            dfs(root.left, level+1)
        if root.right:
            dfs(root.right, level+1)
    dfs(root, 0)
    return res

def levelorderTraversal2(root):
    """迭代"""
    res = []
    queue = [root]
    while queue:
        n = len(queue)
        tmp = []  #存储每层的结点
        for _ in range(n):
            q = queue.pop(0)
            if q:
                tmp.append(q.val)
                queue.append(q.left if q.left else None)
                queue.append(q.right if q.right else None)
        if tmp: res.append(tmp)
    return res

"""
测试用例
"""
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

ans = preorderTraversal1(f)
print("preorder: ", ans)
ans = preorderTraversal2(f)
print("preorder: ", ans)
ans =inorderTraversal1(f)
print("inorder: ", ans)
ans =inorderTraversal2(f)
print("inorder: ", ans)
ans =postorderTraversal1(f)
print("inorder: ", ans)
ans =postorderTraversal2(f)
print("inorder: ", ans)
ans =levelorderTraversal1(f)
print("levelorder: ", ans)
ans =levelorderTraversal2(f)
print("levelorder: ", ans) 

