#Created by Fatika Rahma Sanjaya

from tabulate import tabulate
import pyinputplus as pyip

dataPasien = [
    {'id' : 'P001', 'nama_pasien': 'Clara','umur': 50, 'kelas_kamar': 'VIP','penjamin' : 'ASURANSI', 'nama_dokter' : 'Adhitama'},
    {'id' : 'P002', 'nama_pasien': 'Freya','umur': 22, 'kelas_kamar': 'I','penjamin' : 'UMUM', 'nama_dokter' : 'Karel'},
    {'id' : 'P003','nama_pasien': 'Oktavianus','umur': 33,'kelas_kamar': 'II', 'penjamin' : 'BPJS','nama_dokter' : 'Erica'},
    {'id' : 'P004','nama_pasien': 'Wisnutama','umur': 45,'kelas_kamar': 'VIP','penjamin' : 'ASURANSI', 'nama_dokter' : 'Karel'},
    {'id' : 'P005', 'nama_pasien': 'Alan Dirga','umur': 17, 'kelas_kamar': 'I','penjamin' : 'BPJS', 'nama_dokter' : 'Erica'}
]

# Fungsi untuk menampilkan menu utama
def menu():
    while True:
        print("="*44)
        print("    Aplikasi Data Pasien TrueCare Hospital    ")
        print("          Pasien Rawat Inap        ")
        print("="*44)
        print("\nMenu:")
        print("1. Tampilkan Daftar Pasien")
        print("2. Menambah Data Pasien Baru")
        print("3. Menghapus Data Pasien")
        print("4. Edit Data Pasien")
        print("5. Keluar")

        pilihan = pyip.inputNum(prompt="Masukkan pilihan (1/2/3/4/5): ", min=1, max=5)

        if pilihan == 1:
            tampil_data()
        elif pilihan == 2:
            tambah_data()
        elif pilihan == 3:
            hapus_data()
        elif pilihan == 4:
            edit_data()
        elif pilihan == 5:
            print("\nTerima kasih telah menggunakan aplikasi Data Pasien TrueCare Hospital")
            print("Sampai jumpa kembali!")
            quit()
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

# Fungsi untuk menampilkan data pasien
def tampil_data():
    while True:
        print('''
            Sub-menu Tampil Data Pasien Truecare Hospital
                1. Melihat Seluruh Data Pasien
                2. Melihat Data Pasien Berdasarkan ID
                3. Kembali ke Menu Utama
                ''')
        sub_pilihan = pyip.inputNum(prompt="\nPilih sub-menu (1-3): ",min=1, max=3)
        if sub_pilihan == 1:
            if not dataPasien:
                print("Tidak ada data pasien yang tersimpan.")
            else:
                tampil_semua_data()
        elif sub_pilihan == 2:
            while True:
                id_pasien = pyip.inputStr(prompt="Masukkan ID Pasien: ").upper()
                if not dataPasien:
                    print("Tidak ada data pasien yang tersimpan.")
                    break
                elif len(id_pasien) != 4 or id_pasien[0] != 'P' or not id_pasien[1:].isdigit() or id_pasien[1:] == '000':
                    print("ID Pasien harus dimulai dengan 'P' dan terdiri dari 3 angka (tidak boleh 'P000').")
                else:
                    data_pasien_berdasarkan_id(id_pasien)
                    break
        elif sub_pilihan == 3:
            break
        else:
            print("\nPilihan tidak valid. Silakan masukkan pilihan yang benar.")

#Fungsi untuk menampilkan data gabungan
def tampil_semua_data():
    if not dataPasien:
        print("\nTidak ada data pasien yang tersimpan.")
        return
    # Mengurutkan dataPasien berdasarkan ID pasien secara ascending (A-Z)
    sorted_data = sorted(dataPasien, key=lambda x: x['id'])
    table_headers = ["ID", "Nama Pasien", "Umur", "Kelas Kamar", "Penjamin", "Nama Dokter"]
    table_rows = [[data['id'], data['nama_pasien'], data['umur'], data['kelas_kamar'], data['penjamin'], data['nama_dokter']] for data in sorted_data]
    print(tabulate(table_rows, headers=table_headers, tablefmt="grid"))

