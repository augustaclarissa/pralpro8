#Augusta Clarissa Silvy Pascalin
#Universitas Kristen Duta Wacana
#Topik : Lists

'''Rissa memiliki perpustakaan pribadi di rumahnya. Meskipun Ia sudah memiliki banyak buku, Ia merasa ingin membeli buku 
lagi dan lagi. Karena Rissa kesulitan dalam penyimpanan buku - bukunya, Ia ingin menata ulang semua bukunya sesuai abjad. 
Maka dari itu Ia butuh mencatat judul buku - buku yang Ia punya dan karena mengurutkan buku - buku tersebut membutuhkan 
waktu lama apabila menggunakan cara manual, Rissa butuh bantuanmu untuk mengurutkan buku - bukunya dengan program yang 
kamu buat.'''

#input : judul buku lama + judul buku baru
#proses : memasukkan ke dalam list, menambahkan judul baru, mengurutkan sesuai abjad
#output : daftar buku, semua buku, judul buku yang sudah diurutkan

judul = input("Judul Buku Lama (pemisah koma) : ")
judul = judul.split(",")
print('DAFTAR BUKU RISSA = ', judul)

tambah = input("Judul Buku Baru (pemisah koma) : ")
x = tambah.split(",")
judul.extend(x)
print('SEMUA BUKU RISSA = ', judul)

judul.sort()
print('JUDUL BUKU SESUAI URUTAN ABJAD = ', judul)