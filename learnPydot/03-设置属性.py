#Dot是最主要的接口，不要直接使用Graph类,pydot有bug，无法导出汉语
#所以还是通过命令行比较好
import pydot
g=pydot.Dot(fontname="Microsoft Yahei")
g.set_graph_defaults(fontname="Microsoft Yahei")
g.set_node_defaults(fontname="Microsoft Yahei")
g.set_edge_defaults(fontname="Microsoft Yahei")
g.add_edge(pydot.Edge("曹操","曹植"))
g.write(__file__+".jpg",format="jpg")
print(g.to_string())
