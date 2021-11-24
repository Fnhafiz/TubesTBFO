from F05 import tambahGadget, tambahConsumable
from F06 import hapusGadget, hapusConsumable
from F07 import ubahGadget, ubahConsumable
from F08 import pinjamGadget, cari
from F09 import kembalikanGadget, cariPinjam, tampilkanPinjam

gadget = [[ 0 for j in range(6)]for i in range(100)]
consumable = [[ 0 for j in range(5)]for i in range(100)]
pinjam = [[ 0 for j in range(6)]for i in range(100)]
user = [[ 0 for j in range(6)]for i in range(100)]
#f01 - f04
def generateUserID(): 
    temp = 0
    with open('user.csv') as data:
        for line in data:
            temp += 1
        temp = temp + 1
    return ('ID'+ str(210418000 + temp))

#fungsi untuk menginput data kedalam user.csv
def registerUser(id, nama, username, password, alamat, role,user):
    #x = f'{id};{nama};{username};{password};{alamat};{role}\n'
    with open('user.csv', 'a') as data:
        data.write(x)
    user[0] = id
    user[1] = nama
    user[2] = username
    user[3] = password
    user[4] = alamat
    #print(f'User {username} telah berhasil register ke dalam Kantong Ajaib.')
#fungsi untuk memisahkan data per semicolon(;) di dalam file csv

def parseSemicolon(str):
    retArr = []
    i = 0
    while i < len(str):
        if str[i] != ';':
            i += 1
        else:
            retArr.append(str[i:i])
            str = str[i+1:]
            i = 0
    retArr.append(str)
    return retArr #mengembalikan data yang sudah dipisah dalam bentuk array of string

#fungsi untuk membuat user id yang akan diinput di user.csv dan dibuat secara otomatis


#fungsi untuk membaca file user.csv dan mengembalikannya dalam bentuk array of dictionary
def loadUsers():
    users = []
    with open('user.csv') as data:
        for line in data:
            tempDict = {}
            tempArr = parseSemicolon(line)
            tempDict['id'] = tempArr[0]
            tempDict['nama'] = tempArr[1]
            tempDict['username'] = tempArr[2]
            tempDict['password'] = tempArr[3]
            tempDict['alamat'] = tempArr[4]
            tempDict['role'] = tempArr[5]
            users.append(tempDict)
    return users
#fungsi untuk membaca file gadget.csv dan mengembalikannya dalam bentuk array of dictionary
def loadGadgets():
    gadgets = []
    with open('gadget.csv') as data:
        for line in data:
            tempDict = {}
            tempArr = parseSemicolon(line)
            tempDict['ID'] = tempArr[0]
            tempDict['nama'] = tempArr[1]
            tempDict['deskripsi'] = tempArr[2]
            tempDict['jumlah'] = tempArr[3]
            tempDict['rarity'] = tempArr[4]
            tempDict['tahun'] = tempArr[5]
            gadgets.append(tempDict)
    return gadgets


def validasiTanggal(tanggal) :
    hari = int(tanggal[0]) * 10 + int(tanggal[1] )
    bulan = int(tanggal[3]) *10 + int(tanggal[4]) 
    if hari >0 and hari <=31 and bulan >0 and bulan <=12 and int(tanggal[6]) >0 :
        return True
    else :
        return False
#fungsi untuk print data gadget, fungsi ini digunakan sebagai template

def printDataGadget(x):
    print("Nama            : ")
    print("Deskripsi       : ")
    print("Jumlah          : ")
    print("Rarity          : ")
    print("Tahun Ditemukan : ")
    print()

#fungsi untuk mencari data gadget berdasarkan kategori rarity
def searchByRarity(rarity, gadgetData):
    print('Hasil pencarian: ')
    count = 0
    for x in gadgetData:
        if x['rarity'] == rarity:
            count += 1
            printDataGadget(x)
    if count == 0:
        print('Tidak ditemukan data dengan rarity.')
 
#fungsi untuk mencari data gadget berdasarkan kategori tahun 
def searchByTahun(tahun, kategori, gadgetData):
    print('Hasil pencarian: \n')
    count = 0
    for x in gadgetData:
        if kategori == '>':
            if int(x['tahun']) > int(tahun):
                count += 1
                printDataGadget(x)
        elif kategori == '<':
            if int(x['tahun']) < int(tahun):
                count += 1
                printDataGadget(x)
        elif kategori == '>=':
            if int(x['tahun']) >= int(tahun):
                count += 1
                printDataGadget(x)
        elif kategori == '<=':
            if int(x['tahun']) <= int(tahun):
                count += 1
                printDataGadget(x)
        elif kategori == '=':
            if int(x['tahun']) == int(tahun):
                count += 1
                printDataGadget(x)
    if count == 0:
        print('Tidak ditemukan data dengan tahun .')

