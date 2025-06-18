Data_Pasien = [
    {'Nomor Kode Pasien' : 'KP001', 'Nama Lengkap' : 'Adelia Yuni', 'Jenis Kelamin':'P', 'Tanggal Lahir' : {'Tanggal' : 3, 'Bulan' : 1, 'Tahun' : 1997}, 'Tanggungan' : 'Tanpa BPJS', 'Perawatan' : 'Rawat Inap', 'Proses' : 'Sedang Berjalan' },
    {'Nomor Kode Pasien' : 'KP002', 'Nama Lengkap' : 'Bambang Suhenda', 'Jenis Kelamin':'L', 'Tanggal Lahir' : {'Tanggal' : 6, 'Bulan' : 2, 'Tahun' : 1962}, 'Tanggungan' : 'BPJS', 'Perawatan' : 'Rawat Inap', 'Proses' : 'Sedang Berjalan' },
    {'Nomor Kode Pasien' : 'KP004', 'Nama Lengkap' : 'Cintya Nursela', 'Jenis Kelamin':'P', 'Tanggal Lahir' : {'Tanggal' : 9, 'Bulan' : 3, 'Tahun' : 2012}, 'Tanggungan' : 'BPJS', 'Perawatan' : 'Rawat Jalan', 'Proses' : 'Selesai' },
    {'Nomor Kode Pasien' : 'KP005', 'Nama Lengkap' : 'Dinda Putri', 'Jenis Kelamin':'P', 'Tanggal Lahir' : {'Tanggal' : 12, 'Bulan' : 4, 'Tahun' : 2022}, 'Tanggungan' : 'Tanpa BPJS', 'Perawatan' : 'Rawat Jalan', 'Proses' : 'Selesai' },
    {'Nomor Kode Pasien' : 'KP007', 'Nama Lengkap' : 'Erlan Suteja', 'Jenis Kelamin':'L', 'Tanggal Lahir' : {'Tanggal' : 15, 'Bulan' : 5, 'Tahun' : 1978}, 'Tanggungan' : 'Tanpa BPJS', 'Perawatan' : 'Rawat Inap', 'Proses' : 'Sedang Berjalan' },
    {'Nomor Kode Pasien' : 'KP008', 'Nama Lengkap' : 'Farhan Ibnu', 'Jenis Kelamin':'L', 'Tanggal Lahir' : {'Tanggal' : 18, 'Bulan' : 6, 'Tahun' : 2005}, 'Tanggungan' : 'BPJS', 'Perawatan' : 'Rawat Inap', 'Proses' : 'Sedang Berjalan' },
    {'Nomor Kode Pasien' : 'KP009', 'Nama Lengkap' : 'Gisela Abel', 'Jenis Kelamin':'P', 'Tanggal Lahir' : {'Tanggal' : 21, 'Bulan' : 7, 'Tahun' : 1992}, 'Tanggungan' : 'BPJS', 'Perawatan' : 'Rawat Jalan', 'Proses' : 'Selesai' },
    {'Nomor Kode Pasien' : 'KP010', 'Nama Lengkap' : 'Hendri Sutarjo', 'Jenis Kelamin':'L', 'Tanggal Lahir' : {'Tanggal' : 24, 'Bulan' : 8, 'Tahun' : 1990}, 'Tanggungan' : 'Tanpa BPJS', 'Perawatan' : 'Rawat Jalan', 'Proses' : 'Selesai' },
    {'Nomor Kode Pasien' : 'KP012', 'Nama Lengkap' : 'Intan Tasya', 'Jenis Kelamin':'P', 'Tanggal Lahir' : {'Tanggal' : 27, 'Bulan' : 9, 'Tahun' : 2017}, 'Tanggungan' : 'Tanpa BPJS', 'Perawatan' : 'Rawat Inap', 'Proses' : 'Sedang Berjalan' },
    {'Nomor Kode Pasien' : 'KP013', 'Nama Lengkap' : 'Jarwo Ilsa', 'Jenis Kelamin':'L', 'Tanggal Lahir' : {'Tanggal' : 30, 'Bulan' : 10, 'Tahun' : 2001}, 'Tanggungan' : 'BPJS', 'Perawatan' : 'Rawat Inap', 'Proses' : 'Selesai' }
]
# Data Pasien merupakan bagian dari dictionary dalam list. Karena sebagai dictionary dapat disimpan bersana key dan values

