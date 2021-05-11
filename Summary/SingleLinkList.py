"""
https://zhuanlan.zhihu.com/p/60057180
"""
# 定义结点
# 结点的数据结构：数据元素(item) + 指针（next）

class Node(object):
    """单链表的结点"""
    def __init__(self, item):
        self.item = item
        self.next = None
"""
# 定义链表
# 链表需要具有首地址指针head

class SingleLinkList(object):
    def __init__(self):
        self._head = None

# 创建链表
if __name__ == '__main__':
    # 创建链表
    link_list = SingleLinkList()
    # 创建节点
    node1 = Node(1)
    node2 = Node(2)
    # 将节点添加到链表
    link_list._head = node1
    node1.next = node2
    #访问链表
    print(link_list._head.item)
    print(link_list._head.next.item)
"""

# 增加操作方法
"""
is_empty() 链表是否为空
length() 链表长度
items() 获取链表数据迭代器
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
find(item) 查找节点是否存在
"""

class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def items(self):
        """遍历链表"""
        # 获取head指针
        cur = self._head
        # 循环遍历
        while cur is not None:
            # 返回生成器
            yield cur.item
            # 指针下移
            cur = cur.next

    def add(self, item):
        """向链表头部添加元素"""
        node = Node(item)
        # 新结点指针指向原头部结点
        node.next = self._head
        # 头部结点指针修改为新结点
        self._head = node

    def append(self, item):
        """尾部添加元素"""
        node = Node(item)
        # 先判断是否为空链表
        if self. is_empty():
            # 空链表，_head指向新结点
            self._head = node
        else:
            # 不是空链表，则找到尾部，将尾部next结点指向新结点
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, index, item):
        """指定位置插入元素"""
        # 头部插入
        if index <= 0:
            self.add(item)
        # 尾部插入
        elif index > (self.length() - 1):
            self.append(item)
        else:
            # 创建元素结点
            node = Node(item)
            cur = self._head
            # 循环到需要插入的位置
            for i in range(index-1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除结点"""
        cur = self._head
        pre = None
        while cur is not None:
            # 找到指定元素
            if cur.item == item:
                if not pre:
                    # 如果删除的是第一个节点，直接将head移至下一结点
                    self._head = cur.next
                else:
                    # 如果不是第一个节点，将删除位置的前一个结点直接指向后一个结点
                    pre.next = cur.next
                return True
            # 没找到指定元素，向后移
            else:
                pre = cur
                cur = cur.next

    def find(self, item):
        """查找元素是否存在"""
        return item in self.items()

# 操作链表
if __name__ == '__main__':
    link_list = SingleLinkList()
    # 向链表尾部添加数据
    for i in range(5):
        link_list.append(i)
    # 向头部添加数据
    link_list.add(6)
    # 遍历链表数据
    for i in link_list.items():
        print(i, end='\t')
    # 链表数据插入数据
    link_list.insert(3, 9)
    print('\n', list(link_list.items()))
    # 删除链表数据
    link_list.remove(0)
    print('\n', list(link_list.items()))
    # 查找链表数据
    print(link_list.find(4))




