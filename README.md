**Penjelasan Kode Toko Sembako**

**1. Pendahuluan**

Program ini dirancang untuk membantu pengelola toko sembako dalam melacak inventaris produk. Kode ini ditulis dalam bahasa pemrograman Python dan terstruktur ke dalam tiga kelas utama: `Data`, `View`, dan `Proses`.

**2. Kelas Data**

  - **`__init__(self)`:**

      - Menginisialisasi atribut `products` sebagai daftar kosong untuk menyimpan informasi produk.

  - **`add_product(self, name, price, quantity)`:**

      - Menambahkan produk baru ke dalam daftar `products`.
      - Memvalidasi harga dan jumlah produk agar tidak negatif.
      - Memformat informasi produk menjadi kamus dengan key `'name'`, `'price'`, dan `'quantity'`.
      - Menambahkan kamus produk ke dalam daftar `products`.
      - Mencetak pesan konfirmasi penambahan produk.

  - **`get_products(self)`:**

      - Mengembalikan seluruh isi daftar `products`.

**3. Kelas View**

  - **`@staticmethod`:**

      - Menandakan bahwa metode `display_products` tidak memerlukan inisialisasi objek `View`.

  - **`display_products(products)`:**

      - Mencetak header tabel daftar produk toko sembako.
      - Mencetak format kolom untuk "Nama Produk", "Harga", dan "Jumlah".
      - Iterasi melalui setiap produk dalam daftar `products`.
      - Mencetak informasi produk dalam format tabel yang rapi.
      - Mencetak garis pembatas bawah tabel.

**4. Kelas Proses**

  - **`__init__(self)`:**

      - Menginisialisasi objek `Data` untuk mengelola data produk.

  - **`input_product(self)`:**

      - Memulai loop interaktif untuk penambahan produk.
      - Meminta pengguna memasukkan nama, harga, dan jumlah produk secara berulang.
      - Memvalidasi input pengguna agar harga dan jumlah tidak negatif.
      - Menangani kesalahan `ValueError` jika input tidak valid.
      - Memanggil metode `add_product` dari objek `data` untuk menambahkan produk baru.
      - Mencetak pesan konfirmasi penambahan produk.
      - Menanyakan pengguna apakah ingin menambah produk lagi.
      - Keluar dari loop jika pengguna tidak ingin menambah produk lagi.

  - **`show_products(self)`:**

      - Mengambil daftar produk dari objek `data`.
      - Memanggil metode `display_products` dari kelas `View` untuk menampilkan daftar produk jika ada.
      - Mencetak pesan jika tidak ada produk yang terdaftar.

**5. Blok `if __name__ == "__main__":`**

  - Memastikan kode di dalam blok ini hanya dieksekusi ketika program dijalankan secara langsung (bukan diimpor sebagai modul).
  - Menginisialisasi objek `Proses` bernama `proses`.
  - Memanggil metode `input_product` dari objek `proses` untuk memungkinkan pengguna menambah produk.
  - Memanggil metode `show_products` dari objek `proses` untuk menampilkan daftar produk yang telah ditambahkan.
  - ![photo](https://github.com/Moviezal/UAS-1/blob/e354241358b98acbb2534aa728d29e5a51e84ddb/Output.jpeg)

**6. Kesimpulan**

Program ini menyediakan sistem sederhana untuk pengelola toko sembako dalam mengelola inventaris produk. Pengguna dapat menambah produk baru, lengkap dengan nama, harga, dan jumlah stok. Program ini juga menampilkan daftar produk yang terdaftar dalam format tabel yang mudah dibaca.
