# Simpan dengan nama: layanan_hp.py

class Handphone:
    def __init__(self, merk, model, harga, stok):
        """Inisialisasi atribut HP"""
        self.merk = merk
        self.model = model
        self.harga = harga
        self.stok = stok

    def tampilkan_info(self):
        """Menampilkan detail produk"""
        print(f"Merk  : {self.merk}")
        print(f"Model : {self.model}")
        print(f"Harga : Rp{self.harga:,}")
        print(f"Stok  : {self.stok} unit")
        print("-" * 20)

    def restock(self, jumlah):
        """Menambah stok barang"""
        self.stok += jumlah
        print(f"Stok {self.model} berhasil ditambah sebanyak {jumlah}.")

    def kurangi_stok(self, jumlah):
        """Logika pengurangan stok saat terjual"""
        if self.stok >= jumlah:
            self.stok -= jumlah
            return True
        return False