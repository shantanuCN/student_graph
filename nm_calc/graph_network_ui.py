# # libraries
# import pandas as pd
# import networkx as nx
# import matplotlib.pyplot as plt
#
# # Build a dataframe with 4 connections
# df = pd.DataFrame({'from': [1,1,2,2], 'to': [2,3,4,5]})
#
# # Build your graph
# G = nx.from_pandas_edgelist(df, 'from', 'to')
#
# # Plot it
# nx.draw(G, with_labels=True)
# plt.show()

from ete3 import Tree, TreeStyle, TextFace, add_face_to_node
t = Tree( "(1_months,2_months,(1_months)3_months,(1_months,2_months)4_months,(1_months,2_months,(1_months)3_months)5_months,(1_months,2_months,(1_months)3_months,(1_months,2_months)4_months)6_months)8_months;" , format=1)
ts = TreeStyle()
ts.show_leaf_name = False
def my_layout(node):
    F = TextFace(node.name, tight_text=True)
    add_face_to_node(F, node, column=0, position="branch-right")
ts.layout_fn = my_layout
ts.rotation = 90
t.show(tree_style=ts)
