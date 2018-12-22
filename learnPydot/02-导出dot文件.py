import pydot
g=pydot.Graph("mygraph")
g.add_node(pydot.Node("haha")) 
print(g.to_string())

print('='*20)
g = pydot.Dot()
g.set_type('digraph')
node = pydot.Node('legend')
node.set("shape", 'box')
g.add_node(node)
node.set('label','mine')
print(g.to_string())