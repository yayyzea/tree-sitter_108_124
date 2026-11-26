# Analisis Kesalahan Source Code

## Source Code
Aplikasi Manajemen Order menggunakan Python.

## Hasil Identifikasi Kesalahan

| No | Lokasi | Jenis Kesalahan | Penjelasan |
|---|---|---|---|
| 1 | process_order() | Type mismatch | Parameter tax_rate menerima string "0.11", padahal seharusnya float. |
| 2 | find_order() | Undefined attribute | Atribut order.id tidak didefinisikan pada class Order. |
| 3 | generate_report() | Undefined variable | Variabel order_status digunakan tanpa deklarasi sebelumnya. |
| 4 | calculate_bulk_price() | Undefined attribute | Atribut product.quantity tidak didefinisikan pada class Product. |
| 5 | calculate_bulk_price() | Type mismatch | String "Total: " digabungkan dengan nilai numerik total menggunakan operator +. |
| 6 | calculate_bulk_price() | Return type mismatch | Fungsi memiliki deklarasi return type float, tetapi mengembalikan string. |

## Kesimpulan

Berdasarkan analisis source code, ditemukan beberapa potensi kesalahan semantik yang berkaitan dengan tipe data, penggunaan atribut objek, variabel yang belum didefinisikan, serta ketidaksesuaian tipe nilai return.

Kesalahan tersebut tidak semuanya terdeteksi hanya melalui pemeriksaan sintaks. Oleh karena itu, diperlukan Semantic Analyzer untuk melakukan pemeriksaan lebih lanjut terhadap source code dan struktur Concrete Syntax Tree (CST).