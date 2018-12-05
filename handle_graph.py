from py2neo import Graph

class HandleGraph:

    def __init__(self, boltUrl):
        self.boltUrl = boltUrl

    def makeConnenction(self):
        self.g = Graph(self.boltUrl)

    def addNode(self, type, properties):
        query = "create (n:" + type + "{ "
        cnt = 0
        for key in properties:
            if cnt != 0:
                query = query + ","
            query = query + key + ": '" + str(properties[key]) + "'"
            cnt += 1
        query = query + "}) return id(n) as id"
        data = self.g.run(query).data()
        return data[0]["id"]

    def addFriendEdge(self, reg_no_from, reg_no_to):
        query = """
            MATCH (a:student),(b:student)
            WHERE a.registration_number = '{n1}' AND b.registration_number = '{n2}'
            CREATE (a)-[r1:friend]->(b)
            CREATE (b)-[r2:friend]->(a)
            RETURN type(r1),type(r2)
        """
        query = query.format(n1=reg_no_from, n2=reg_no_to)
        data = self.g.run(query).data()
        return data

    def addAssignmentDoneEdge(self, reg_no_from, assignment_no_to):
        query = """
            MATCH (a:student),(b:assignment)
            WHERE a.registration_number = '{n1}' AND b.assignment_number = '{n2}'
            CREATE (a)-[r:done]->(b)
            RETURN type(r)
        """
        query = query.format(n1=reg_no_from, n2=assignment_no_to)
        data = self.g.run(query).data()
        return data

# obj = ClassWithinClass("bolt://codegraph-prod-sandbox.devfactory.com:22636")
# obj.makeConnenction()
# data_list = []
# data_list.append()
# properties = {}
# properties["assignment_name"] = "neural_net"
# properties["assignment_number"] = "5"
# print(obj.addNode("assignment", properties))
# print(obj.addAssignmentDoneEdge("1", "5"))