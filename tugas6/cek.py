import sys
from pathlib import Path

import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

Q_TODO = Query(
    PY,
    '((comment) @c (#match? @c "TODO|FIXME"))'
)

Q_FUNC = Query(
    PY,
    '(function_definition name: (identifier) @nama) @fungsi'
)

SKIP_DIRS = {".git", "venv", ".venv", "node_modules"}


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

    # Fitur 1: deteksi TODO/FIXME
    todo_nodes = QueryCursor(Q_TODO).captures(
        tree.root_node
    ).get("c", [])

    for node in todo_nodes:
        komentar = node.text.decode(errors="replace").strip()
        print(f"{path}:{node.start_point[0] + 1}: {komentar}")

    # Fitur 2: fungsi lebih dari 30 baris
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

    # Fitur 3: deteksi syntax error
    if tree.root_node.has_error:
        error_node = cari_error(tree.root_node)

        if error_node:
            baris = error_node.start_point[0] + 1

            print(
                f"{path}:{baris}: "
                f"Syntax error pada node '{error_node.type}'"
            )


def main():
    if len(sys.argv) != 2:
        print("Penggunaan: python cek.py <folder>")
        sys.exit(1)

    folder = Path(sys.argv[1])

    if not folder.exists():
        print(f"Folder tidak ditemukan: {folder}")
        sys.exit(1)

    if not folder.is_dir():
        print(f"Path bukan folder: {folder}")
        sys.exit(1)

    for path in folder.rglob("*.py"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue

        cek_file(path)


if __name__ == "__main__":
    main()