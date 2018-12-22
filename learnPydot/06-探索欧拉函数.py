import pydot
import os
N = 8


def get_vals(N, op):
    a = []
    for i in range(N):
        b = []
        x = i
        while x not in b:
            b.append(x)
            x = op(x, i) % N
        a.append(b)
    return a


def form_dot(N, g, path, prog, format):
    graph = pydot.Dot("数字图", fontname="Microsoft Yahei",
                      graph_type='digraph', label=str(N) + "Graph")
    for i in range(N):
        for j in range(N):
            if g[i][j]:
                graph.add_edge(pydot.Edge(i, j, label=str(g[i][j])))
    graph.write(path=path, prog=prog, format=format)  # prog默认为dot


def get_mul_graph(N, path, prog, format):
    a = get_vals(N, lambda x, y: x * y)
    print(a)
    g = [[[]for i in range(N)]for j in range(N)]
    g[0][0] = [0]
    for i, ar in enumerate(a):
        for j in range(len(ar)):
            if ar[j] != 0:  # 如果到了0，就别想出来了
                g[ar[j]][ar[(j - 1 + len(ar)) % len(ar)]].append(i)
    form_dot(N, g, path, prog, format)


def get_add_graph(N, path, prog, format):
    a = get_vals(N, lambda x, y: x + y)
    print(a)
    g = [[[]for i in range(N)]for j in range(N)]
    for i, ar in enumerate(a):
        for j in range(len(ar)):
            g[ar[j]][ar[(j - 1 + len(ar)) % len(ar)]].append(i)
    form_dot(N, g, path, prog, format)
# get_mul_graph(10,"mul.jpg","circo","jpg")#circo和spdf效果比较好
# get_add_graph(2,"add.jpg","circo","jpg")


"""
python 探索欧拉函数.py add 4 #只生成add图
python 探索欧拉函数.py mul 8 #只生成mul图
python 探索欧拉函数.py 4  #同时生成add图和mul图
"""
if __name__ == '__main__':
    x, method = 3, None
    if len(os.sys.argv) == 2:
        x = int(os.sys.argv[1])
    elif len(os.sys.argv) == 3:
        x = int(os.sys.argv[2])
        method = os.sys.argv[1]
    if not method or method == 'mul':
        get_mul_graph(x, "mul.jpg", "circo", "jpg")
    if not method or method == 'add':
        get_add_graph(x, "add.jpg", "circo", "jpg")
"""
费马小定理是欧拉定理的特殊形式

他们是如何发现这些规律的？

给定一个数字N，可以画出一个包含N个结点的图来，图中每条边上标有数字。

只有2，4，2p，2p^a才有原根

定义一种二元运算取模，就会形成一种图。
这种图是一种天然的图，非常巧妙的图。
"""
