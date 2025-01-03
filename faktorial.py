# Nama: Ifah Fatmawati
# NIM: 2021150105

def hitung_faktorial(n):
    """
    Fungsi untuk menghitung faktorial dari sebuah angka.
    Parameter:
    n (int): Angka yang akan dihitung faktorialnya.
    Returns:
    int: Hasil faktorial dari n.
    """
    if n == 0:
        return 1
    else:
        return n * hitung_faktorial(n - 1)

def main():
    angka = int(input("Masukkan angka: "))
    hasil = hitung_faktorial(angka)
    print(f"Faktorial dari {angka} adalah {hasil}")

if __name__ == "__main__":
    main()