# Fungsi untuk menampilkan data pasien berdasarkan ID
def data_pasien_berdasarkan_id(id_pasien):
    found_data = False
    for data in dataPasien:
        if data['id'] == id_pasien:
            found_data = True
            table_headers = ["ID", "Nama Pasien", "Umur", "Kelas Kamar", "Penjamin", "Nama Dokter"]
            table_data = [[data['id'], data['nama_pasien'], data['umur'], data['kelas_kamar'], data['penjamin'], data['nama_dokter']]]
            print(tabulate(table_data, headers=table_headers, tablefmt="grid"))
    if not found_data:
        print("Data pasien dengan ID tersebut tidak ditemukan.")

# Fungsi untuk menambahkan data pasien
def tambah_data():
    print('''
            Sub-menu Tambah Data Pasien Truecare Hospital
                1. Tambah Data Pasien Baru
                2. Kembali ke Menu Utama
                ''')
    a = pyip.inputNum(prompt="Masukan angka 1 atau 2: ", min=1, max=2)
    
    if a == 2:
        menu() 
    elif a == 1:
        while True:
            id_new = pyip.inputStr(prompt="Masukkan ID Pasien: ").upper()
            if len(id_new) != 4 or id_new[0] != 'P' or not id_new[1:].isdigit() or id_new[1:] == '000':
                print("ID Pasien harus dimulai dengan 'P' dan terdiri dari 3 angka (tidak boleh 'P000').")
            elif any(data['id'] == id_new for data in dataPasien):
                print("ID Pasien sudah ada. Masukkan ID lain.")
                tambah_data()
            else:
                break
        
        while True:
            nama_pasien = pyip.inputStr(prompt="Nama Pasien: ", blockRegexes=[r'[^A-Za-z\s]']).title()
            if not nama_pasien.strip():
                print("Nama Pasien tidak boleh kosong.")
            elif len(nama_pasien) > 25:
                print("Nama Pasien tidak boleh lebih dari 25 karakter.")
            elif any(char.isdigit() for char in nama_pasien):
                print("Nama Pasien tidak boleh mengandung angka.")
            else:
                break
        
        while True:
            umur = pyip.inputInt(prompt="Umur Pasien: ", min=0, max=100)
            break
        
        while True:
            kelas_kamar = pyip.inputChoice(['VIP', 'I', 'II', 'III'], prompt="Kelas Kamar (VIP/I/II/III): ", caseSensitive=False)
            break
            
        while True:
           penjamin = pyip.inputMenu(['ASURANSI', 'BPJS', 'UMUM'], numbered=True, prompt="Pilih 1/2/3:\n")
           break
        
        while True:
            nama_dokter = pyip.inputStr(prompt="Nama Dokter: ", blockRegexes=[r'[^A-Za-z\s]']).title()
            if not nama_dokter.strip():
                print("Nama Dokter tidak boleh kosong.")
            elif len(nama_dokter) > 25:
                print("Nama Dokter tidak boleh lebih dari 25 karakter.")
            elif any(char.isdigit() for char in nama_dokter):
                print("Nama Dokter tidak boleh mengandung angka.")
            else:
                break
        
        # Menampilkan tabel hasil input pengguna
        table_headers = ["ID", "Nama Pasien", "Umur", "Kelas Kamar", "Penjamin", "Nama Dokter"]
        table_data = [[id_new, nama_pasien, umur, kelas_kamar, penjamin, nama_dokter]]
        print(tabulate(table_data, headers=table_headers, tablefmt="grid"))

        # Tanyakan kepada pengguna apakah mereka ingin menyimpan data tersebut
        checker = input('Simpan data pasien baru? (Y/N)').upper()
        if checker == 'Y':
            # Simpan data ke dalam list dataPasien
            dataPasien.append({
                'id': id_new,
                'nama_pasien': nama_pasien,
                'umur': umur,
                'kelas_kamar': kelas_kamar,
                'penjamin': penjamin,
                'nama_dokter': nama_dokter
            })
            print("Data Pasien berhasil ditambahkan!")
            tambah_data()
        elif checker == 'N':
            print("Data Pasien tidak disimpan.")
            tambah_data()
        else:
            print("Pilihan tidak valid.")

