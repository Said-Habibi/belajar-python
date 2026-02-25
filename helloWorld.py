print("Hello world")

a = 1
b = "ini String"
c = True
e = 1.1
f = [
    a,b,c,e,
]
g = {
    "Lokasi" : "pekanbaru"
}

print(type(a))
print(type(b))
print(type(c))
print(type(e))
print(type(f))
print(type(g))

# for di gunakan ketika loop sudah di ketahui berapa banyak perulangan yang akan dilakukan
for i in f: # i  di dalam f sama saja seperti f[i] jadinya yang diprint adalah isi dari list f kalau kalian lakukan ini ke map itu tidak bisa karena map menggunakan key untuk mengakses value nya beda dengan list dia menggunakan index auto iterasi mangkannya bisa menggunakan for in range atau for in
    print(i)


def tambah(m, n):
    try:
        m = int(m)
    except ValueError:
        print("pls enter a INTEGER")
    n = int(n)
    return m + n
keadaan = False

# while di gunakan ketika loop belum di ketahui kapan berhentinya seperti di bawah ini ketika user memasukan string program akan mengulang terus sampai si user memasukan integer atau float ke dalam while ini
while(not keadaan):
    # try di sini untuk mencoba kode akan berjalan normal atau tidak jika tidak di lempar ke except untuk mengetahui errornya tanpa menghentikan program atau tetap akan berhenti jika kalian tidak ingin menjalankan program sebelum kode benar
    try:
        num1 = int(input("masukan integer: "))
        num2 = int(input("masukan integer2: "))
        keadaan = True
    except ValueError:
        print("error masukan nomor")
hasil = tambah(num1,num2)
print(hasil)

# ini adalah fungsi rekursif, fungsi ini memanggil dirinya sendiri hingga menyentuh base case atau akhir dari rekursifnya, ini sangat membantu ketika kita ingin memanggil si fungsi di dalam fungsi nya tersendiri, namun ada bahaya ketika kita memasukan jumlah rekursif yang besar program akan otomatis berhenti karena adanya stack overflow.
def faktorial(n):
    if n <= 1:
        return 1
    else:
        return n * faktorial(n - 1)
print(faktorial(9))