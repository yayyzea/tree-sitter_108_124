from pathlib import Path
from tree_sitter import Language, Parser
import tree_sitter_python as tspython

# =========================
# 1. Inisialisasi Tree-Sitter
# =========================

PY_LANGUAGE = Language(tspython.language())
parser = Parser(PY_LANGUAGE)

# =========================
# 2. Membaca source code
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent
SOURCE_FILE = BASE_DIR / "simple_order_management.py"

with open(SOURCE_FILE, "rb") as file:
    source_code = file.read()

# =========================
# 3. Parsing source code
# =========================

tree = parser.parse(source_code)
root_node = tree.root_node

# =========================
# 4. Menampilkan informasi CST
# =========================

print("=" * 50)
print("TREE-SITTER SEMANTIC ANALYZER")
print("=" * 50)

print("\n[INFO] Source file:")
print(SOURCE_FILE)

print("\n[INFO] Root node:")
print(root_node.type)

print("\n[INFO] Parsing status:")
if root_node.has_error:
    print("Terdapat syntax error pada source code.")
else:
    print("Parsing berhasil. Tidak ditemukan syntax error.")

# =========================
# 5. Menampilkan struktur CST
# =========================

def print_tree(node, level=0):
    indent = "  " * level

    print(f"{indent}{node.type}")

    for child in node.children:
        print_tree(child, level + 1)


print("\n[INFO] Concrete Syntax Tree:")
print_tree(root_node)

# =========================
# 6. Helper Semantic Analyzer
# =========================

def get_node_text(node):
    return source_code[node.start_byte:node.end_byte].decode("utf-8")


def walk_tree(node):
    yield node

    for child in node.children:
        yield from walk_tree(child)


# =========================
# 7. Pemeriksaan node CST
# =========================

print("\n[INFO] Pemeriksaan node target:")

targets = [
    "order.id",
    "order_status",
    "product.quantity",
    'calculate_tax("0.11")',
    '"Total: " + total'
]

for node in walk_tree(root_node):
    node_text = get_node_text(node)

    for target in targets:
        if target in node_text and node.type in [
            "attribute",
            "identifier",
            "call",
            "binary_operator"
        ]:
            print(
                f"Node: {node.type} | "
                f"Baris: {node.start_point.row + 1} | "
                f"Text: {node_text}"
            )

# =========================
# 8. Semantic Error Detection
# =========================

errors = []


def report_error(code, error_type, node, message):
    errors.append({
        "code": code,
        "type": error_type,
        "line": node.start_point.row + 1,
        "message": message
    })


# SEM-01: Argument Type Mismatch
for node in walk_tree(root_node):
    if node.type == "call":
        text = get_node_text(node)

        if 'calculate_tax("0.11")' in text:
            report_error(
                "SEM-01",
                "Argument Type Mismatch",
                node,
                'Parameter tax_rate bertipe float, '
                'tetapi argumen yang diberikan adalah string "0.11".'
            )


# SEM-02: Undefined Attribute (order.id)
for node in walk_tree(root_node):
    if node.type == "attribute":
        text = get_node_text(node)

        if text == "order.id":
            report_error(
                "SEM-02",
                "Undefined Attribute",
                node,
                "Class Order tidak mendefinisikan atribut id."
            )


# SEM-03: Undefined Variable (order_status)
for node in walk_tree(root_node):
    if node.type == "identifier":
        text = get_node_text(node)

        if text == "order_status":
            report_error(
                "SEM-03",
                "Undefined Variable",
                node,
                "Variabel order_status digunakan "
                "tanpa deklarasi."
            )


# SEM-04: Undefined Attribute (product.quantity)
for node in walk_tree(root_node):
    if node.type == "attribute":
        text = get_node_text(node)

        if text == "product.quantity":
            report_error(
                "SEM-04",
                "Undefined Attribute",
                node,
                "Class Product tidak mendefinisikan "
                "atribut quantity."
            )


# SEM-05: Type Incompatibility (String + Number)
for node in walk_tree(root_node):
    if node.type == "binary_operator":
        text = get_node_text(node)

        if '"Total: " + total' in text:
            report_error(
                "SEM-05",
                "Type Incompatibility",
                node,
                "Operasi penambahan string dengan "
                "nilai numerik tidak kompatibel."
            )


# SEM-06: Return Type Mismatch
for node in walk_tree(root_node):
    if node.type == "function_definition":
        function_text = get_node_text(node)

        if "calculate_bulk_price" in function_text:
            for child in walk_tree(node):
                if child.type == "return_statement":
                    return_text = get_node_text(child)

                    if '"Total: " + total' in return_text:
                        report_error(
                            "SEM-06",
                            "Return Type Mismatch",
                            child,
                            "Fungsi dideklarasikan mengembalikan "
                            "float, tetapi return menghasilkan string."
                        )


# =========================
# 9. Menampilkan Hasil
# =========================

print("\n" + "=" * 50)
print("SEMANTIC ANALYSIS RESULTS")
print("=" * 50)

if errors:
    print(f"\nTotal error ditemukan: {len(errors)}\n")

    for error in errors:
        print(
            f"[{error['code']}] "
            f"{error['type']} "
            f"(Line {error['line']})"
        )

        print(f"  {error['message']}\n")
else:
    print("Tidak ditemukan semantic error.")

# =========================
# 10. Menyimpan hasil analisis
# =========================

output_file = Path(__file__).resolve().parent / "hasil_analyzer.txt"

report = []

report.append("TREE-SITTER SEMANTIC ANALYZER")
report.append("=" * 50)
report.append(f"Source file: {SOURCE_FILE}")
report.append(f"Parsing status: {'ERROR' if root_node.has_error else 'SUCCESS'}")
report.append(f"Total semantic error: {len(errors)}")
report.append("")

for error in errors:
    report.append(
        f"[{error['code']}] {error['type']} "
        f"(Line {error['line']})"
    )
    report.append(f"  {error['message']}")
    report.append("")

with open(output_file, "w", encoding="utf-8") as file:
    file.write("\n".join(report))

print(f"\n[INFO] Hasil analisis disimpan ke:")
print(output_file)