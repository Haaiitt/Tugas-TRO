**LAPORAN PROYEK**

**Mata Kuliah Teknik Riset Oprasional**

![](./image1.png){width="2.6613188976377953in"
height="2.5844160104986877in"}

DiSusun Oleh:

  -----------------------------------------------------------------------
  NAMA                    : AHMAD HAITAMI
  ----------------------- -----------------------------------------------
  NIM                     : 231011401533

  KELAS                   : 05TPLM009
  -----------------------------------------------------------------------

Dosen Pengampu:

AGUNG PERDANANTO S.Kom, M.Kom.

**TEKNIK INFORMATIKA**

**FAKULTAS ILMU KOMPUTER**

**UNIVERSITAS PAMULANG**

LAPORAN PROYEK\
TEKNIK RISET OPERASIONAL

Judul Proyek : Analisis dan Optimasi Penjadwalan Produksi Menggunakan
*Linear Programming* Guna Meningkatkan Efisiensi Waktu di Pabrik Makanan
Agro Jaya.

Disusun oleh : AHMAD HAITAMI

NIM : 231011401533

Kelas : 05TPLM009

Dosen Pengampu : AGUNG PERDANANTO S.Kom, M.Kom

Program Studi : TEKNIK INFORMATIKA -- UNIVERSITAS PAMULANG

Tanggal Pengumpulan :

# PENDAHULUAN

## A. Latar Belakang Masalah

Efisiensi operasional merupakan kunci keberhasilan bagi industri
manufaktur, terutama di sektor makanan yang memiliki persaingan ketat
dan margin keuntungan yang sensitif terhadap biaya produksi. Pabrik
Makanan Agro Jaya menghadapi tantangan klasik dalam alokasi sumber daya:
bagaimana menentukan bauran produksi optimal untuk berbagai jenis produk
(Roti Manis, Biskuit, dan Snack Ringan) agar dapat memaksimalkan
keuntungan dan sekaligus meningkatkan efisiensi waktu kerja mesin yang
terbatas.

Proses penjadwalan produksi yang tidak optimal dapat menyebabkan
terjadinya *bottleneck* pada mesin kritis, pemanfaatan sumber daya yang
tidak merata, dan pada akhirnya, kerugian akibat waktu henti (*idle
time*) atau biaya lembur yang tidak perlu. Oleh karena itu, diperlukan
suatu pendekatan sistematis dan kuantitatif untuk menyelesaikan masalah
ini.

## B. Rumusan Masalah

Bagaimana memodelkan masalah penjadwalan produksi di Pabrik Makanan Agro
Jaya ke dalam model Program Linier (*Linear Programming*)?

Berapa kuantitas produksi optimal untuk masing-masing jenis produk yang
harus diproduksi dalam satu periode waktu guna memaksimalkan total
keuntungan perusahaan, dengan mempertimbangkan kendala kapasitas mesin
dan batasan permintaan pasar?

Bagaimana dampak perubahan kapasitas mesin (*bottleneck*) terhadap
profitabilitas dan efisiensi waktu, serta skenario optimal apa yang
dapat direkomendasikan?

## C. Tujuan Proyek

Tujuan yang ingin dicapai melalui proyek analisis dan optimasi ini
adalah:

Memformulasikan model matematika Program Linier untuk masalah alokasi
sumber daya dan penjadwalan produksi di Pabrik Makanan \'Agro Jaya\'.

Menemukan solusi penjadwalan produksi optimal menggunakan metode
komputasi (Python/PuLP) serta membandingkan hasilnya.

Melakukan analisis sensitivitas dan eksplorasi untuk mengidentifikasi
*bottleneck* dan memberikan rekomendasi strategis guna meningkatkan
efisiensi pemanfaatan waktu dan kapasitas mesin.

## D. Manfaat dan Ruang Lingkup

Proyek ini memberikan manfaat utama berupa solusi optimal yang langsung
meningkatkan efisiensi operasional Agro Jaya.

1.  Keputusan Produksi Tepat: Menghasilkan jadwal produksi yang pasti
    (XA​,XB​,XC​) yang memaksimalkan total keuntungan (Zmax​) perusahaan.

2.  Identifikasi Investasi Kritis: Menggunakan analisis *Shadow Price*
    untuk secara ilmiah mengidentifikasi Mesin *Bottleneck* yang
    membatasi keuntungan, sehingga keputusan investasi peningkatan
    kapasitas menjadi tepat sasaran.

