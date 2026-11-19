import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))

kode = b"""
def sapa(nama):
    return "Halo, " + nama
"""

tree = parser.parse(kode)

function_node = tree.root_node.named_children[0]

print("Menggunakan children:")
for c in function_node.children:
    print(c.type, "bernama" if c.is_named else "anonim")

print("\nMenggunakan named_children:")
for c in function_node.named_children:
    print(c.type, "bernama")
