from ete3 import Tree
import json 

f = open("../david/placements.jplace")

data = json.load(f)

# print(data.keys())
for i in data['tree']:
    print(i)

# t = Tree("metag_tree_bacteria.newick")
# t = Tree("../david/placements.jplace")

# # print(type(t))
# for node in t.traverse("postorder"):
#   # Do some analysis on node
#     print(node.name)



