def kategori_usia(usia):
    if usia < 12:
        return "Anak-anak"
    elif usia <= 17:
        return "Remaja"
    elif usia <= 59:
        return "Dewasa"
    else:
        return "Lansia"


# Input dari pengguna
usia = int(input("usia kamu berapa: "))
print("kamu itu:", kategori_usia(usia))
