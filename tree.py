# NOTE - Unused
from vertex import Vertex


class Tree:
    def __init__(self):
        self.vertices = []
        self.prufer_code = []

    def add_vertex(self, vertex: Vertex) -> None:
        """Method that adds a vertex to the tree.

        Args:
            vertex (Vertex): The vertex to be added.

        Returns:
            None
        """
        self.vertices.append(vertex)

    def __str__(self):
        return str([str(v) for v in self.vertices])