#==================================================================================================================================
# Menu Utama                                                                                        # Menampilkan menu utama pada aplikasi CRUD
def menuUtama():
    print('''
    ==================== SELAMAT DATANG DI RUMAH SAKIT NIAGARA ====================
__________________________________________________
          
Menu 1 : Menampilkan Data Pasien Rumah Sakit
Menu 2 : Menambahkan Data Pasien Rumah Sakit
Menu 3 : Mengubah Data Pasien Rumah Sakit
Menu 4 : Menghapus Data Pasien Rumah Sakit
Menu 5 : Keluar Dari Program
__________________________________________________
    ''')
# Apa Saja yang harus dilakukan
#==================================================================================================================================
#1. Membuat Tabel Pasien
def tabelPasien(i):
    KolomTabel = ['Nomor Kode Pasien', 'Nama Lengkap','Jenis Kelamin', 'Tanggal Lahir', 'Tanggungan', 'Perawatan', 'Proses' ]
    print('{:13}|{:17}|{:13}|{:17}|{:17}|{:17}|{:17}|'.format(*KolomTabel))                    #Mengubah Ukuran Pembatas Judul Tabel
    for pasien in i:
        baris = [
            pasien['Nomor Kode Pasien'],
            pasien['Nama Lengkap'],
            pasien['Jenis Kelamin'],
            str(penulisanTanggalLahir(pasien['Tanggal Lahir'])),
            pasien['Tanggungan'],
            pasien['Perawatan'],
            pasien['Proses']
        ]
        print('{:<17}|{:<17}|{:<13}|{:<17}|{:<17}|{:<17}|{:<17}|'.format(*baris))            # Mengubah Ukuran Pembatas Baris Tabel
    print()
#2. Format tanggal lahir diubah menjadi mm-dd-yyyy
def penulisanTanggalLahir(tanggalLahir):
    return f"{tanggalLahir['Tanggal']:02d}-{tanggalLahir['Bulan']:02d}-{tanggalLahir['Tahun']:04d}"
#==================================================================================================================================
# Konfirmasi Periksa Perubahan                                                                 # Yes/No untuk menghapus data
def MenyimpanPerubahan():
    while True: 
        konfirmasi = input('Yakin Mau Menghapus Data? (Y/N): ')
        if konfirmasi.upper() == 'Y':
            return True
        elif konfirmasi.upper() == 'N':
            return False
        else:
            continue        
def mengubah():                                                                                 # Yes/No untuk mengubah daata
    while True: 
        konfirmasi = input('Yakin Mau Mengubah Data? (Y/N): ')
        if konfirmasi.upper() == 'Y':
            return True
        elif konfirmasi.upper() == 'N':
            return False
        else:
            continue        

# Periksa duplikat unique key                                                                     # Mengecek agar Kode Pasien Tidak double/sama
def nkp(nomorKP):
    global Data_Pasien
    for pasien in Data_Pasien:
        if pasien['Nomor Kode Pasien'] == nomorKP.upper():
            return True
    else:
        return False
    
# Cari pasien berdasarkan nomor unik                                                              # Mencari Pasien Berdasarkan Kode Pasien
def pasien(nomorKP):
    for pasien in Data_Pasien:
        if pasien['Nomor Kode Pasien'] == nomorKP.upper():
            return pasien
        
