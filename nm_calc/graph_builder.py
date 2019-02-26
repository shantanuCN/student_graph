from ete3 import Tree, TreeStyle, TextFace, add_face_to_node
import pprint
legs = int(input("enter legs"))
months = int(input("enter months"))

parent = {}
month_duration = {}
leg_count = {}
node_count = 1

month_duration[1] = months
parent[1] = 1
leg_count[1] = 0

def addChildDfs(parent_node, child_number):
    global node_count
    if leg_count[parent_node] == legs:
        return
    if month_duration[parent_node] <= 2:
        return
    if month_duration[parent_node] <= (1 + child_number) :
        return
    node_count += 1
    new_node = node_count
    leg_count[parent_node] += 1
    leg_count[new_node] = 0
    parent[new_node] = parent_node
    month_duration[new_node] = month_duration[parent_node] - (1 + child_number)
    for i in range(1,legs + 1):
        addChildDfs(new_node, i)

pp = pprint.PrettyPrinter()
for i in range(1, legs + 1):
    addChildDfs(1, i)
pp.pprint("parent")
pp.pprint(parent)
pp.pprint("month")
pp.pprint(month_duration)
pp.pprint("legs")
pp.pprint(leg_count)

graph = {}
graph[1] = []

for i in range(2, node_count + 1):
    if parent[i] not in graph:
        graph[parent[i]] = []
    graph[parent[i]].append(i)

pp.pprint(graph)

subtree_count = {}
def countChildNodes(node):
    children = 1
    if node in graph:
        for child_node in graph[node]:
            children += countChildNodes(child_node)
    subtree_count[node] = children
    return children

countChildNodes(1)
pp.pprint(subtree_count)
profit_val = 0.0

def bonus(amnt):
    if amnt >= 1000000:
        return amnt * 0.36
    elif amnt >= 700000:
        return amnt * 0.33
    elif amnt >= 400000:
        return amnt * 0.30
    elif amnt >= 240000:
        return amnt * 0.28
    elif amnt >= 120000:
        return amnt * 0.26
    elif amnt >= 50000:
        return amnt * 0.24
    elif amnt >= 10000:
        return amnt * 0.21
    return 0

for i in range(1, node_count + 1):
    if(parent[i] == 1):
        print(str(i) + " " + str(subtree_count[i] * 10000.0))
        if (profit_val == 0):
            profit_val += bonus(subtree_count[i] * 10000.0)
        else:
            profit_val -= bonus(subtree_count[i] * 10000.0)
            if(subtree_count[i] * 10000.0 > 1000000):
                profit_val += subtree_count[i] * 10000.0 * 0.06

pp.pprint(profit_val)

def get_tree_string(node):
    if node not in graph:
        return str(month_duration[node]) + "_months"
    sz = len(graph[node])
    if sz == 0:
        return str(month_duration[node]) + "_months"
    return_str = "("
    for i in range(0, sz):
        if i != 0:
            return_str = return_str + ","
        return_str = return_str + str(get_tree_string(graph[node][sz - i - 1]))
    return return_str + ")" + str(month_duration[node]) + "_months"

tree_str = get_tree_string(1)+";"

t = Tree(tree_str, format=1)
ts = TreeStyle()
ts.show_leaf_name = False
def my_layout(node):
    F = TextFace(node.name, tight_text=True)
    add_face_to_node(F, node, column=0, position="branch-right")
ts.layout_fn = my_layout
ts.rotation = 90
t.show(tree_style=ts)
