
import tree_sitter_python as tspython
from tree_sitter import Language, Parser

# Menyiapkan parser Python
parser = Parser(Language(tspython.language()))

# Kode sengaja dibuat salah: tanda ':' setelah sapa(nama) dihilangkan
kode = b"""
def sapa(nama)
    return "Halo, " + nama
"""

# Melakukan parsing
tree = parser.parse(kode)

# Menampilkan syntax tree
print("Syntax Tree:")
print(tree.root_node)

# Memeriksa apakah terdapat error
print("\nApakah terdapat error:", tree.root_node.has_error)

# Mencari node ERROR dan MISSING
def cari_error(node):
    if node.type == "ERROR" or node.is_missing:
        print(
            "Node:", node.type,
            "| Missing:", node.is_missing,
            "| Posisi:", node.start_point
        )

    for child in node.children:
        cari_error(child)

print("\nHasil pemeriksaan node:")
cari_error(tree.root_node)
