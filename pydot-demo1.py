import pydot
g = pydot.Dot()
g.set_type('digraph')
node = pydot.Node('legend')
node.set("shape", 'box')
g.add_node(node)
node.set('label','mine')
g.write("haha.jpg",prog="dot",format="jpg")