#==================================================================================================================================
# Menu 1                                                                                           # Menampilkan List Menu 1
def menu1():
    print(
        ''' ================= Lihat Daftar Pasien Rumah Sakit Niagara =================''')
    print('''
    ________________________________________
          
    1. Tampilkan Seluruh Data
    2. Tampilkan Data Pasien Tertentu
    3. Kembali ke Menu Utama
    _________________________________________
     ''')

#==================================================================================================================================
# Menu 2                                                                                        
def menu2():
    print('''\n================= Menambahkan Data Pasien Baru =================\n''')       # Menampilkan List Menu 2   
    print('''\n1. Tambahkan Data Pasien Baru\n2. Kembali ke Menu Utama\n''')

# 2.1 Menu tambah pasien                                                                    # Menyimpan data pasien yang ditambah nantinya
def tambahPasien():
    global Data_Pasien
    global dataBaru 
    if inputNoBaru(dataBaru) == True:
        kelengkapanData_PasienBaru()
        if MenyimpanPerubahan() == True:
            Data_Pasien.append(dataBaru)
            print('Data Tersimpan ✅')   
    return dataBaru, Data_Pasien

# 2.2 Menu input data pasien baru                                                  # Menginput data pasien baru berupa nama,jk,tl,tanggungan,perawatan,dan prosen
def kelengkapanData_PasienBaru():                                                  # lalu nanti dimasukan ke dalam tabel sebagai input data pasien baru
    global Data_Pasien
    global dataBaru
    inputNama(dataBaru)
    inputJk(dataBaru)
    tglLahir()
    inputTanggungan(dataBaru)
    inputPerawatan(dataBaru)
    inputProses(dataBaru)
    tabelPasien([dataBaru])
    return dataBaru
#==================================================================================================================================
# Fungsi-fungsi untuk Input Data Pasien
def inputNoBaru(dataBaru):
    while True:
        nomorKP = input('Masukkan Nomor Kode Pasien Pasien: ')              # Input Nomor Kode Pasien
        if nkp(nomorKP) == True:                                            # Memeriksa data duplikat jika terdaftar maka false dan gagal menyimpan
            tabelPasien([pasien(nomorKP)])
            print('\n===== Pasien sudah terdaftar ❌ =====')
            return False
        if len(nomorKP) < 4 or not nomorKP.isalnum():                       # Periksa format unique key
            print('===== Nomor Kode Pasien Harus terdiri dari Huruf dan angka minimal 4 karakter ❌=====')
            break
        else:
            dataBaru['Nomor Kode Pasien'] = nomorKP.upper()                 # input Nomor Kode Pasien
            return True                                                     # Jika benar maka dianggap true dan data disimpan

def inputNama(dataBaru):                                                # Input Nama pasien lebih dari 3 huruf
    while True:
        namaLengkap = input('Masukkan Nama Lengkap Pasien: ')
        if namaLengkap.isalpha and len(namaLengkap) > 3:                    
            dataBaru['Nama Lengkap'] = namaLengkap.title()
            break
        else:
            print('===== Input Nama Lengkap dengan Benar ❌ =====')             # Jika sudah benar keluar output seperti ini

def inputJk(dataBaru):                                                  # Input jenis kelamin ada 2 opsi P/L
    while True:
        jenisKelamin = input('Masukkan Jenis Kelamin Pasien (P/L): ')       
        if jenisKelamin.upper() == 'P' or jenisKelamin.upper() == 'L':      
            dataBaru['Jenis Kelamin'] = jenisKelamin.upper()
            break
        else:
            print('\n===== Masukkan jenis kelamin dengan benar ❌ =====')  #jika salah input maka akan keluar output seperti ini

