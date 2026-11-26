import tree_sitter_python as tspython
from tree_sitter import Language, Parser

PYTHON_LANGUAGE = Language(tspython.language())
parser = Parser(PYTHON_LANGUAGE)

codes = {
    "Code 1 - Function": """
def tambah(a, b):
    return a + b
""",

    "Code 2 - If Else": """
if x > 0:
    print("positif")
else:
    print("non-positif")
""",

    "Code 3 - Class": """
class Mahasiswa:
    def belajar(self):
        print("Belajar Python")
"""
}

for title, code in codes.items():
    print("=" * 50)
    print(title)
    print("=" * 50)

    tree = parser.parse(code.encode("utf-8"))
    print(tree.root_node)
    print()