#Fungsi Menghapus Data Pasien
dataPasienDihapus = []
def hapus_data():
    while True:
        print('''
          Sub-menu Hapus Data Pasien TrueCare Hospital
                1. Hapus data berdasarkan ID pasien
                2. Restore data pasien
                3. Kembali ke Menu Utama
                ''')
        b = pyip.inputNum(prompt="\nMasukkan angka (1-3): ", min=1, max=3)
        if b == 1:
            id_pasien = pyip.inputStr(prompt="Masukkan ID Pasien: ").upper()
            if len(id_pasien) != 4 or id_pasien[0] != 'P' or not id_pasien[1:].isdigit() or id_pasien[1:] == '000':
                print("ID Pasien harus dimulai dengan 'P' dan terdiri dari 3 angka (tidak boleh 'P000').")
                continue
            found = False
            for i, data in enumerate(dataPasien):
                if data['id'] == id_pasien:
                    found = True
                    table_headers = ["ID", "Nama Pasien", "Umur", "Kelas Kamar", "Penjamin", "Nama Dokter"]
                    table_data = [[data['id'], data['nama_pasien'], data['umur'], data['kelas_kamar'], data['penjamin'], data['nama_dokter']]]
                    print(tabulate(table_data, headers=table_headers, tablefmt="grid"))
                    checker = input('Apakah Anda yakin ingin menghapus data ini? (Y/N)').upper()
                    if checker == 'Y':
                        dataPasienDihapus.append(dataPasien.pop(i))
                        print(f"Data Pasien dengan ID {id_pasien} berhasil dihapus.")
                    elif checker == 'N':
                        print("Penghapusan data dibatalkan.")
                        break  # Keluar dari loop saat penghapusan data dibatalkan
                    else:
                        print("Masukan tidak valid. Silakan masukkan Y atau N.")
            if not found:
                print(f"ID Pasien {id_pasien} tidak ditemukan.")
        
        elif b == 2:
            restore_data()
        elif b == 3:
            menu()
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1, 2, atau 3.")

#sub delete : restore data
def restore_data():
    if not dataPasienDihapus:
        print("Tidak ada data pasien yang dihapus.")
        hapus_data()
    print("Data Pasien yang Dihapus:")
    sorted_datahapus = sorted(dataPasienDihapus, key=lambda x: x['id'])
    table_headers = ["ID", "Nama Pasien", "Umur", "Kelas Kamar", "Penjamin", "Nama Dokter"]
    table_rows = [[data['id'], data['nama_pasien'], data['umur'], data['kelas_kamar'], data['penjamin'], data['nama_dokter']] for data in sorted_datahapus]
    print(tabulate(table_rows, headers=table_headers, tablefmt="grid"))

    id_pasien_restore = input("Masukkan ID Pasien yang ingin dipulihkan: ").upper()
    for i, data in enumerate(dataPasienDihapus):
        if data['id'] == id_pasien_restore:
            print("Data Pasien yang Akan Dipulihkan:")
            print(tabulate([table_headers, table_rows[i]], tablefmt="grid"))

            checker = input('Apakah Anda yakin ingin memulihkan data ini? (Y/N)').upper()
            if checker == 'Y':
                # Pindahkan data yang dipulihkan kembali ke dataPasien
                dataPasien.append(dataPasienDihapus.pop(i))
                print(f"Data Pasien dengan ID {id_pasien_restore} berhasil dipulihkan.")
                hapus_data()
            elif checker == 'N':
                print("Pemulihan data dibatalkan.")
                hapus_data()
            else:
                print("Masukan tidak valid. Silakan masukkan Y atau N.")
            return
    print(f"ID Pasien {id_pasien_restore} tidak ditemukan di data yang dihapus.")
    return
    