def inputTanggungan(dataBaru):                                         # Input Tanggungan ada 2 opsi BPJS dan Tanpa BPJS
    while True:
        Tanggungan = input(f'''{'-'*50}\nTanggungan\n1. Tanpa BPJS\t 2. BPJS \t\nMasukkan Jenis Tanggungan Pasien [1-2]: ''')                   
        if Tanggungan == '1':
            Tanggungan = 'Tanpa BPJS'
            break
        elif Tanggungan == '2':
            Tanggungan = 'BPJS'
            break
        else:
            print('===== Masukkan salah satu dari pilihan ❌ =====')               # Pilih salah satu dari 2 opsi tersebut   
    dataBaru['Tanggungan'] = Tanggungan
    
def inputPerawatan(dataBaru):                                         # Input Perawatan ada 2 opsi Rawat Inap dan Berjalan
    while True:
        perawatan = input(f'''{'-'*50}\nPerawatan\n1. Rawat Inap\t 2. Rawat Jalan\nMasukkan Jenis Perawatan Pasien [1-2]: ''')
        if perawatan == '1':
            perawatan = 'Rawat Inap'
            break
        elif perawatan == '2':
            perawatan = 'Rawat Jalan'
            break
        else:
            print('===== Masukkan salah satu dari pilihan ❌ =====')           # Pilih salah satu dari 2 opsi tersebut         
    dataBaru['Perawatan'] = perawatan
    
def inputProses(dataBaru):                           # Input Proses Pengobatan dari 2 opsi tersebut
    while True:
        proses = input(f'''{'-'*50}\nProses Pengobatan\n1. Sedang Berjalan\t 2. Selesai\nProses Pengobatan Pasien [1-2]: ''')
        if proses == '1':
            proses = 'Sedang Berjalan'
            break
        elif proses == '2':
            proses = 'Selesai'
            break
        else:
            print('===== Masukkan salah satu dari pilihan ❌ =====')           #  Pilih salah satu dari 2 opsi tersebut      
    dataBaru['Proses'] = proses
    

#2.2.1 Khusus tanggal lahir
def tglLahir():
    print('\nMasukkan Tanggal, Bulan, dan Tahun Lahir Pasien')
    global dataBaru
    dataBaru['Tanggal Lahir']={'Tanggal':'','Bulan':'','Tahun':''}              # Input tanggal lahir 
    inputTglLahir(dataBaru)

def inputTglLahir(dataBaru):
    while True:
        try:
            tanggalLahir = int(input('1. Tanggal (maksimal 2 digit angka): '))      # Input Tanggal Lahir (hari)
            if tanggalLahir <= 31 and tanggalLahir > 0:                             # Dari > 0 sampai <= 31 (hari)
                dataBaru['Tanggal Lahir']['Tanggal'] = tanggalLahir
                break
            else:
                print('''\n===== Masukkan tanggal dengan benar ❌ =====\n''')           # Output jika sudah benar

        except ValueError:                                                      # Jika lebih dari 2 digit angka maka akan error
            print('''\n===== Masukkan Maksimal 2 digit angka ❌ =====\n''')

    while True:   
        try:
            bulanLahir = int(input('2. Bulan (maksimal 2 digit angka): '))          # Input Tanggal Lahir (bulan)
            if bulanLahir <= 12 and bulanLahir > 0:                                 # Dari >0 sampai <= 12 (bulan)
                dataBaru['Tanggal Lahir']['Bulan'] = bulanLahir
                break
            else:
                print(''''\n===== Masukkan bulan dengan benar ❌ =====\n''')            # Output jika sudah benar
        except ValueError:
            print('''\n===== Masukkan Maksimal 2 digit angka ❌ =====\n''')              # Jika lebih dari 2 digit angka maka akan error

    while True:           
        try:
            tahunLahir = int(input('3. Tahun (masukkan 4 digit angka): '))          # Input Tanggal Lahir (tahun)
            if tahunLahir <= 2025 and tahunLahir > 1925:                            # Tahun kelahiran dari 1925 - 2025
                dataBaru['Tanggal Lahir']['Tahun'] = tahunLahir
                break
            else:
                print('''\n===== Masukkan tahun dengan benar ❌ =====\n''')             # Output jika sudah benar
        except ValueError:
            print('''\n===== Masukkan Maksimal 4 digit angka ❌ =====\n''')             # Jika lebih dari 4 digit angka makan akan error 

    return dataBaru, tanggalLahir, bulanLahir, tanggalLahir
