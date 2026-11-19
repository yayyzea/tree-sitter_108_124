
import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))

# Contoh kode dengan Syntax Error
kode_error = b"""
nilai = 85

if nilai >= 75
    print("Lulus")
else:
    print("Tidak Lulus")
"""

tree_error = parser.parse(kode_error)


# Memeriksa Syntax Error
print("Pengujian Syntax Error:")
print("Apakah terdapat error?")
print(tree_error.root_node.has_error)


# Mencari Node ERROR dan MISSING
def cari_error(node):
    if node.is_error or node.is_missing:
        jenis = "ERROR" if node.is_error else "MISSING"

        print(
            f"{jenis}: {node.type}, "
            f"baris {node.start_point[0] + 1}"
        )

    for child in node.children:
        cari_error(child)


print("\nDetail Node Error:")
cari_error(tree_error.root_node)
