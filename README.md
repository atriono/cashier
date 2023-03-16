# cashier
Berisi mengenai script python untuk mengakomodasi kebutuhan transaksi di cashier. Berisi fungsi menambahkan barang, merubah barang, menghapus barang, mengecek belanjaan hingga total belanja dan diskonnya.

# Latar Belakang
Program dibuat ini berdasarkan keingainan Andi seorang pemilik supermarket besar di salah satu kota di iIndonesia. Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu Andi akan membuat sistem kasir yang self-servie di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain. 

# Objectives
begini journey Customer dalam membantu orang yang berbelanja tersebut:
1.	Customer membuat ID transaksi customer
2.	Kemudian, Customer memasukkan nama item, jumlah item, dan harga barang.
3.	Jika ternyata ada kesalahan dalam memasukkan nama item atau jumlah item atau harga item tetapi tidak ingin menghapus itemnya, Customer bisa melakukan:
  a.	Update nama item
  b.	Update jumlah item 
  c.	Update harga item
4.	Jika batal membeli item belanjaan, Customer bisa melakukan:
  a.  Menghapus salah satu item dari nama item
  b.  Langsung menghapus semua transaksi atau reset transaksi dengan method
5.  Customer sudah selesai dengan berbelanja online nya, tetapi Customer masih ragu apakah harga barang dan nama barang yang diinput sudah benar. Bisa saja Customer melakukan kesalahan dalam melakukan input, semisal sudah melakukan input harga barang tetapi lupa untuk input nama barangnya.
6.  Setelah melakukan pengecekan, Customer bisa menghitung total belanja yang sudah dibeli. Andi bisa menggunakan method total_price (). Pada supermarket ini ternyata terdapat ketentuan:
a.	Jika total belanja Andi diatas Rp 200.000 maka akan mendapatkan diskon 5%
b.	Jika total belanja Andi diatas Rp 300.000 maka akan mendapatkan diskon 8%
c.	Jika total belanja Andi diatas Rp 500.000 maka akan mendapatkan diskon 10%

# Alur Program
1. Program dimulai dengan mendeklarasikan variabel untuk mendampung data transaksi yaitu trnsct_123 = {}
2. membuat fungsi untuk menambahkan data transaksi ke variabel
3. membuat fungsi untuk mengupdate nama item ke variabel
4. membuat fungsi untuk mengupdate jumlah item ke variabel
5. membuat fungsi untuk mengupdate harga item ke variabel
6. membuat fungsi untuk menghapus item
7. membuat fungsi untuk mereset transaksi
8. membuat fungsi untuk mencetak transaksi
9. membuat fungsi untuk menghitung total belanjaan
10. menghitung total yang harus dibayar setelah diskon

# Fungsi Dalam Program
1. fungsi add_item(nama_item, jumlah_item, harga_per_item) yang berguna untuk menambahkan data transaksi ke variabel
2. fungsi update_item_name(nama_item, update_nama_item) yang berguna untuk mengupdate nama item ke variabel
3. fungsi update_item_qty(nama_item, update_jumlah_item) yang berguna untuk mengupdate jumlah item ke variabel
4. fungsi update_item_price(nama_item, update_harga_item) yang berguna untuk mengupdate harga item ke variabel
5. fungsi delete_item(nama_item) yang berguna untuk menghapus item
6. fungsi reset_transaction() yang berguna untuk mereset transaksi
7. fungsi check_order() yang berguna untuk mencetak transaksi
8. fungsi total_price() yang berguna untuk menghitung total belanjaan dan total bayar

# Test Case
cashier.add_item('ayam goreng',2, 20000)
  --> Item yang dibeli adalah:  {'ayam goreng': [2, 20000]}

cashier.add_item('pasta gigi',3, 15000)
  --> Item yang dibeli adalah:  {'ayam goreng': [2, 20000], 'pasta gigi': [3, 15000]}

cashier.delete_item('pasta gigi')
  --> item pasta gigi  berhasil dihapus

cashier.reset_transaction()
  --> Semua item berhasil di delete!

cashier.add_item('Ayam Goreng',2, 20000)
  --> Item yang dibeli adalah:  {'Ayam Goreng': [2, 20000]}

cashier.add_item('Pasta Gigi',3, 15000)
  --> Item yang dibeli adalah:  {'Ayam Goreng': [2, 20000], 'Pasta Gigi': [3, 15000]}

cashier.add_item('Mainan Mobil',1, 200000)
  --> Item yang dibeli adalah:  {'Ayam Goreng': [2, 20000], 'Pasta Gigi': [3, 15000], 'Mainan Mobil': [1, 200000]}

cashier.add_item('Mi Instan',5, 3000)
  --> Item yang dibeli adalah:  {'Ayam Goreng': [2, 20000], 'Pasta Gigi': [3, 15000], 'Mainan Mobil': [1, 200000], 'Mi Instan': [5, 3000]}

cashier.total_price()
  --> Total belanja yang harus dibayarkan adalah  285000.0
cashier.check_order()
  --> {'Ayam Goreng': [2, 20000], 'Pasta Gigi': [3, 15000], 'Mainan Mobil': [1, 200000], 'Mi Instan': [5, 3000]}

# Conlusion
Program ini telah selesai dibuat dan sudah dilakukan testcase dan dapat digunakan untuk sistem kasir yang self-servie di supermarket. Semoga bermanfaat
