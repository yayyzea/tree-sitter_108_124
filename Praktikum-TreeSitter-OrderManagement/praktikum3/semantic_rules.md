# Semantic Analyzer Rules

## SEM-01 - Argument Type Mismatch
Memeriksa kesesuaian tipe data argumen yang diberikan pada pemanggilan fungsi atau method dengan tipe parameter yang dideklarasikan.

Target:
order.calculate_tax("0.11")

Expected:
tax_rate memiliki tipe float, tetapi argumen yang diberikan berupa string.

## SEM-02 - Undefined Object Attribute
Memeriksa penggunaan atribut objek yang tidak didefinisikan pada class terkait.

Target:
order.id

Expected:
Class Order tidak memiliki atribut id.

## SEM-03 - Undefined Variable
Memeriksa penggunaan variabel yang belum didefinisikan dalam scope yang relevan.

Target:
order_status

Expected:
order_status tidak ditemukan deklarasinya sebelum digunakan.

## SEM-04 - Undefined Object Attribute
Memeriksa penggunaan atribut objek yang tidak tersedia pada class terkait.

Target:
product.quantity

Expected:
Class Product tidak memiliki atribut quantity.

## SEM-05 - Type Incompatibility
Memeriksa operasi yang melibatkan tipe data tidak kompatibel dan kesesuaian nilai return dengan return type yang dideklarasikan.

Target:
"Total: " + total

Expected:
Operasi penambahan string dan numeric tidak kompatibel tanpa konversi.

Target:
calculate_bulk_price()

Expected:
Fungsi dideklarasikan mengembalikan float, tetapi menghasilkan string.