#==================================================================================================================================

# Menu 3
def menu3():
    print(
        '''\n==================== Mengubah Data Pasien ====================\n''')       # Menampilkan list menu 3
    print('''\n1. Ubah Data Pasien \n2. Kembali ke Menu Utama\n''')

# 3.1 Fungsi Ubah Data Pasien
dataUpdate={}                                                                    # Mengupadte Pasien berdasarkan Nomor Kode Pasien
def ubahData_Pasien(nomorKP):
    global Data_Pasien
    if nkp(nomorKP) == True:
        tabelPasien([pasien(nomorKP)])                                            # memunculkan tabel pasien sesuai input primary key
        if mengubah() == True:
            kolomUpdate(pasien(nomorKP)) 
    else:
        print('===== Data Tidak Ada ❌ =====')                                          # Output jika pasien tidak terdaftar di data pasien
    return pasien
# 3.1.2 Pilih Kolom Update 
def kolomUpdate(pasien):
    kolom = (input(f'''{'-'*50}\nInput Kolom yang di-Update: ''')).title()
    keyDitemukan = False
    for key, values in pasien.items():
        if key == kolom:
            keyDitemukan = True
            if key == 'Nama Lengkap':
                namaUpdate(pasien)
            elif key == 'Nomor Kode Pasien':
                nkpUpdate(pasien)
            elif key == 'Jenis Kelamin':
                jkUpdate(pasien)
            elif key == 'Tanggal Lahir':
                tlUpdate(pasien)
            elif key == 'Tanggungan':
                TanggunganUpdate(pasien)
            elif key == 'Perawatan':
                perawatanUpdate(pasien)
            elif key == 'Proses':
                prosesUpdate(pasien)
    if not keyDitemukan:
        print('Kolom Tidak Ada')
    return Data_Pasien

#  Fungsi-fungsi untuk update data pasien sesuai kolom terpilih    
def nkpUpdate(pasien):
    print('\n----- Update Nomor Kode Pasien Pasien -----\n')
    while inputNoBaru(dataUpdate) != True:                                  # Menambahkan fungsi dari menu 2 (input)
        continue
    if MenyimpanPerubahan() == True:
        pasien['Nomor Kode Pasien'] = dataUpdate['Nomor Kode Pasien']
        print('\n===== Data Telah Di-Update ✅ =====\n')                                    # Notif sudah diupdate
    return Data_Pasien

def namaUpdate(pasien):                                                     # Mengubah nama lengkap pasien untuk nantinya diupdate lalu disimpan
    print('\n----- Update Nama Pasien -----\n')
    inputNama(dataUpdate)
    if MenyimpanPerubahan() == True:
        pasien['Nama Lengkap'] = dataUpdate['Nama Lengkap']
        print('\n===== Data Telah Di-Update ✅ =====\n')                                   # Notif sudah di update
    return Data_Pasien

def jkUpdate(pasien):                                                       # Mengubah jenis kelamin untuk nantinya diupdate lalu disimpan
    print('\n----- Update Jenis Kelamin Pasien -----\n')
    inputJk(dataUpdate)
    if MenyimpanPerubahan() == True:
        pasien['Jenis Kelamin'] = dataUpdate['Jenis Kelamin']
        print('\n===== Data Telah Di-Update ✅ =====\n')                                   # Notif sudah diupdate
    return Data_Pasien

