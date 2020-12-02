class Edge(object):
    def __init__(self, from_node, to_node, score):
        self.begin = from_node
        self.end = to_node
        self.score = int(score)

    def GetScore(self):
        return self.score

class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.prev = name

    def GetName(self):
        return self.name
