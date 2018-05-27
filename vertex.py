
class Vertex:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)

    def set_parent(self, parent):
        self.parent = parent

    def remove_child(self, value):
        # Iterates through all the children to remove the specified child
        for child in self.children:
            if child.value == value:  # EPPO: Seems like this will
                                      # take quite a lot of time for
                                      # very large trees.
                self.children.remove(child)
                # EPPO: Maybe also return to kill above objection?

                return True

        return False

    def is_leaf(self):
        return len(self.children) == 0

    def __str__(self):
        if self.leaf:
            return "Vertex with value " + str(self.value) + " and is a leaf"
        else:
            return "Vertex with value " + str(self.value) + " and children " + str([str(child.value) for child in self.children])
