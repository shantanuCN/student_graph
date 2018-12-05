import json
from pprint import pprint
from handle_graph import *

obj = HandleGraph("bolt://codegraph-prod-sandbox.devfactory.com:25508")
obj.makeConnenction()

with open('student_details.json') as f:
    data_node = json.load(f)

with open('relationship_details.json') as f:
    data_edge = json.load(f)

for node in data_node:
    obj.addNode(node['type'], node)

for edge in data_edge:
    if edge['type'] == 'friend':
        print(obj.addFriendEdge(edge['registration_number_from'], edge['registration_number_to']))
    else:
        print(obj.addAssignmentDoneEdge(edge['registration_number_from'], edge['registration_number_to']))
