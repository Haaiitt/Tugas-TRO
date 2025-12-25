from pulp import *
import numpy as np # Digunakan untuk fungsi pembulatan saat menampilkan hasil

# =========================================================
# 1. DEFINISI MASALAH DAN VARIABEL
# =========================================================

# Mendefinisikan masalah sebagai Maksimisasi Keuntungan
prob = LpProblem("Penjadwalan_Produksi_Agro_Jaya", LpMaximize)

# Mendefinisikan Variabel Keputusan (XA, XB, XC)
# Batasan minimum produksi dimasukkan langsung ke lowBound.
XA = LpVariable("XA_Roti_Manis", lowBound=1000, cat='Continuous') 
XB = LpVariable("XB_Biskuit", lowBound=500, cat='Continuous')
XC = LpVariable("XC_Snack_Ringan", lowBound=800, cat='Continuous')

# =========================================================
# 2. FUNGSI TUJUAN (OBJECTIVE FUNCTION)
# =========================================================

# Max Z = 5000 XA + 7000 XB + 4000 XC
prob += 5000 * XA + 7000 * XB + 4000 * XC, "Total_Keuntungan"

# =========================================================
# 3. KENDALA (CONSTRAINTS)
# =========================================================

# Kendala Kapasitas Mesin (Semua <= Kapasitas Maksimal)
# Data: XA=0.015, XB=0.010, XC=0.005 | Kapasitas=100
prob += 0.015 * XA + 0.010 * XB + 0.005 * XC <= 100, "Kapasitas_M1_Pencampuran"
# Data: XA=0.025, XB=0.020, XC=0.010 | Kapasitas=120
prob += 0.025 * XA + 0.020 * XB + 0.010 * XC <= 120, "Kapasitas_M2_Pemanggangan"
# Data: XA=0.010, XB=0.010, XC=0.015 | Kapasitas=90
prob += 0.010 * XA + 0.010 * XB + 0.015 * XC <= 90, "Kapasitas_M3_Pengemasan"

# Kendala Minimum (sudah diatur di lowBound variabel)

# =========================================================
# 4. SOLVE DAN TAMPILKAN HASIL
# =========================================================

# Menyelesaikan model
prob.solve()

# =========================================================
# TAMPILAN OUTPUT
# =========================================================
print("=" * 70)
print("HASIL SOLUSI OPTIMASI PRODUKSI PABRIK AGRO JAYA (PU LP)")
print("=" * 70)

# 1. Status Solusi dan Keuntungan Maksimum
print(f"Status Solusi: {LpStatus[prob.status]}")
keuntungan_max = value(prob.objective)
print(f"Keuntungan Maksimum (Z): Rp {keuntungan_max:,.0f}")
print("-" * 70)

# 2. Nilai Variabel Keputusan (Unit Produksi Optimal)
print("Kuantitas Produksi Optimal:")
for v in prob.variables():
    # Menggunakan np.ceil untuk membulatkan ke atas jika produksi harus integer
    # atau np.round jika produksi boleh pecahan (Continuous)
    # Karena cat='Continuous', kita biarkan hasilnya dengan dua desimal.
    print(f"- {v.name}: {v.varValue:,.2f} Unit")

# 3. Analisis Kendala (Slack/Bottleneck)
print("-" * 70)
print("Analisis Kapasitas Mesin (Slack/Sisa Waktu):")
for name, c in prob.constraints.items():
    # c.slack akan menunjukkan sisa kapasitas (0 jika terikat/bottleneck)
    print(f"- {name}: Slack = {c.slack:,.2f} Jam")
print("=" * 70)