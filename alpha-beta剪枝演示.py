"""
极小极大搜索是博弈搜索的基本形式
alpha-beta剪枝是极小极大搜索的一种剪枝策略

随机生成一棵博弈树，求给定博弈树使用alpha-beta
剪枝之后搜索的结点的个数
这种方式可以用来考查alpha-beta剪枝算法是否正确
"""
import random
import pydot
import os
MAX_VALUE = 2**30
MIN_VALUE = -2**30
MAX_NODE_COUNT = 15
TARGET_DIR = "alpha-beta"
node_cnt = 0
# 从100开始，则按照文件名排序必然正确，如果从0开始则会将10排在2前面
img_cnt = 100
if not os.path.exists(TARGET_DIR):
    os.mkdir(TARGET_DIR)
"""
根节点为第0层，为我方
偶数层要最大化收益
奇数层要最小化收益
"""


class Node:
    def __init__(self, id):
        self.max = MAX_VALUE
        self.min = MIN_VALUE
        self.sons = []
        self.visit = False
        self.id = id

    def __str__(self):
        return "min={},max={}".format(self.min, self.max)


def generate_tree():
    global node_cnt
    node_cnt += 1
    root = Node(node_cnt)
    nodes=[root]
    i=0
    while node_cnt<MAX_NODE_COUNT and i<node_cnt:
        now=nodes[i]
        i+=1
        sonsize = random.randint(2, 3)
        for j in range(sonsize):
            node_cnt+=1
            son=Node(node_cnt)
            nodes.append(son)
            now.sons.append(son)
    while i<node_cnt :
        node=nodes[i]
        i+=1
        node.max = node.min = random.randint(0, 100)  # 这个值表示对我的好处有多大
    return root


def go(node, mi, ma, depth):
    #执行alpha-beta剪枝
    global img_cnt
    node.visit = True
    if len(node.sons) == 0:  # 如果为叶子节点
        return node.max
    else:
        node.min = mi
        node.max = ma
        for i in node.sons:
            x = go(i, node.min, node.max, depth + 1)
            if depth & 1:  # 奇数层，要最小化评估值，父亲告诉了我，不可太贪，否则会被剪枝
                if x < node.min:
                    node.max = MIN_VALUE  # 如果出界了，它就要认为自己赢了
                    break
                else:
                    node.max = min(x, node.max)
            else:  # 偶数层，要最大化评估值
                if x > node.max:
                    node.min = MAX_VALUE
                    break
                else:
                    node.min = max(x, node.min)
        tree_to_dot(root, os.path.join(TARGET_DIR, "%d.jpg" % img_cnt), node)
        img_cnt += 1
        if depth & 1:
            return node.max
        else:
            return node.min


def count_visit(node):
    #计算整棵树中访问的结点的个数
    if not node.visit:
        return 0
    return sum(map(count_visit, node.sons)) + 1


def tree_to_dot(root, filename, active_node):
    #将一棵树转化为一张图片
    g = pydot.Dot(graph_type="digraph")

    def dfs(node, parent, depth):
        if node is None:
            return
        color = "grey" if not node.visit else "red"
        shape = "rectangle" if depth & 1 else "ellipse"
        fontcolor = "green" if active_node == node else "black"
        g.add_node(pydot.Node(node.id, color=color,
                              fontcolor=fontcolor, label=str(node), shape=shape))
        if parent:
            g.add_edge(pydot.Edge(parent, node.id))
        for i in node.sons:
            dfs(i, node.id, depth + 1)
    dfs(root, None, 0)
    g.write(filename, prog="dot", format="jpg")


root = generate_tree()
go(root, MIN_VALUE, MAX_VALUE, 0)
print(count_visit(root), node_cnt)
