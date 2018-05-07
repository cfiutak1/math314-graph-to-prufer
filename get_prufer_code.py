from vertex import Vertex
import json
import sys


def get_vertex(vertices: list, value: int) -> Vertex:
    """Function which returns a vertex object with value <value> from a list of
    vertices. Assumes a well-formed list of vertices.

    Args:
        vertices (list): A list containing every vertex in a given tree.

        value (int): The value of the vertex.

    Returns:
        Vertex: The vertex object corresponding to value.
    """
    for vertex in vertices:
        if vertex.value == value:
            return vertex


def construct_graph(tree_json: list) -> list:
    """Function which constructs a list of vertices that represents the input
    graph. Reads in all vertices in a provided JSON formatted data structure,
    and connects them to their parent (if applicable).

    Args:
        tree_json (list): A list of dictionaries which represents every vertex
        in a tree.

    Returns:
        vertex_list (list): A list of Vertex objects that represents the given
        JSON structure.
    """

    vertex_list = []

    for vertex in tree_json:
        v = Vertex(vertex["value"])

        # Add the root
        if vertex["parent"] == -1:
            # Sanity check for an improperly added root
            if len(vertex_list) != 0:
                raise Exception("The root must be the first vertex in the file")

            vertex_list.append(v)
            continue

        # Add a regular vertex
        else:
            parent = get_vertex(vertex_list, vertex["parent"])

            v.set_parent(parent)
            parent.add_child(v)
            vertex_list.append(v)

    return vertex_list


def get_leaves(vertex_list: list) -> list:
    """Function that returns a list of vertices that are leaves.

    Args:
        vertex_list (list): A list of all Vertex objects in a given tree.

    Returns:
        leaves_list (list): A list of Vertex objects that have no children.
    """
    leaves_list = []

    for vertex in vertex_list:
        if vertex.is_leaf():
            leaves_list.append(vertex)

    return leaves_list


def find_smallest_leaf(root: Vertex, leaf_list: list) -> Vertex:
    """Function that finds the smallest leaf in a list of leaves.

    Args:
        root (Vertex): The root of the tree.

        leaf_list (list): A list of all leaves in the tree.

    Returns:
        smallest_leaf (Vertex): The Vertex object with the smallest value.
    """
    min_so_far = 2 ** 64
    smallest_leaf = None

    for leaf in leaf_list:
        if leaf.value < min_so_far and leaf != root:
            min_so_far = leaf.value
            smallest_leaf = leaf

    return smallest_leaf


def generate_prufer_code(root: Vertex, vertex_list: list) -> list:
    """Function that generates the prufer code of a given tree.
    
    Args:
        root (Vertex): The root of the tree.

        vertex_list (list): A representation of a tree with a list of Vertex
        objects.

    Returns:
        prufer_code (list): A list containing the prufer code of a tree.
    """
    prufer_code = []

    while find_smallest_leaf(root, vertex_list) is not None and len(vertex_list) > 2:
        # Determine the leaf to prune and its parent
        delete = find_smallest_leaf(root, get_leaves(vertex_list))
        parent = delete.parent

        # Delete the victim from the vertex list
        vertex_list.remove(delete)

        # Remove the victim from its parent's children list
        parent.remove_child(delete.value)

        # Append the parent's value to the prufer sequence
        prufer_code.append(parent.value)

    return prufer_code


def main():
    # Check that the program was invoked correctly
    if len(sys.argv) != 2 or ".json" not in sys.argv[1].lower():
        raise Exception("Please invoke as <get_prufer_code.py tree.json>")

    # Read in the tree JSON
    fptr = open(sys.argv[1], "r")
    tree_json = json.load(fptr)
    fptr.close()

    # Sanity check for bad values
    for vertex in tree_json:
        if vertex["value"] not in range(len(tree_json)):
            raise Exception("Invalid vertex value of " + str(vertex["value"]))

    # If there are 0 vertices or 1 vertex in the json, return nothing
    if len(tree_json) < 3:
        print("There is no prufer code for this graph")
        return

    # Construct the graph
    vertex_list = construct_graph(tree_json)

    # Generate the prufer code
    prufer_code = generate_prufer_code(vertex_list[0], vertex_list)

    print(prufer_code)


main()
