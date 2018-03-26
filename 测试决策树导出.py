from sklearn import tree, datasets

data = datasets.load_iris()
x = data['data']
y = data['target']
clf = tree.DecisionTreeClassifier()
clf.fit(x, y)
tree.export_graphviz(clf)