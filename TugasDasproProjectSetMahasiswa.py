# Program   : TugasDasproProjectSetMahasiswa.py
# Deskripsi : Program yang berisi tentang implementasi dan penggunaan dari set of Mahasiswa
# Kelompok  : 
# Dhimas Reza Nafi Wahyudi (24060124120010)
# Fadhil Yaafi Widodo (24060124140169)
# Elza Khoirisma Carrynda(24060124130065)
# Gabriel Serafim Hartajaya (24060124140159)
# Dewangga Maulana Saputro (24060124120032)
# Tanggal   : 10/11/2024

# Bagian 1
# Nomor 1 (Realisasi Selektor)
def getNIM(L): # Selektor untuk mengambil NIM dari mahasiswa
    return L[0]

def getNama(L):
    return L[1]

def getKelas(L):
    return L[2]

def getNilai(L):
    return L[3]

# Nomor 2
def IsEmpty(L):
    return L == []

def Konso(e, L):
    return [e] + L

def Tail(L):
    if IsEmpty(L):
        return None
    else: 
        return L[1:]

def FirstElmt(L):
    if IsEmpty(L):
        return None
    else: 
        return L[0]

def SumElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return FirstElmt(L) + SumElmt(Tail(L))
    
def NbElmt(L):
    if IsEmpty(L):
        return 0 
    else: 
        return 1 + NbElmt(Tail(L))

def AvgElmt(L):
    if NbElmt(L) == 0:
        return 0
    else:
        return int(SumElmt(L) / NbElmt(L))

def MaxElmt(L):
    if IsEmpty(L):  # Basis: Jika list mahasiswa kosong, kembalikan nilai 0
        return 0
    elif getNilai(getFirstMhs(L)) == []:  # Jika mahasiswa pertama tidak punya nilai, lanjut ke Tail
        return MaxElmt(Tail(L))
    elif MaxElmt(Tail(L)) > AvgElmt(getNilai(getFirstMhs(L))):  # Bandingkan dengan nilai dari Tail
        return MaxElmt(Tail(L))
    else:  # Jika nilai mahasiswa pertama lebih besar atau sama, kembalikan nilai tersebut
        return AvgElmt(getNilai(getFirstMhs(L)))

def makemhssesuaikelas(L, kelas): # Fungsi untuk mengelompokkan mahasiswa berdasarkan kelas tertentu
    if IsEmpty(L):
        return []  # Basis: jika list kosong, kembalikan list kosong
    if getKelas(getFirstMhs(L)) == kelas:
        return [getFirstMhs(L)] + makemhssesuaikelas(Tail(L), kelas) # Jika kelas mahasiswa pertama sesuai dengan kelas yang dicari
    else:
        return makemhssesuaikelas(Tail(L), kelas) # Jika kelas mahasiswa pertama tidak sesuai, lanjutkan ke mahasiswa berikutnya

    
# Bagian 2
# Nomor 1
# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
def MakeMhs(nim, nama, kelas, nilai): # Untuk membuat tipe bentukan mahasiswa
    return [nim, nama, kelas, nilai]

def makeNilai(nilai): # Untuk membuat set Nilai
    return nilai

# DEFINISI DAN SPESIFIKASI SELEKTOR
def getFirstMhs(set): # Selektor untuk mengambil list mahasiswa pertama dari set mahasiswa
    return set[0]

def getLastMhs(set): # Selektor untuk mengambil lst mahasiswa terakhir dari set mahasiswa
    return set[-1]


# Nomor 2
# A (SET OF MAHASISWA DENGAN SYARAT)
def MakeSpecialSetMhs(B, L): # Membuat set Mahasiswa dimana terdiri dari gabungan mahasiswa dengan NIM yang unik
    if IsEmpty(L):
        return Konso(B, L)
    elif getNIM(B) == getNIM(getFirstMhs(L)):
        return "Duplicate NIM " + "returning " + str(L)
    else:
        return Konso(MakeSpecialSetMhs(B, Tail(L)),getFirstMhs(L))
# Aplikasi
print(
    MakeSpecialSetMhs(
        MakeMhs(24060124120011, "Rawr", "F", makeNilai([90, 100, 80])),
        [
            MakeMhs(24060124120014, "Mooo", "F", makeNilai([90, 100, 80])),
            MakeMhs(24060124120015, "Quack", "F", makeNilai([90, 100, 80])),
        ],
    )
)
# B (MAHASISWA YANG LULUS)
def MhsLulus(H):
    if IsEmpty(H):
        return []
    else:
        if AvgElmt(getNilai(FirstElmt(H))) >= 70:
            return Konso(FirstElmt(H),MhsLulus(Tail(H)))
        else:
            return MhsLulus(Tail(H))
# Aplikasi
print(
    MhsLulus(
        [
            MakeMhs("001", "Jack", "C", [60, 50, 70, 85, 72]),
            MakeMhs("011", "Kala", "C", [90]),
            MakeMhs("003", "Huna", "B", [80, 90]),
            MakeMhs("004", "Ma", "C", [90]),
            MakeMhs("001", "Tata", "A", []),
            MakeMhs("005", "Sang", "B", [80, 92]),
            MakeMhs("003", "Peselancar", "A", []),
            MakeMhs("007", "Handal", "C", []),
        ]
    )
)

