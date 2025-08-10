import time
print("hesap makinesine hoş geldiniz")
time.sleep(1)
print("hesap makinesi çalışıyor...")
time.sleep(2)
print("işelemler için lütfen aşağıdaki seçeneklerden birini seçiniz:")
print("1. Toplama")
print("2. Çıkarma")
print("3. çarpma")
print("4. bölme")
secim = input("seçiminizi giriniz (1/2/3/4): ")
if secim == '1':
    sayi1 = float(input("ilk sayıyı giriniz: "))
    sayi2 = float(input("ikinci sayıyı giriniz: "))
    print("sonuç: ", sayi1 + sayi2)
elif secim == '2':
    sayi1 = float(input("ilk sayıyı giriniz:"))
    sayi2 = float(input("ikinci sayıyı giriniz: "))
    print("sonuç: ", sayi1 - sayi2)
elif secim == '3':
    sayi1 = float(input("ilk sayıyı giriniz: "))
    sayi2 = float(input("ikinci sayıyı giriniz:"))
    print("sonuç: ", sayi1 * sayi2)
elif secim == '4':
    sayi1 = float(input("ilk sayıyı giriniz: "))
    sayi2 = float(input("ikinci sayıyı giriniz: "))
    print("sonuç: ", sayi1 / sayi2)
else:
    print("geçersiz seçim, lütfen 1, 2, 3 veya 4 giriniz.")
