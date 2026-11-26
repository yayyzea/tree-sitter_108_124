def tambah(a, b):

&#x20;   return a + b



module

└── function\_definition

&#x20;   ├── name: identifier (tambah)

&#x20;   ├── parameters

&#x20;   │   ├── identifier (a)

&#x20;   │   └── identifier (b)

&#x20;   └── body: block

&#x20;       └── return\_statement

&#x20;           └── binary\_operator

&#x20;               ├── identifier (a)

&#x20;               └── identifier (b)

## Perbandingan Derivasi Manual dengan CST Tree-Sitter

### Code 1 - Function

Hasil parsing Tree-Sitter menunjukkan struktur module yang berisi
function_definition. Node function_definition memiliki name,
parameters, dan body.

Bagian parameters berisi dua identifier, yaitu a dan b.
Body berisi return_statement yang di dalamnya terdapat binary_operator
dengan identifier a sebagai operand kiri dan identifier b sebagai operand kanan.

Hasil CST sesuai dengan derivasi manual dari segi struktur named nodes.


if x > 0:

&#x20;   print("positif")

else:

&#x20;   print("non-positif")



module

└── if\_statement

&#x20;   ├── condition: comparison\_operator

&#x20;   │   ├── identifier (x)

&#x20;   │   └── integer (0)

&#x20;   ├── consequence: block

&#x20;   │   └── expression\_statement

&#x20;   │       └── call

&#x20;   │           ├── function: identifier (print)

&#x20;   │           └── arguments: argument\_list

&#x20;   │               └── string ("positif")

&#x20;   └── alternative: else\_clause

&#x20;       └── block

&#x20;           └── expression\_statement

&#x20;               └── call

&#x20;                   ├── function: identifier (print)

&#x20;                   └── arguments: argument\_list

&#x20;                       └── string ("non-positif")

### Code 2 - If Else

Hasil parsing Tree-Sitter menunjukkan struktur if_statement
yang terdiri dari condition, consequence, dan alternative.

Condition direpresentasikan sebagai comparison_operator
yang memiliki identifier x dan integer 0.

Bagian consequence dan alternative masing-masing berisi block
dengan expression_statement berupa pemanggilan fungsi print.

Tree-Sitter memberikan representasi string yang lebih detail,
yaitu string_start, string_content, dan string_end.
Bagian else direpresentasikan melalui else_clause yang
memiliki body berupa block.

Hasil CST sesuai dengan derivasi manual secara struktur,
dengan beberapa detail node tambahan yang ditampilkan Tree-Sitter.

class Mahasiswa:

&#x20;   def belajar(self):

&#x20;       print("Belajar Python")



module

└── class\_definition

&#x20;   ├── name: identifier (Mahasiswa)

&#x20;   └── body: block

&#x20;       └── function\_definition

&#x20;           ├── name: identifier (belajar)

&#x20;           ├── parameters

&#x20;           │   └── identifier (self)

&#x20;           └── body: block

&#x20;               └── expression\_statement

&#x20;                   └── call

&#x20;                       ├── function: identifier (print)

&#x20;                       └── arguments: argument\_list

&#x20;                           └── string ("Belajar Python")

### Code 3 - Class dengan Method

Hasil parsing Tree-Sitter menunjukkan struktur class_definition
dengan identifier sebagai nama class, yaitu Mahasiswa.

Body class berisi function_definition yang merupakan method
belajar. Method memiliki parameters yang berisi identifier self
dan body berupa block.

Di dalam block terdapat expression_statement yang berisi
pemanggilan fungsi print. Argumen print berupa string
yang direpresentasikan melalui string_start, string_content,
dan string_end.

Hasil CST sesuai dengan derivasi manual secara struktur,
dengan detail tambahan pada node string.

### Eksperimen Syntax Error

Pengujian dilakukan dengan menghilangkan tanda titik dua (`:`) pada deklarasi fungsi Python.

Kode yang diuji:

```python
def tambah(a, b)
    return a + b
```

Tree-Sitter menghasilkan node `ERROR` pada CST. Hasil pemeriksaan menunjukkan `root_node.has_error` bernilai `True`, yang menandakan bahwa pohon syntax mengandung kesalahan.

Tree-Sitter tetap menghasilkan CST dengan menandai bagian yang bermasalah melalui node `ERROR`. Hal ini menunjukkan kemampuan Tree-Sitter dalam melakukan error recovery sehingga struktur kode masih dapat dianalisis meskipun terdapat syntax error.

Pada eksperimen ini, Tree-Sitter menghasilkan node `ERROR`, bukan `MISSING`.

**Kesimpulan:** Tree-Sitter mampu mendeteksi syntax error dan menandai bagian kode yang tidak sesuai dengan grammar Python melalui node `ERROR`.