# C (MAHASISWA YANG TIDAK MENGERJAKAN KUIS)
def TdkMngrjknKuis(L):
    if IsEmpty(L):  # Jika list mahasiswa kosong, kembalikan list kosong
        return []
    elif getNilai(getFirstMhs(L)) == []:  # Jika mahasiswa pertama tidak mengerjakan kuis (nilai == [])
        # Tambahkan seluruh data mahasiswa yang tidak mengerjakan kuis ke hasil
        return MakeSpecialSetMhs(getFirstMhs(L), TdkMngrjknKuis(Tail(L)))  # Tambahkan mahasiswa ke hasil dan lanjutkan
    else:
        return TdkMngrjknKuis(Tail(L))  # Jika mahasiswa mengerjakan kuis, lanjutkan ke elemen berikutnya tanpa menambahkannya ke hasil
# Aplikasi
print("Mahasiswa yang tidak mengerjakan kuis:", TdkMngrjknKuis(([MakeMhs('24060124120032', 'Dewangga Maulana Saputro', 'B', makeNilai([])), MakeMhs('24060124120033', 'Dhimas Reza', 'B', makeNilai([90]))])))

# D (NILAI TERTINGGI (SEMUA KELAS))
# Fungsi untuk mendapatkan mahasiswa dengan nilai tertinggitanpa 
def NilaiTertinggi(L):
    if IsEmpty(L):
        return []  # Basis: jika list kosong, kembalikan list kosong
    else:
        if MaxElmt(L) == AvgElmt(getNilai(getFirstMhs(L))):
            return getFirstMhs(L)  # Kembalikan mahasiswa jika nilainya sama dengan nilai tertinggi
        else:
            return NilaiTertinggi(Tail(L))  # Lanjutkan ke mahasiswa berikutnya
# Aplikasi
print(NilaiTertinggi([MakeMhs('24060124120032', 'Dewangga Maulana Saputro', 'B', makeNilai([87, 100])), MakeMhs('24060124120033', 'Dhimas Rheza', 'B', makeNilai([90]))]))


# E (NILAI TERTINGGI (KELAS TERTENTU))
def Nilaitertinggisesuaikelas(L, kelas):
    if IsEmpty(L):
        return []  # Basis: jika list kosong, kembalikan list kosong
    elif getKelas(getFirstMhs(L)) == kelas:
        mahasiswakelastsb = makemhssesuaikelas(L, kelas) #kelompokkan mahasiswa sesuai kelas
        return NilaiTertinggi(mahasiswakelastsb) #Ambil mahasiswa dengan nilai tertinggi
    else:
        return Nilaitertinggisesuaikelas(Tail(L), kelas) # Jika kelas tidak sesuai, lanjutkan dengan mahasiswa berikutnya

# Aplikasi
print(Nilaitertinggisesuaikelas([
    MakeMhs('24060124120032', 'Dewangga Maulana Saputro', 'B', makeNilai([85])), 
    MakeMhs('24060124120033', 'Dhimas Reza', 'B', makeNilai([90])),
    MakeMhs('24060124120034', 'Andi', 'A', makeNilai([95]))
], 'B'))

# F (JUMLAH MAHASISWA TIDAK KUIS (SEMUA KELAS))
def JumlahMahasiswaTidakKuis(L):
    if IsEmpty(L):
        return 0 # Basis : jika list kosong kembalikan 0
    elif getNilai(getFirstMhs(L)) == [] : #Mengecek apakah mahasiswa pertama sudah mengerjakan kuis
        return 1 + JumlahMahasiswaTidakKuis(Tail(L)) 
    else :
        return JumlahMahasiswaTidakKuis(Tail(L)) #Jika mahasiswa pertama sudah mengerjakan kuis, lanjutkan dengan mahasiswa berikutnya

# Aplikasi
print(JumlahMahasiswaTidakKuis([
    MakeMhs('24060124120032', 'Dewangga Maulana Saputro', 'B', makeNilai([])),
    MakeMhs('24060124120033', 'Dhimas Reza', 'B', makeNilai([90])),
    MakeMhs('24060124120034', 'Andi', 'A', makeNilai([])),
    MakeMhs('24060124120035', 'Budi', 'C', makeNilai([])),
    MakeMhs('24060124120036', 'Cici', 'D', makeNilai([])),
    MakeMhs('24060124120037', 'Dina', 'E', makeNilai([]))
]))


# G (JUMLAH MAHASISWA LULUS (SEMUA KELAS))
def BanyakLulus(H):
    if IsEmpty(H):
        return 0
    else:
        if AvgElmt(getNilai(FirstElmt(H))) >= 70:
            return 1 + BanyakLulus(Tail(H))
        else:
            return BanyakLulus(Tail(H))
# Aplikasi
print(
    BanyakLulus(
        [
            MakeMhs("001", "Jack", "C", [60, 50, 70, 85, 72]),
            MakeMhs("011", "Kala", "C", [90]),
            MakeMhs("003", "Huna", "B", [80, 90]),
            MakeMhs("004", "Ma", "C", [90]),
            MakeMhs("001", "Tata", "A", []),
            MakeMhs("005", "Sang", "B", [80, 92]),
            MakeMhs("003", "Peselancar", "A", []),
            MakeMhs("007", "Handal", "C", []),
        ]
    )
)

