
class Vertex:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.leaf = True
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        self.leaf = False

    def set_parent(self, parent):
        self.parent = parent

    def remove_child(self, value):
        # Iterates through all the children to remove the specified child
        for child in self.children:
            if child.value == value:
                self.children.remove(child)

        # Sets the is_leaf flag to true if there are no more children
        if len(self.children) == 0:
            self.leaf = True

    def is_leaf(self):
        return self.leaf

    def __str__(self):
        if self.leaf:
            return "Vertex with value " + str(self.value) + " and is a leaf"
        else:
            return "Vertex with value " + str(self.value) + " and children " + str([str(child.value) for child in self.children])
