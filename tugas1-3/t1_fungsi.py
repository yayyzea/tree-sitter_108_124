import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))

kode = b"""
def sapa(nama):
    return "Halo, " + nama
"""

tree = parser.parse(kode)

# Menampilkan seluruh syntax tree
print(tree.root_node)

# Mengambil function_definition
function_node = tree.root_node.named_children[0]

print("\nChildren dari function_definition:")
for c in function_node.children:
    print(c.type, "bernama" if c.is_named else "anonim")

# Mengambil node parameters
parameters_node = function_node.named_children[1]

print("\nChildren dari parameters:")
for c in parameters_node.children:
    print(c.type, "bernama" if c.is_named else "anonim")