# Fungsi untuk melakukan edit data
def edit_data():
    while True:
        print('''
              Sub Menu Edit Data Pasien Rawat Inap
              1. Edit data pasien rawat inap
              2. Kembali ke menu utama''')
        c = input("Masukan angka 1 atau 2: ")
        if c == '2':
            return
        elif c == '1':
            while True:
                idEdit = pyip.inputStr(prompt="Masukkan ID Pasien yang ingin diedit: ").upper()
                if len(idEdit) != 4 or idEdit[0] != 'P' or not idEdit[1:].isdigit() or idEdit[1:] == '000':
                    print("ID Pasien harus dimulai dengan 'P' dan terdiri dari 3 angka (tidak boleh 'P000').")
                    continue
                for data in dataPasien:
                    if data['id'] == idEdit:
                        print("Data ditemukan!")
                        print("Data Pasien:")
                        table_headers = ["ID", "Nama Pasien", "Umur", "Kelas Kamar", "Penjamin", "Nama Dokter"]
                        table_data = [[data['id'], data['nama_pasien'], data['umur'], data['kelas_kamar'], data['penjamin'], data['nama_dokter']]]
                        print(tabulate(table_data, headers=table_headers, tablefmt="grid"))
                        
                        # Konfirmasi apakah pengguna ingin mengedit data
                        confirm_edit = input("Apakah Anda ingin mengedit data ini? (Y/N): ").upper()
                        if confirm_edit == 'Y':
                            while True:
                                print("\nPilih kolom yang ingin diedit:")
                                print("1. Nama Pasien")
                                print("2. Umur")
                                print("3. Kelas Kamar")
                                print("4. Penjamin")
                                print("5. Nama Dokter")
                                print("6. Selesai")
                                edit_choice = input("Masukkan angka pilihan (1-6): ")
                                
                                if edit_choice == '1':
                                    new_nama_pasien = pyip.inputStr("Masukkan nama pasien baru: ",blockRegexes=[r'[^A-Za-z\s]']).title()
                                    if new_nama_pasien == data['nama_pasien']:
                                        print("Data tidak berubah. Isi dengan informasi lain.")
                                    else:
                                        data['nama_pasien'] = new_nama_pasien
                                elif edit_choice == '2':
                                    new_umur_str = input("Masukkan umur pasien baru: ")
                                    if new_umur_str:
                                        try:
                                            new_umur = int(new_umur_str)
                                            if not (0 <= new_umur <= 100):
                                                raise ValueError
                                            data['umur'] = new_umur
                                        except ValueError:
                                            print("Masukkan umur pasien yang valid!")
                                    else:
                                        print("Umur tidak berubah.")
                                elif edit_choice == '3':
                                    new_kelas = input("Masukkan kelas kamar baru (VIP/I/II/III): ").upper()
                                    if new_kelas in ['VIP', 'I', 'II', 'III']:
                                        data['kelas_kamar'] = new_kelas
                                    else:
                                        print("Kelas kamar tidak valid. Harap masukkan VIP/I/II/III.")
                                elif edit_choice == '4':
                                    new_penjamin = pyip.inputMenu(['ASURANSI', 'BPJS', 'UMUM'], numbered=True, prompt="Pilih 1/2/3:\n")
                                    if new_penjamin in ['ASURANSI', 'BPJS', 'UMUM']:
                                        data['penjamin'] = new_penjamin
                                    else:
                                        print("Penjamin tidak valid. Harap masukkan ASURANSI/BPJS/UMUM.")
                                elif edit_choice == '5':
                                    new_nama_dokter = pyip.inputStr("Masukkan nama dokter baru: ",blockRegexes=[r'[^A-Za-z\s]']).title()
                                    data['nama_dokter'] = new_nama_dokter
                                elif edit_choice == '6':
                                    break
                                else:
                                    print("Pilihan tidak valid.")
                                
                                # Konfirmasi apakah pengguna ingin mengedit kolom lainnya
                                confirm_update = input("Apakah Anda ingin mengupdate kolom lain? (Y/N): ").upper()
                                if confirm_update == 'N':
                                    break
                        
                            # Konfirmasi apakah pengguna ingin menyimpan perubahan
                            confirm_save = input("Apakah Anda yakin ingin menyimpan perubahan? (Y/N): ").upper()
                            if confirm_save == 'Y':
                                print("Data pasien berhasil diperbarui!")
                                edit_data()
                            elif confirm_save == 'N':
                                print("Perubahan data dibatalkan.")
                                edit_data()
                            else:
                                print("Pilihan tidak valid.")
                                edit_data()
                        elif confirm_edit == 'N':
                            print("Pengeditan data dibatalkan.")
                            edit_data()
                        else:
                            print("Pilihan tidak valid.")
                            edit_data()
                        
                        return
                
                print("Data pasien dengan ID tersebut tidak ditemukan.")



        
print("Selamat datang di TrueCare Hospital")
print("Silakan pilih menu yang tersedia untuk memulai.")
menu()