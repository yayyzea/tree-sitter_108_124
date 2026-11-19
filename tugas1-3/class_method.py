import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))

kode = b"""
class Mahasiswa:
    def sapa(self):
        print("Halo")
"""

tree = parser.parse(kode)

# Menampilkan seluruh syntax tree
print(tree.root_node)

# Memeriksa children langsung dari root
print("\nChildren dari root:")
for c in tree.root_node.children:
    print(c.type, "bernama" if c.is_named else "anonim")

# Mengambil class_definition
class_node = tree.root_node.named_children[0]

# Mengambil block di dalam class_definition
class_body = class_node.named_children[1]

# Mengambil function_definition di dalam block
method_node = class_body.named_children[0]

print("\nChildren dari class_definition:")
for c in class_node.children:
    print(c.type, "bernama" if c.is_named else "anonim")

print("\nChildren dari function_definition:")
for c in method_node.children:
    print(c.type, "bernama" if c.is_named else "anonim")