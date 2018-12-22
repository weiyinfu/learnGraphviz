import pydot
import sys
"""
给定一个二进制数字，判断这个数字模n余几，这个问题可以使用有限状态自动机来描述
"""


def build(n):
    a = [[] for i in range(n)]
    for i in range(n):
        a[i].append((0, i * 2 % n))
        a[i].append((1, (i * 2 + 1) % n))
    return a


def export(g)->pydot.Dot:
    dot = pydot.Dot(graph_type='digraph')
    for i in range(len(g)):
        for label, j in g[i]:
            dot.add_edge(pydot.Edge(i, j, label=label))
    #TODO
    return dot


def main():
    n = 4
    g = build(n)
    dot = export(g)
    filename = __file__ + '.jpg'
    dot.write(filename, prog="dot", format="jpg")


if __name__ == '__main__':
    main()
