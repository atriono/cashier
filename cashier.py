# %%
#mendeklarasikan variabel untuk mendampung data transaksi
trnsct_123 = {}

#membuat fungsi untuk menambahkan data transaksi ke variabel
def add_item(nama_item, jumlah_item, harga_per_item):
    trnsct_123.update({nama_item: [jumlah_item, harga_per_item]})
    print('Item yang dibeli adalah: ', trnsct_123) 

#membuat fungsi untuk mengupdate nama item ke variabel
def update_item_name(nama_item, update_nama_item):
    # menambahkan nama item yang baru dan menampilkan jumlah dan harga yang lama
    nama_item_baru = update_nama_item
    data_item_baru = trnsct_123[nama_item]
    # menghapus data item yang lama
    trnsct_123.pop(nama_item)
    # mengupdate nama item yang baru dengan jumlah dan harga yang lama
    trnsct_123.update({nama_item_baru: data_item_baru})
    print('item ', nama_item, ' sudah berubah menjai ', nama_item_baru) 

#membuat fungsi untuk mengupdate jumlah item ke variabel
def update_item_qty(nama_item, update_jumlah_item):
    # menambahkan jumlah item yang baru dan menampilkan harga yang lama
    data_item_baru = [update_jumlah_item, trnsct_123[nama_item][1]]
    # mengupdate jumlah item yang baru dengan harga yang lama
    trnsct_123.update({nama_item:  data_item_baru})
    print('jumlah item ', nama_item, ' berhasil dirubah') 

def update_item_price(nama_item, update_harga_item):
    # menambahkan harga item yang baru dan menampilkan jumlah yang lama
    data_item_baru = [trnsct_123[nama_item][0], update_harga_item]
    # mengupdate harga item yang baru dengan jumlah yang lama
    trnsct_123.update({nama_item:  data_item_baru})
    print(trnsct_123) 

def delete_item(nama_item):
    # menghapus item
    trnsct_123.pop(nama_item)
    print('item' , nama_item, ' berhasil dihapus') 

def reset_transaction():
    # mereset transaksi
    trnsct_123.clear()
    print('Semua item berhasil di delete!') 

def check_order():
    # mencetak data order
    print(trnsct_123) 

def total_price():
    # membuat list nama item
    item_keys = list(trnsct_123.keys())
    # menghitung jumlah item
    jml_row = len(item_keys)
    # membuat list kosong untuk menampung perkalian jumlah dan harga 
    total_price_item = []

    # melakukan perhitung perkalian jumlah dan harga sesuai per item
    # hasilnya ditambahkan ke list total price
    for i in range (jml_row):
        total_price_item.append(trnsct_123[item_keys[i]][0] * trnsct_123[item_keys[i]][1])

    # menjumlahkan list total price
    total_trans = sum(total_price_item)

    # membuat kriteria diskon
    if total_trans > 500000:
        discount = 0.1
    elif total_trans > 300000:
        discount = 0.08
    elif total_trans > 200000:
        discount = 0.05

    # mennghitung total yang harus dibayar setelah diskon
    total_bayar = total_trans * (1- discount)
    # mencetak total belanja yang harus dibayar
    print('Total belanja yang harus dibayarkan adalah ', total_bayar)


