from pathlib import Path
from tree_sitter import Language, Parser
import tree_sitter_python

PYTHON = Language(tree_sitter_python.language())
parser = Parser(PYTHON)

BASE_DIR = Path(__file__).resolve().parent.parent
SOURCE_FILE = BASE_DIR / "simple_order_management.py"

source_code = SOURCE_FILE.read_bytes()
tree = parser.parse(source_code)
root = tree.root_node


def get_text(node):
    return source_code[node.start_byte:node.end_byte].decode("utf-8")


print("=" * 60)
print("RINGKASAN CST")
print("=" * 60)


def walk(node):
    if node.type == "class_definition":
        name = node.child_by_field_name("name")
        print(f"\nCLASS: {get_text(name)}")

    elif node.type == "function_definition":
        name = node.child_by_field_name("name")
        parameters = node.child_by_field_name("parameters")
        print(f"\nFUNCTION: {get_text(name)}")
        print(f"PARAMETERS: {get_text(parameters)}")

    elif node.type == "call":
        function = node.child_by_field_name("function")
        arguments = node.child_by_field_name("arguments")
        print(f"CALL: {get_text(function)}")
        if arguments:
            print(f"ARGUMENTS: {get_text(arguments)}")

    for child in node.children:
        walk(child)


walk(root)
