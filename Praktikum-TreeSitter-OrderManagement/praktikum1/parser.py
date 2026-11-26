from pathlib import Path
from tree_sitter import Language, Parser
import tree_sitter_python

# Grammar Python
PYTHON = Language(tree_sitter_python.language())
parser = Parser(PYTHON)

# Lokasi source code yang akan dianalisis
BASE_DIR = Path(__file__).resolve().parent.parent
SOURCE_FILE = BASE_DIR / "simple_order_management.py"

# Parse source code
source_code = SOURCE_FILE.read_bytes()
tree = parser.parse(source_code)

# Root CST
root = tree.root_node

print("=" * 60)
print("TREE-SITTER PYTHON PARSER")
print("=" * 60)
print(f"File       : {SOURCE_FILE.name}")
print(f"Jumlah byte: {len(source_code)}")
print(f"Ada error  : {root.has_error}")
print()

# Menampilkan CST
print("CONCRETE SYNTAX TREE (CST)")
print("-" * 60)
print(root)

# Simpan CST ke file
OUTPUT_FILE = Path(__file__).resolve().parent / "hasil_cst.txt"
OUTPUT_FILE.write_text(str(root), encoding="utf-8")

print()
print(f"CST disimpan di: {OUTPUT_FILE}")

# Pemeriksaan syntax error
if root.has_error:
    print("\nSYNTAX ERROR DITEMUKAN")
else:
    print("\nTidak ditemukan syntax error oleh Tree-Sitter.")
