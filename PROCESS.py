
class Proses:
    def __init__(self):
        self.data = Data()

    def input_product(self):
        while True:
            try:
                name = input("Masukkan nama produk: ")
                price = float(input("Masukkan harga produk: "))
                quantity = int(input("Masukkan jumlah produk: "))

                if price < 0 or quantity < 0:
                    raise ValueError("Harga dan jumlah harus lebih besar atau sama dengan nol.")

                self.data.add_product(name, price, quantity)
                print(f"Produk '{name}' berhasil ditambahkan.")

                another = input("Apakah Anda ingin menambah produk lagi? (y/n): ")
                if another.lower() != 'y':
                    break
            except ValueError as e:
                print(f"Input tidak valid: {e}")

    def show_products(self):
        products = self.data.get_products()
        if products:
            View.display_products(products)
        else:
            print("Tidak ada produk yang terdaftar.")



