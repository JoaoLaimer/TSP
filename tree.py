class Tree(object):
    def __init__(self, name='root',weight=0,children=None,parent=None):
        self.name = str(name)
        self.weight = weight
        self.children = []
        self.isOdd = False
        self.parent = parent

        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name
    
    def search(self,name):
        if self.name == name:
            return self
        for child in self.children:
            result = child.search(name)
            if result is not None:
                return result
        return None
    
    def add_child(self,node):
        assert isinstance(node,Tree)
        self.children.append(node)
        node.parent = self
    
    def insert_in_tree(self,name,child):
        node = self.search(str(name))
        if node is not None:
            node.add_child(child)
        else:
            raise ValueError("Node not found") 

    def print_tree(self, indent=0):
        print("  " * indent + f"{self.name} (Weight: {self.weight})")
        for child in self.children:
            child.print_tree(indent + 1)
    
    def print_odds(self, indent=0):
        if self.isOdd:
            print("  " * indent + f"{self.name} (Weight: {self.weight})")
        for child in self.children:
            child.print_odds(indent + 1)

    def total_vertex(self):
        total = 1
        for child in self.children:
            total += child.total_vertex()
        return total

    def pre_order(self, weight):
        weight[0] += self.weight
        self.find_odd()
        for child in self.children:
            child.pre_order(weight)

    def find_odd(self):
        if len(self.children) % 2 != 0 and self.parent is not None:
            self.isOdd = False
        elif len(self.children) % 2 == 0 and self.parent is not None:
            self.isOdd = True
        elif len(self.children) % 2 != 0 and self.parent is None:
            self.isOdd = True
        else:
            self.isOdd = False
    
    def find_odd_nodes(self, odd_nodes):
        if self.isOdd:
            odd_nodes.append(self.name)
        for child in self.children:
            child.find_odd_nodes(odd_nodes)
        return odd_nodes
    
    def set_odds_in_tree(self):
        self.find_odd()
        for child in self.children:
            child.set_odds_in_tree()