def hitung_kalimat(teks):
    vokal = "aiueo"
    jumlah_vokal = 0
    jumlah_konsonan = 0

    for huruf in teks.lower():
        if huruf.isalpha():
            if huruf in vokal:
                jumlah_vokal += 1
            else:
                jumlah_konsonan += 1

    jumlah_kata = len(teks.split())

    print("Vokal:", jumlah_vokal)
    print("Konsonan:", jumlah_konsonan)
    print("Kata:", jumlah_kata)

# Input dari pengguna
kalimat = input("tolong masukan kalimatnya: ")
hitung_kalimat(kalimat)