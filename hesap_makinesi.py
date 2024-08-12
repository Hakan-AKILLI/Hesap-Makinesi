def hesap_makinesi():
    """Basit bir hesap makinesi fonksiyonu."""

    while True:
        print("\nİşlemi seçin:")
        print("1. Toplama")
        print("2. Çıkarma")
        print("3. Çarpma")
        print("4. Bölme")
        print("5. Çıkış")

        secim = input("Seçiminizi yapın (1/2/3/4/5): ")

        if secim == '5':
            print("Programdan çıkılıyor...")
            break

        if secim in ['1', '2', '3', '4']:
            try:
                sayi1 = float(input("İlk sayıyı girin: "))
                sayi2 = float(input("İkinci sayıyı girin: "))
            except ValueError:
                print("Geçersiz sayı girdiniz. Lütfen tekrar deneyin.")
                continue

            if secim == '1':
                sonuc = sayi1 + sayi2
                islem = "+"
            elif secim == '2':
                sonuc = sayi1 - sayi2
                islem = "-"
            elif secim == '3':
                sonuc = sayi1 * sayi2
                islem = "*"
            elif secim == '4':
                while sayi2 == 0:
                    print("Bir sayıyı sıfıra bölemezsiniz.")
                    sayi2 = float(input("İkinci sayıyı tekrar girin: "))
                sonuc = sayi1 / sayi2
                islem = "/"

            print(str(sayi1) + " " + islem + " " + str(sayi2) + " = " + str(sonuc))

        else:
            print("Geçersiz seçim. Lütfen 1-5 arasında bir değer girin.")

# Fonksiyonu çağırıyoruz
hesap_makinesi()

