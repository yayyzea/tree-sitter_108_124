
import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))

kode = b"""
nilai = 85

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak Lulus")
"""

tree = parser.parse(kode)


def tampilkan_tree(node, kedalaman=0, field=None):
    indentasi = "  " * kedalaman

    label = f"{field}: " if field else ""

    print(f"{indentasi}{label}{node.type}")

    for i, child in enumerate(node.children):
        nama_field = node.field_name_for_child(i)

        tampilkan_tree(
            child,
            kedalaman + 1,
            nama_field
        )


print("Hasil Syntax Tree:")
tampilkan_tree(tree.root_node)

print("\nApakah terdapat syntax error?")
print(tree.root_node.has_error)

# Tugas 1 - Bagian 2: Mengidentifikasi Named Nodes dan Anonymous Nodes.
print("\nIdentifikasi Named dan Anonymous Nodes:")

if_node = tree.root_node.named_children[1]

for child in if_node.children:
    jenis = "Named" if child.is_named else "Anonymous"
    print(f"{child.type}: {jenis}")


def cari_anonymous(node):
    for child in node.children:
        if not child.is_named:
            print(child.type)

        cari_anonymous(child)


print("\nSeluruh Anonymous Nodes:")
cari_anonymous(tree.root_node)


# Pengujian Syntax Error
kode_error = b"""
nilai = 85

if nilai >= 75
    print("Lulus")
else:
    print("Tidak Lulus")
"""

tree_error = parser.parse(kode_error)

print("\nPengujian Syntax Error:")
print("Apakah terdapat error?")
print(tree_error.root_node.has_error)


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