role = ''
print(loadUsers())
while True:
    userData = loadUsers()
    gadgetData = loadGadgets()
    prompt = input()

#f01    
    if prompt.lower() == 'register':
        nama = input('Masukan nama: ')
        username = input('Masukan username: ')
        isUnique = True
        for x in userData:
            if x['username'] == username:
                isUnique = False
                break
        if not isUnique:
            print('Username tidak unik. Silakan register kembali.')
        else:
            password = input('Masukan password: ')
            alamat = input('Masukan alamat: ')
            uid = generateUserID()
            registerUser(uid, nama, username, password, alamat, 'user')
   
#f02
    if prompt.lower() == 'login':
        notfound = True
        tempPass = ''
        tempRole = ''
        while notfound :
            inputuser = input("Masukan username: ")
            for line in userData:
                if line['username'] == inputuser:
                    tempPass = line['password']
                    tempRole = line['role']
                    notfound = False
            if notfound :
                print("username tidak ditemukan")
        if not notfound :
            belommasuk = True
            while belommasuk :
                inputPass = input('Masukan password: ')
                if inputPass == tempPass:
                    print("Hallo ! Selamat datang di Kantong Ajaib.")
                    role = tempRole
                    belommasuk = False
                else:
                    print('Password salah')

#f03
    print("Pilihan Menu :")
    print("1. Menambah item ")
    print("2. Hapus item")
    print("3. Ubah Jumlah item")
    print("4. Pinjam Gadget")
    print("5. Kembalikan Gadget")
    print("99. Keluar aplikasi") 
    x = int(input("Masukkan nomor yang diinginkan "))
    if x == 1 :
        id_benda = input("Masukkan ID: ")
        benar = 0
        if id_benda[0] == "G" :
            gadget = tambahGadget(gadget,id_benda)
        elif id_benda[0] == "C" :
            consumable = tambahConsumable(consumable,id_benda)
        else :
            print("Gagal menambahkan item karena ID tidak valid")
    elif x == 2 :
        id_benda = input("Masukkan ID: ")
        benar = 0
        if id_benda[0] == "G" :
            gadget = hapusGadget(gadget,id_benda)
        elif id_benda[0] == "C" :
            consumable = hapusConsumable(consumable,id_benda)
        else :
            print("Gagal menambahkan item karena ID tidak valid")
    elif x == 3 :
        id_benda = input("Masukkan ID: ")
        benar = 0
        if id_benda[0] == "G" :
            gadget = ubahGadget(gadget,id_benda)
        elif id_benda[0] == "C" :
            consumable = ubahConsumable(consumable,id_benda)
        else :
            print("Gagal menambahkan item karena ID tidak valid")
    elif x == 4 :
        id_benda = input("Masukkan ID: ")
        indeks = 0
        if id_benda[0] == "G" :
            tanggal = input("Tanggal peminjaman: ")
            while benar ==0 :
                    tanggal = input("Tanggal pengembalian: ")
                    if (validasiTanggal) :
                        benar = 1
            pinjam = pinjamGadget(gadget,pinjam,id_benda,tanggal,jumlah)
            indeks = cari(gadget,id_benda)
            gadget[indeks][3] = gadget[indeks][3] -jumlah           
        else :
            print("Gagal menambahkan item karena ID tidak valid")
    elif x == 5 : 
        if id_benda[0] == "G" :
            nomor = tampilkanPinjam(pinjam)
            if pinjam[nomor][0] != 0 :
                jumlah = int(input("Masukkan jumlah gadget yang dikembalikan: "))
                benar = 0
                while benar ==0 :
                    tanggal = input("Tanggal pengembalian: ")
                    if (validasiTanggal) :
                        benar = 1
                pinjam = kembalikanGadget(gadget,pinjam,id_benda,jumlah,nomor)
            else :
                print("Masukkan nomor peminjaman yang benar")
            indeks = cariPinjam(gadget,pinjam,id_benda,nomor,jumlah) 
            gadget[indeks][3] = gadget[indeks][3] + jumlah
        else :
            print("Gagal menambahkan item karena ID tidak valid")
    if prompt.lower() == 'carirarity':
        if role == 'Admin' or role == 'User':
            rarity = input('Masukkan rarity: ')
            searchByRarity(rarity, gadgetData)
        elif role == '':
            print('Silahkan login terlebih dahulu')
        else: 
            print("Akses tidak bisa dilakukan")
 
#f04
    if prompt.lower() == 'caritahun':
        if role == 'Admin' or role == 'User':
            tahun = input('Masukkan tahun: ')
            kategori = input('Masukkan kategori: ')
            searchByTahun(tahun, kategori, gadgetData)
        elif role == '':
            print('Silahkan login terlebih dahulu')
        else:
            print("Akses tidak bisa dilakukan")

    