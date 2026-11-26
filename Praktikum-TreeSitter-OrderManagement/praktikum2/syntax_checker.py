import tree_sitter_python as tspython
from tree_sitter import Language, Parser

PYTHON_LANGUAGE = Language(tspython.language())
parser = Parser(PYTHON_LANGUAGE)

with open("praktikum2/syntax_error_test.py", "r") as file:
    source_code = file.read()

tree = parser.parse(source_code.encode("utf-8"))

print("Source Code:")
print(source_code)

print("\nCST Tree:")
print(tree.root_node)

print("\nSyntax Error Check:")
print("Root has error:", tree.root_node.has_error)

def check_errors(node):
    if node.type == "ERROR":
        print("ERROR node found:", node)

    if node.is_missing:
        print("MISSING node found:", node)

    for child in node.children:
        check_errors(child)

check_errors(tree.root_node)