def tlUpdate(pasien):                                                       # Mengubah Tanggal Lahir untuk nantinya diupdate lalu disimpan
    print('\n----- Update Tanggal Lahir Pasien -----\n')                    # Berupa Tanggal, Bulan, dan tahun
    dataUpdate['Tanggal Lahir']={'Tanggal':'','Bulan':'','Tahun':''}
    inputTglLahir(dataUpdate)
    if MenyimpanPerubahan() == True:
        pasien['Tanggal Lahir']['Tanggal'] = dataUpdate['Tanggal Lahir']['Tanggal']
        pasien['Tanggal Lahir']['Bulan'] =  dataUpdate['Tanggal Lahir']['Bulan']
        pasien['Tanggal Lahir']['Tahun'] =  dataUpdate['Tanggal Lahir']['Tahun']
        print('===== Data Telah Di-Update ✅ =====')                                                   # Notif sudah di update
    return Data_Pasien

def TanggunganUpdate(pasien):                                                  # Mengubah Tanggungan untuk nantinya di update lalu disimpan
    print('\n----- Update Tanggungan Pasien -----\n')
    inputTanggungan(dataUpdate)
    if MenyimpanPerubahan() == True:
        pasien['Tanggungan'] = dataUpdate['Tanggungan']
        print('\n===== Data Telah Di-Update ✅ =====\n')                                      # Notif sudah di update
    return Data_Pasien

def perawatanUpdate(pasien):                                                    # Mengubah Perawatan untuk nantinya di update lalu disimpan
    print('\n----- Update Jenis Perawatan Pasien -----\n')
    inputPerawatan(dataUpdate)
    if MenyimpanPerubahan() == True:
        pasien['Perawatan'] = dataUpdate['Perawatan']
        print('\n===== Data Telah Di-Update ✅ =====\n')                                       # Notif sudah di update
    return Data_Pasien

def prosesUpdate(pasien):                                                       # Mengubah proses pengobatan untuk nantinya di update lalu disimpan
    print('\n----- Update Proses Pengobatan Pasien -----\n')
    inputProses(dataUpdate)
    if MenyimpanPerubahan() == True:
        pasien['Proses'] = dataUpdate['Proses']
        print('===== Data Telah Di-Update ✅ =====')                                           # Notif sudah di update
    return Data_Pasien
    
#==================================================================================================================================
# Menu 4
Data_PasienDihapus = []                                                                 
pasienSelesai = []
def menu4():
    print(
        ''' ==================== Menghapus Data Pasien ====================\n''')       # Menampilkan list menu 4
    print('''
    1. Hapus Data Pasien Tertentu
    2. Hapus Pasien yang Selesai Berobat
    3. History Data Pasien Yang Di Hapus
    4. Kembali ke Menu Utama
    ''')

# 4.1 Fungsi Hapus Pasien Tertentu                                                      # Menghapus data pasien
Data_PasienDihapus = []
def hapusPasien(nomorKP):
    global Data_PasienDihapus
    global Data_Pasien
    if nkp(nomorKP) == True:                                                             # Menghapus berdasarkan Nomor KP
        tabelPasien([pasien(nomorKP)])
        if MenyimpanPerubahan() == True:                                                  # Lalu disimpan jika sudah benar 
            Data_PasienDihapus.append(pasien(nomorKP))                                    
            Data_Pasien.remove(pasien(nomorKP))
            print('===== Data Telah Dihapus ✅ =====')                                                   # Notif sudah di hapus
    else:
        print('Pasien Tidak Terdaftar')
    return Data_PasienDihapus, Data_Pasien

# 4.2 Hapus berdasarkan kategori
def hapusPasienKategori():                                                              # Menghapus berdasarkan kategori 
    global Data_PasienDihapus
    global pasienSelesai
    global Data_Pasien
    dataDitemukan = False
    for pasien in Data_Pasien:
        if pasien['Proses'] == 'Selesai':                                               # Jika proses pengobatan selesai maka bisa dihapus dari data 
            pasienSelesai.append(pasien)
            dataDitemukan = True
    if dataDitemukan == True:                       
        tabelPasien(pasienSelesai)
        if MenyimpanPerubahan() == True:                                                # Disimpan jika sudah benar
            for pasien in pasienSelesai:
                Data_PasienDihapus.append(pasien)                                       # Menambahkan pasien yang sudah dihapus 
                Data_Pasien.remove(pasien)
            print('===== Data Telah Dihapus ✅ =====')                                                 # Notif jika pasien sudah dihapus
        pasienSelesai.clear()
    if not dataDitemukan:
        print('Tidak Ada Pasien Selesai')     