3.  Efisiensi Waktu: Memastikan alokasi waktu mesin yang optimal,
    mengurangi waktu terbuang (*idle time*), dan secara keseluruhan
    meningkatkan efisiensi pemanfaatan sumber daya.

Proyek ini fokus pada pemodelan dan analisis pada lingkup terbatas agar
hasilnya spesifik dan terukur.

1.  Fokus Terbatas: Analisis hanya mencakup tiga jenis produk dan tiga
    pusat kerja/mesin utama di tahap produksi.

2.  Model *Linear Programming*: Menggunakan metode Program Linier (PL)
    sebagai kerangka pemodelan utama.

3.  Asumsi Data Pasti: Semua data input (waktu, biaya, kapasitas)
    diasumsikan pasti (*deterministik*) dan tidak mempertimbangkan
    faktor ketidakpastian (misalnya, kerusakan mesin atau fluktuasi
    permintaan).

4.  Alat Solusi: Solusi dicapai dan diverifikasi dengan perbandingan
    hasil antara Excel Solver dan Python (PuLP/SciPy).

# DESKRIPSI STUDI KASUS

## 1.1 Deskripsi singkat perusahaan/kasus

Pabrik Makanan Agro Jaya adalah perusahaan manufaktur makanan skala
menengah yang berlokasi di Jawa Barat. Perusahaan ini beroperasi dalam
lingkungan pasar yang kompetitif dan berupaya keras menjaga efisiensi
biaya operasional, terutama dalam proses produksinya. \'Agro Jaya\'
menggunakan sistem produksi *job-shop* di mana produk harus melewati
serangkaian mesin utama.

Manajemen Agro Jaya menyadari bahwa penjadwalan produksi yang ada saat
ini seringkali menghasilkan pemanfaatan mesin yang tidak merata dan
munculnya *bottleneck* yang tidak teridentifikasi, yang pada akhirnya
mengurangi total keuntungan mingguan. Oleh karena itu, perusahaan
mencari solusi optimal untuk alokasi produksi guna memaksimalkan
keuntungan dalam batasan jam kerja mesin yang tersedia.

Agro Jaya fokus pada tiga jenis produk utama dengan tingkat keuntungan
dan kebutuhan pemrosesan yang berbeda:

1\. Produk A (Roti Manis Premium): Memiliki margin keuntungan tertinggi,
tetapi membutuhkan waktu pemanggangan yang relatif lama.

2\. Produk B (Biskuit Hemat): Memiliki margin keuntungan sedang, dan
prosesnya seimbang di semua mesin.

3\. Produk C (Snack Ringan Cepat Saji): Memiliki margin keuntungan
terendah, tetapi waktu pemrosesannya sangat cepat di Mesin Pencampuran
dan Pengemasan.

## 1.2 Tabel Mesin dan Kapasitas

  -------------------------------------------------------------------------
  Lokasi Sumber Fungsi Utama        Simbol        Kapasitas Maksimal
  Daya (Mesin)                      Kendala       (Jam/Minggu)Mesin
  ------------- ------------------- ------------- -------------------------
  Mesin M1      Pencampuran Adonan  Kendala 1     100 Jam

  Mesin M2      Pemanggangan        Kendala 2     120 Jam

  Mesin M3      Pengemasan Akhir    Kendala 3     90 Jam
  -------------------------------------------------------------------------

Tabel ini mendefinisikan sumber daya utama (mesin) dan batas atas
(kendala) ketersediaan waktu. Nilai dalam kolom Kapasitas Maksimal akan
digunakan di sisi kanan (RHS) setiap pertidaksamaan kendala dalam model
Program Linier.

## 1.3 Tabel Produk dan Batasan Produksi

  --------------------------------------------------------------------------
  Produk                Variabel          Keuntungan/Unit   Batasan Minimum
                        Keputusan                           Produksi
                                                            (Unit/Minggu)
  --------------------- ----------------- ----------------- ----------------
  Produk A (Roti Manis) XA                ​Rp 5.000          1.000 unit

  Produk B (Biskuit)    XB                ​Rp 7.000          500 unit

  Produk C (Snack       XC                ​Rp 4.000          800 unit
  Ringan)                                                   
  --------------------------------------------------------------------------

