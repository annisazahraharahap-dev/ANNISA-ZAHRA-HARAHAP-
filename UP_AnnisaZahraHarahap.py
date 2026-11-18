HARGA = {"1": ("Reguler", 35000), "2": ("VIP", 50000), "3": ("Premium", 75000)}

lanjut = "y"
while lanjut.lower() == "y":
    nama = input("Nama pelanggan: ")

    print("1. Reguler (Rp35.000)")
    print("2. VIP (Rp50.000)")
    print("3. Premium (Rp75.000)")
    pilihan = input("Pilih jenis tiket (1/2/3): ")
    jumlah = int(input("Jumlah tiket: "))

    if pilihan in HARGA:
        jenis, harga = HARGA[pilihan]
        total = harga * jumlah

        if jumlah > 3:
            diskon = total * 0.10
            total -= diskon
        else:
            diskon = 0

        print("=== STRUK PEMESANAN ===")
        print(f"Nama   : {nama}")
        print(f"Tiket  : {jenis}")
        print(f"Jumlah : {jumlah}")
        print(f"Diskon : Rp{diskon:,.0f}")
        print(f"Total  : Rp{total:,.0f}")
    else:
        print("Jenis tiket tidak valid!")

    lanjut = input("Layani pelanggan lain? (y/n): ")
    