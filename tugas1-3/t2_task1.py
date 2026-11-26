import tree_sitter_python as tspython
from tree_sitter import Language, Parser

from t2_jelajah import jelajah

parser = Parser(Language(tspython.language()))

# Contoh kode dari Task 1
kode = b"x = 1+2\n"

tree = parser.parse(kode)

print("=== HASIL TREE-SITTER ===")
print(tree.root_node)

print("\n=== HASIL JELAJAH ===")
jelajah(tree.root_node)