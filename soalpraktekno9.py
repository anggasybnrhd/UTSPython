transaksi = [("Senin", 50000), ("Selasa", -20000), ("Rabu", 0), ("Kamis", 100000)]


saldo = sum(nominal for hari, nominal in transaksi)

pengeluaran = [(hari, nominal) for hari, nominal in transaksi if nominal < 0]
hari_pengeluaran_terbesar = pengeluaran[0][0] if pengeluaran else "Tidak ada"

hari_tanpa_transaksi = [hari for hari, nominal in transaksi if nominal == 0]
hari_tanpa_transaksi = hari_tanpa_transaksi[0] if hari_tanpa_transaksi else "Tidak ada"

print("Saldo akhir:", saldo)
print("Hari pengeluaran terbesar:", hari_pengeluaran_terbesar)
print("Hari tanpa transaksi:", hari_tanpa_transaksi)