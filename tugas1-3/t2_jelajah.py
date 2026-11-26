import sys
import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))


def jelajah(node, kedalaman=0, field=None):
    baris, kolom = node.start_point
    label = f"{field}: " if field else ""

    print("  " * kedalaman + f"{label}{node.type} [{baris + 1}:{kolom}]")

    for i, child in enumerate(node.children):
        if child.is_named:
            nama_field = node.field_name_for_child(i)
            jelajah(child, kedalaman + 1, nama_field)


if __name__ == "__main__":
    with open(sys.argv[1], "rb") as f:
        tree = parser.parse(f.read())

    jelajah(tree.root_node)