class Data:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        product = {
            'name': name,
            'price': price,
            'quantity': quantity
        }
        self.products.append(product)

    def get_products(self):
        return self.products



class View:
    @staticmethod
    def display_products(products):
        print("\nDaftar Produk Toko Sembako:")
        print("{:<20} {:<10} {:<10}".format("Nama Produk", "Harga", "Jumlah"))
        print("-" * 40)
        for product in products:
            print("{:<20} {:<10} {:<10}".format(product['name'], product['price'], product['quantity']))
        print("-" * 40)


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


if __name__ == "__main__":
    proses = Proses()
    proses.input_product()
    proses.show_products()
