import sys
import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

kode = open(sys.argv[1], "rb").read()
pola = open(sys.argv[2]).read()

tree = parser.parse(kode)

hasil = QueryCursor(Query(PY, pola)).matches(tree.root_node)

for _, cap in hasil:
    for nama_capture, nodes in cap.items():
        for n in nodes:
            print(
                f"@{nama_capture} "
                f"baris{n.start_point[0] + 1}:"
                f"{n.text.decode()}"
            )

    # Khusus query nama fungsi dan parameter
    if "nama" in cap and "params" in cap:
        nama = cap["nama"][0].text.decode()
        jumlah = cap["params"][0].named_child_count
        print(f"-> {nama}: {jumlah} parameter")