#==================================================================================================================================
# Konsep besar
while True:
    menuUtama()
    pilihan_menu= input('Silahkan Pilih Menu [1-5]: ')

# MENU 1: MENAMPILKAN DATA (READ)
    if pilihan_menu == '1':
        while True:                  
            menu1()
            pilihan_menu1 = input('Silahkan Pilih Menu [1-3]: ') 
            if pilihan_menu1 == '1':
                if len(Data_Pasien) > 0: 
                    tabelPasien(Data_Pasien)               
                else:
                    print('*** Data Tidak Ada ***')
            elif pilihan_menu1 == '2':                               
                nomorKP = (input('Masukkan Nomor Kode Pasien: ')).capitalize()
                if nkp(nomorKP) == True:
                    tabelPasien([pasien(nomorKP)])
                elif nkp(nomorKP) == False:
                    print('*** Data Tidak Ada ***')
            elif pilihan_menu1 == '3':
                break
            else:
                print('===== Inputan salah. Masukkan sesuai opsi menu ❌ =====\n')
        
# MENU 2: MENAMBAHKAN DATA (CREATE)
    elif pilihan_menu == '2':
        while True:
            menu2()
            pilihan_menu2 = input('Silakan Pilih Menu [1-2]: ')
            if pilihan_menu2 == '1':
                dataBaru ={}
                tambahPasien()
            elif pilihan_menu2 == '2':
                break          
            else:
                print('===== Inputan salah. Masukkan sesuai opsi menu ❌ =====\n')

# MENU 3: UPDATE DATA (UPDATE)
    elif pilihan_menu == '3':
        while True:
            menu3()
            pilihan_menu3 = input('Silakan Pilih Menu [1-2]: ')
            if pilihan_menu3 == '1':
                nomorKP = (input('Masukkan Nomor Kode Pasien: ')).capitalize()
                ubahData_Pasien(nomorKP)
            elif pilihan_menu3 =='2':
                break
            else:
                print('===== Inputan salah. Masukkan sesuai opsi menu ❌ =====\n')
            
# MENU 4: HAPUS DATA (DELETE)
    elif pilihan_menu == '4':
        while True:
            menu4()
            pilihan_menu4 = input('Silakan Pilih Menu [1-4]: ')
            if pilihan_menu4 == '1':
                nomorKP = (input('Masukkan Nomor Kode Pasien: ')).capitalize()
                hapusPasien(nomorKP) 
            elif pilihan_menu4 == '2':
                print('Hapus Pasien Selesai Pengobatan')
                hapusPasienKategori() 
            elif pilihan_menu4 =='3':
                if len(Data_PasienDihapus) > 0:
                    tabelPasien(Data_PasienDihapus)
                else:
                    print('Data Tidak Ada ❌')                  
            elif pilihan_menu4 == '4':
                break
            else:
                print('===== Inputan salah. Masukkan sesuai opsi menu ❌ =====\n')
            
# MENU 5: KELUAR PROGRAM
    elif pilihan_menu == '5':
        keluarProgram = input('Apakah Anda yakin ingin keluar dari program? (Y/N): ')       # Konfirmasi exit program
        if keluarProgram.upper() == 'N':
            continue                                            # Lanjut ke menu Utama jika no
        elif keluarProgram.upper() == 'Y':
            print('\n===== Terima kasih, see you 👋😊 =====')
            break                                               # Keluar dari program jika yes
    else:
        print('===== Pilihan menu tidak tersedia ❌ =====')
        
