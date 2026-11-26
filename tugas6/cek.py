import sys
from pathlib import Path
import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

Q_TODO = Query(PY, '((comment) @c (#match? @c "TODO|FIXME"))')

Q_FUNC = Query(PY, '(function_definition name: (identifier) @nama) @fungsi')

def cari_error(node):
    if node.is_error or node.is_missing:
        return node

    for child in node.children:
        hasil = cari_error(child)
        if hasil:
            return hasil

    return None

def cek_file(path):
    tree = parser.parse(path.read_bytes())

    # Fitur 1: komentarTODO/FIXME (sudah jadi)
    for node in QueryCursor(Q_TODO).captures(tree.root_node).get("c", []):
        print(f"{path}:{node.start_point[0] + 1}:{node.text.decode().strip()}")

    # Fitur 2 (TODO): fungsi yang lebih dari 30 baris
    matches = QueryCursor(Q_FUNC).matches(tree.root_node)

    for pattern_index, captures in matches:
        nama_node = captures["nama"][0]
        fungsi_node = captures["fungsi"][0]

        nama = nama_node.text.decode(errors="replace")
        jumlah_baris = (
            fungsi_node.end_point[0]
            - fungsi_node.start_point[0]
            + 1
        )

        if jumlah_baris > 30:
            print(
                f"{path}:{fungsi_node.start_point[0] + 1}: "
                f"Fungsi '{nama}' memiliki {jumlah_baris} baris"
            )
    # Fitur 3 (TODO): file yang pohonnya mengandung error
        # Fitur 3: deteksi syntax error
    if tree.root_node.has_error:
        error_node = cari_error(tree.root_node)

        if error_node:
            baris = error_node.start_point[0] + 1

            print(
                f"{path}:{baris}: "
                f"Syntax error ditemukan pada node '{error_node.type}'"
            )
for path in Path(sys.argv[1]).rglob("*.py"):
    cek_file(path)
