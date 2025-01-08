class View:
    @staticmethod
    def display_products(products):
        print("\nDaftar Produk Toko Sembako:")
        print("{:<20} {:<10} {:<10}".format("Nama Produk", "Harga", "Jumlah"))
        print("-" * 40)
        for product in products:
            print("{:<20} {:<10} {:<10}".format(product['name'], product['price'], product['quantity']))
        print("-" * 40)