Kolom Keuntungan/Unit menjadi koefisien dalam Fungsi Tujuan (Maksimisasi
Z). Kolom Batasan Minimum Produksi akan menjadi kendala *lower bound*
(≥) yang menjamin perusahaan memenuhi komitmen dasar pasar.

## 1.4 Tabel Kebutuhan Waktu Produksi

  -----------------------------------------------------------------------
  Kebutuhan Waktu      Mesin M1 (100    Mesin M2 (120    Mesin M3 (90
  (Jam/Unit)           Jam)             Jam)             Jam)
  -------------------- ---------------- ---------------- ----------------
  Produk A             0.015            0.025            0.010

  Produk B             0.010            0.020            0.010

  Produk C             0.005            0.010            0.015
  -----------------------------------------------------------------------

Data ini adalah koefisien teknologi yang menunjukkan tingkat konsumsi
waktu mesin oleh setiap produk. Nilai-nilai ini akan dikalikan dengan
Variabel Keputusan (Xi​) dan disajikan di sisi kiri (LHS) dari setiap
pertidaksamaan kendala kapasitas mesin.

# FORMULASI MATEMATIS

Model ini diformulasikan untuk menentukan jumlah unit dari Produk A, B,
dan C yang harus diproduksi dalam seminggu untuk **memaksimalkan total
keuntungan** perusahaan (Z), dengan kendala kapasitas jam mesin yang
tersedia.

## 1.1 Variabel Keputusan

Variabel Keputusan adalah output yang ingin kita cari nilainya, yaitu
kuantitas produksi mingguan untuk setiap produk:

XA​: Jumlah unit Produk A (Roti Manis) yang diproduksi.

XB​: Jumlah unit Produk B (Biskuit) yang diproduksi.

XC​: Jumlah unit Produk C (Snack Ringan) yang diproduksi.

## 1.2 Fungsi Tujuan

Tujuan perusahaan adalah Maksimisasi Keuntungan Total (Z). Koefisien
fungsi tujuan diambil dari kolom Keuntungan/Unit pada data studi kasus
(Tabel Produk dan Batasan Produksi).

Maksimalisasi Keuntungan (Z):

maxZ=5000XA​+7000XB​+4000XC​

## 1.3 Kendala

Kendala dibagi menjadi dua kategori utama: Kendala Kapasitas Mesin
(sumber daya terbatas) dan Kendala Permintaan Minimum (kewajiban pasar)

Kendala Kapasitas Mesin:

Kendala ini memastikan bahwa total waktu yang digunakan oleh semua
produk tidak melebihi kapasitas maksimal jam kerja mesin mingguan.
Koefisien diambil dari Tabel Kebutuhan Waktu Produksi.

\- Kendala Mesin M1 (Pencampuran):

0.015XA​+0.010XB​+0.005XC​≤100

\- Kendala Mesin M2 (Pemanggangan):

0.025XA​+0.020XB​+0.010XC​≤120

\- Kendala Mesin M3 (Pengemasan):

0.010XA​+0.010XB​+0.015XC​≤90

Kendala Permintaan Minimum

Kendala ini memastikan bahwa perusahaan memproduksi setidaknya jumlah
minimum yang telah ditetapkan untuk memenuhi permintaan dasar pasar.

-   Kendala Produk A:

> XA​≥1000

-   Kendala Produk B:

> XB​≥500

-   Kendala Produk C:

> XC​≥800

## 1.4 Kendala Non-Negatif

Kuantitas produk yang diproduksi tidak boleh negatif.

XA​,XB​,XC​≥0

## 1.5 Ringkasan Model Program Linier

  -----------------------------------------------------------------------
  **Komponen**                **Notasi Matematika**
  --------------------------- -------------------------------------------
  Variabel Keputusan          XA​,XB​,XC​

  Fungsi Tujuan               maxZ=5000XA​+7000XB​+4000XC​

  Kendala Kapasitas           0.015XA​+0.010XB​+0.005XC​≤100

                              0.025XA​+0.020XB​+0.010XC​≤120

                              0.010XA​+0.010XB​+0.015XC​≤90

  Kendala Permintaan          XA​≥1000

                              XB​≥500

                              XC​≥800

  Kendala Non-Negatif         XA​,XB​,XC​≥0
  -----------------------------------------------------------------------
