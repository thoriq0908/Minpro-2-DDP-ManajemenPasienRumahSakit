<div align="center">

<h1 id="readme-top">SISTEM PENGELOLAAN DATA PASIEN OPNAME DI RUMAH SAKIT</h1>
<h3 align="center"> Program ini merupakan pengembangan dan penyempurnaan dari program dengan penambahan beberapa method,fungsi,sistem yang membuat program lebih dapat digunakan. </h3>

  <p align="center">
    NAMA: Muhammad Thoriq Kamil | NIM: 047 | KELAS: B
    <br />
<div align= "left">
<br>
  
## Deskripsi singkat Program

Program ini dibuat untuk mengelola data pasien opname rumah sakit, dengan dua peran: admin (bisa CRUD semua data) dan pasien (hanya bisa mengelola data miliknya sendiri(CRU). Pengguna harus login terlebih dahulu dengan username dan password. Setelah login, menu yang tampil bergantung pada role:

| Role | Username / Password | Hak Akses |
|------|---------------------|-----------|
| **Admin** | admin / 123 | CRUD lengkap: tambah, tampilkan, ubah, dan hapus data **semua** pasien |
| **Pasien** | pasien / 123 | Hanya dapat menambah (maksimal 1), menampilkan, dan mengubah data **miliknya sendiri** |

Data pasien yang disimpan: **nomor rekam medis (RM), nama, umur, dan ruangan**.

**Konsep & library yang digunakan**
- **Dictionary**: `akun_pengguna` (data akun) dan `data_pasien` (data pasien, key = nomor RM)
- **Function**: login, validasi, fungsi CRUD, menu per role, dan `main()`
- **Conditional statement**: validasi input angka, input kosong, nomor RM duplikat, pilihan menu
- **Library**: `pwinput` (password tersamar saat diketik), `prettytable` (tampilan tabel), `os` (membersihkan layar)

<br>

## Flowchart dan Penjelasan Alur

<img width="3614" height="2503" alt="FLOWCHART MINPRO 2 THORIQ" src="https://github.com/user-attachments/assets/d58afbb5-486a-4198-ac96-f42614b452b8" />

<br>
Program dimulai dengan input pilihan 1/2:
<br>

**1. untuk login** <br>
**2. untuk keluar** <BR>
jika input = 2, program berakhir<br>
jika input = 1, program berlanjut untuk meminta input berupa username dan password<BR>
program akan melakukan loop jika input kosong atau tidak berupa angka 1/2. <BR>
Setelah menginput 1, program meminta untuk menginput username dan password, dan akan lanjut masuk ke login sebagai admin atau user(pasien) jika input sesuai dengan data yang tersimpan, jika salah atau username dan password tidak sesuai, program akan looping ulang ke input user yaitu pilihan 1/2. <br>

###  Login sebagai admin
program dimulai dengan pemilihan yang meminta input 1-5:<br>
1. Tambah data pasien<BR>
2. Tampilkan data pasien<BR>
3. Ubah data pasien <br>
4. Hapus data pasien<BR>
5. Logout <br>
   
**1. Tambah data pasien:** dimulai dengan input no.rm medis yang menggunakan conditional statement untuk memastikan "apakah no.rm sudah ada?" dan "apakah input berupa angka?", lalu menginput nama, umur, dan ruangan yang juga menggunakan conditional statement dengan tujuan yang sama, dan jika sudah selesai menginput semua, program akan kembali ke program pemilihan. <br>

**2. Tampilkan data pasien:** program akan langsung mengeluarkan output berupa data pasien yang tersismpan, jika tidak ada data yang tersimpan, maka output akan berupa print "belum ada data yang tersimpan", dan program kembali ke program pemilihan. <BR>

**3. Ubah Data Pasien:** program dimulai dengan input no.rm yang ingin diubah, yang dicek menggunakan conditional statement juga, jika belum ada data yang tersimpan program akan output print "belum ada data yang tersimpan", jika ada, maka program akan lanjut mengubah data pada no.rm yang terdaftar tersebut, berupa input nama baru, umur baru, dan ruangan baru. Lalu program akan mengeluarkan output print "data berhasil diubah" dan kembali ke program pemilihan. <BR>

**4. Hapus Data Pasien:** program dimulai dengan input no.rm yang ingin dihapus, yang dicek menggunakan conditional statement juga, jika belum ada data yang tersimpan program akan output print "belum ada data yang tersimpan", jika ada, maka program akan langsung menghapus data pada no.rm yang terdaftar tersebut. Lalu program akan mengeluarkan output print "data berhasil dihapus" dan kembali ke program pemilihan. <BR>

**5. Logout:** Untuk keluar dari program pemilihan, user/admin perlu menginput 5 yaitu logout yang akan langsung keluar dari program dan kembali ke pemilihan awal berupa login dan keluar(1/2)<br>

### Login sebagai user(pasien)
program dimulai dengan pemilihan yang meminta input 1-4:<br>
1. Tambah data saya <BR>
2. Tampilkan data saya<BR>
3. Ubah data saya  <br>
4. Logout <br>

**1. Tambah data saya:** dimulai dengan input no.rm medis yang menggunakan conditional statement untuk memastikan "apakah no.rm sudah ada?" dan "apakah input berupa angka?", lalu menginput nama, umur, dan ruangan yang juga menggunakan conditional statement dengan tujuan yang sama, dan jika sudah selesai menginput semua, program akan kembali ke program pemilihan. <br>

**2. Tampilkan data pasien:** program akan langsung mengeluarkan output berupa data diri sendiri yang tersismpan, jika tidak ada data yang tersimpan, maka output akan berupa print "belum ada data yang tersimpan", dan program kembali ke program pemilihan. <BR>

**3. Ubah Data Pasien:** program dimulai dengan menampilkan data diri sendiri yang ingin diubah, jika belum ada data yang tersimpan program akan output print "belum ada data yang tersimpan", jika ada, maka program akan lanjut mengubah data diri terdaftar tersebut, berupa input nama baru, umur baru, dan ruangan baru. Lalu program akan mengeluarkan output print "data berhasil diubah" dan kembali ke program pemilihan. <BR>

**4. Logout:** Untuk keluar dari program pemilihan, user perlu menginput 4 yaitu logout yang akan langsung keluar dari program dan kembali ke pemilihan awal berupa login dan keluar(1/2)<br>

<BR>

## Dokumentasi Program dan Output
<img width="386" height="154" alt="Screenshot 2026-10-06 205424" src="https://github.com/user-attachments/assets/108601df-ce56-4bf4-b509-444e6b275c8b" /> <BR>
program dimulai dengan memanggil library; pwinput,PrettyTable,Os, yang akan di gunakan dalam program selanjutnya, diawal juga terdapat dictionary akun_pengguna yang menyimpan username,password dan role yang digunakan untuk login. dan ada dictionary kosong berupa data_pasien yang berfungsi untuk menyimpan data pasien.<br>
<br>

**Function Validasi:** <br>
<img width="356" height="203" alt="image" src="https://github.com/user-attachments/assets/51300790-9970-4ad9-98f0-784a2b6ddece" />
 <br>
di fungsi ini terdapat funtion validasi yang berguna untuk memastikan bahwa inputan user/admin itu tidak kosong atau harus berupa angka, dan menggunakan loop, if else, serta try except untuk menghindari eror dan user/admin harus memberi input<br>
<br>

**Function Login:** <br>
<img width="395" height="137" alt="Screenshot 2026-10-06 203420" src="https://github.com/user-attachments/assets/04f1cb72-c3a5-49ab-820d-fb9b7c7280ff" /> <br>
di function ini terdapat input username dan password, di input password menggunakan pwinput agar input password menjadi tersensor karena password bersifat privat, lalu if else untuk memastikan input username dan password apakah terdapat di dictionary akun_pengguna, jika ya maka login berhasil, jika tidak maka login gagal.<br>
<br>

**Function Admin:** <br>
<img width="452" height="287" alt="Screenshot 2026-10-06 213143" src="https://github.com/user-attachments/assets/3d65bf95-f719-4840-92bf-a6cd902da425" /> <br>
- Tambah pasien: admin menginput no.rm, lalu di cek menggunakan if else apakah no.rm sudah terdaftar di dictionary data_pasien jika iya maka akan keluar output print "Masukkan nomor berbeda", jika no.rm belum terdaftar, maka akan masuk ke input nama,umur,ruangan pasien yang menggunakan function validasi di awal tadi agar input sesuai. <BR>
- Tampil pasien: menampilkan isi pada dictionary data_pasien, jika data_pasien==0 maka belum ada data yang terdaftar, jika ada maka menggunakan Library PrettyTable pada data yang tersimpan di data_pasien yang disusun berupa no.rm,nama,umur,ruangan, dan di akhir mengeluarkan print jumlah orang yang opname dengan len(data_pasien). <BR>

<img width="512" height="281" alt="Screenshot 2026-10-06 220005" src="https://github.com/user-attachments/assets/a3d6fbb8-a1b2-4df7-8c38-ef01ebf28a16" /> <br>
- Ubah pasien: jika data di data_pasien = 0, maka print"tidak ada data pasien yang tersimpan", jika data ada, maka dilanjut menginput no.rm pasien yang dicek dictionary data_pasien, jika nomor rm ada, maka dilanjut input nama,ummur, dan ruangan yang menggunakan function validasi,  jika no.rm tidak ada, maka output print "no.rm tidak ditemukan".<BR>
- Hapus Pasien: jika data di data_pasien = 0, maka print "tidak ada data pasien yang tersimpan", jika data ada, maka  dilanjut menginput no.rm pasien yang dicek dictionary data_pasien, jika nomor rm ada, maka data pasien langsung terhapus dari dictionary, jika no.rm tidak ada, maka output print "no.rm tidak ditemukan".<BR>
<BR>

**Function User(pasien):** <br>
<img width="478" height="218" alt="Screenshot 2026-10-06 220958" src="https://github.com/user-attachments/assets/b245c7e0-2b2a-41cd-928c-02bbd71577e7" /> <br>
- Punya Data: function ini mengecek apakah akun pasien sudah memiliki data di database. Hasilnya True atau False.
  nomor_rm is not None: akun sudah pernah menambahkan data.
  nomor_rm in data_pasien: nomor RM tersebut masih ada di database (belum dihapus admin). <br>
- Tambah Data Sendiri: di function ini mengecek apakah username pada function punya data sudah berisi, jika iya, maka print "anda sudah memiliki data dan hanya bisa memilki satu data milik sendiri, jika tidak, maka input no.rm dan dicek di dictionary data_pasien, jika nomor rm ada, maka dilanjut input nama,ummur, dan ruangan yang menggunakan function validasi,  jika no.rm tidak ada, maka output print "no.rm tidak ditemukan".<BR>
<img width="413" height="256" alt="Screenshot 2026-10-06 221033" src="https://github.com/user-attachments/assets/26aee541-1c25-49b9-9863-9e9a043b8c0d" /> <br>
- Tampil Data Sendiri: pada function ini, data yang tersimpan pada dictionary data_pasien tetapi yang terkhusus pada nomor rm yang terdapat di function punya data akan dibuat menjadi tabel yang disusun menggunakan library prettyTable, jika punya data masih None maka print "anda belum memiliki data".<br>
- Ubah Data Sendiri: pada function ini, jika nomor rm yang ada di punya data terdaftar atau ada maka input nama,umur ruangan baru yang sudah disertakan function validasi agar input sesuai, dan jika punya data masih kosong maka print "anda belum memiliki data.<br>
<br>
  
**Function Menu per Role** <br>
<img width="377" height="263" alt="Screenshot 2026-10-06 223733" src="https://github.com/user-attachments/assets/b7a3e70c-6232-40cd-ba2c-ed958997fe7d" /> <br>
- Function menu Admin: di function ini dimulai dengan loop print dan menu pilihan 1-5 dan tiap pilihhan akan masuk ke masing masing function yang telah dibuat sebelumnya, jika input selain 1-5 maka output print "pilihan tidak valid" dan lanjut loop, loop akan berhenti jika user/admin memilih 5 yaitu logout.<br>
<br>
<img width="368" height="231" alt="Screenshot 2026-10-06 223751" src="https://github.com/user-attachments/assets/fd5c7b75-8b69-45f9-9833-bf1131d687e6" /> <br>
- Function menu Pasien: di function ini dimulai dengan loop print dan menu pilihan 1-4 dan tiap pilihhan akan masuk ke masing masing function yang telah dibuat sebelumnya, jika input selain 1-4 maka output print "pilihan tidak valid" dan lanjut loop, loop akan berhenti jika user/admin memilih 4 yaitu logout.<br>
<br>

**Function Menu Utama** <br>
<img width="362" height="286" alt="Screenshot 2026-10-06 223812" src="https://github.com/user-attachments/assets/48b1257c-5d6e-41dc-9585-1d2737ada3db" /> <<br>
di function ini dimulai dengan loop print dan menu pilihan 1/2, jika input 1 maka memanggil function login dan jika role admin dia akan masuk ke function menu admin, jika role user dia akan masuk ke function menu pasien. Jika input 2 maka program berakhir, jika input selain 1/2 maka output print "pilihan tidak valid" dan lanjut loop.<br>
lalu diakhir program memanggil funtion menu utama yang menggunakan try except yang berguna jika user input CTRL + C, output tidak error, tetapi print "Program dihentikan oleh ai".
<br>

### Output
<img width="960" height="600" alt="Screenshot 2026-10-06 225809" src="https://github.com/user-attachments/assets/c85ace66-09cc-420d-ab13-99d8913dce19" /> <br>
Tampilan awal program dan tes conditional statement serta bentuk password yang menggunakan pwinput. <br>
<br>
**Menu Admin:** <br>
<img width="276" height="197" alt="Screenshot 2026-10-06 230126" src="https://github.com/user-attachments/assets/03dc8808-696c-4fb2-ba5c-a46a6f2aeb66" /> <br>
tampilan awal menu admin. <br>
<br>
<img width="359" height="290" alt="Screenshot 2026-10-06 230426" src="https://github.com/user-attachments/assets/965b099d-3e3e-4e45-adfc-85a7b97651fb" /> <br>
contoh tambah data dan penerapan conditional statement. <br>
<br>
<img width="289" height="228" alt="Screenshot 2026-10-06 230654" src="https://github.com/user-attachments/assets/4642d0f5-9f13-47b3-b5fe-5c86ec695771" /> <br>
contoh tampilkan data dan bentuk dari tabel yang menggunakan Library Prettytable. <br>
<br>
<img width="355" height="290" alt="Screenshot 2026-10-06 230922" src="https://github.com/user-attachments/assets/9195de82-ec9b-475c-93e9-d16639ecf33c" /> <br>
contoh ubah data dan kondisi ketika no.rm yang diinput tidak ada pada data_pasien. <br>
<br>
<img width="400" height="317" alt="image" src="https://github.com/user-attachments/assets/6407ef5f-7027-4ec9-a948-45166326062c" /> <br>
contoh hapus data dan kondisi ketika no.rm yang ingin dihapus tidak ada dan update tampilaan data atau(read) yang datanya sudah terhapus. <br>
<br>
<br>
**Menu Pasien** <br>
<img width="262" height="265" alt="image" src="https://github.com/user-attachments/assets/d4157498-b878-4a0a-ae87-73c39b0f4eb4" /> <br>
output tampilan menu pasien dan percobaan input selain 1-4(kosong). <br>
<br>
<img width="326" height="182" alt="image" src="https://github.com/user-attachments/assets/2da88774-cf42-4e4d-be83-d4060c8fa0b6" /> <br>
output menu pilihan 1 yaitu tambah data, dan penerapan conditional statement.<br>
<br>
<img width="274" height="131" alt="image" src="https://github.com/user-attachments/assets/4392029b-17ac-43e7-8439-d5f2c56741c5" /> <br>
output menu pilihan 2 yaitu tampilkan data, menggunakan library pretty table.<br>
<br>
<img width="362" height="276" alt="image" src="https://github.com/user-attachments/assets/b2191e8f-fcc4-4489-beda-2f14217c7e7a" /> <br>
output menu pilihan 3 yaitu ubah data, menggunakan conditional statement dan bukti pada tampilan data yang berubah.<br>
<br>
<br>
<img width="301" height="242" alt="Screenshot 2026-10-06 232633" src="https://github.com/user-attachments/assets/45c4440b-f3e7-4e41-8881-a84c4dc6800a" /> <br>
contoh output ketika no,rm sudah terdapat di dictionary data_pasien sehingga ketika user/pasien ingin menginput no.rm tersebut tidak bisa.<br>
<br>
<BR>
<BR>
## Penjelasan penerapan nilai tambah
<img width="386" height="154" alt="Screenshot 2026-10-06 205424" src="https://github.com/user-attachments/assets/9920a26e-1c72-43a1-ab13-9eeaf63cf4be" /><br>
**Library:** Nilai tambah yang pertama yaitu terdapat pada penerapan library yang minimal 3: <br>
1. pwinput: penerapan pada input password(menjadikan input tersensor) <br>
2. Prettytable: penerapan pada tampilan data(membuat tampilan data lebih rapi dan nyaman dilihat) <br>
3. Os: penerapan pada terminal(menjadikan file saat di run bersih pada terminal) <br>
<br>
<br>
try except 1: <br>
<img width="317" height="110" alt="Screenshot 2026-10-06 233446" src="https://github.com/user-attachments/assets/26dd9bd6-44bb-43d6-a13f-6bb4823991d8" /> <br>
try except 2: <br>
<img width="302" height="64" alt="Screenshot 2026-10-06 233455" src="https://github.com/user-attachments/assets/81d468ad-46c4-4f2a-9ee1-f962530f7b0d" /> <br>

**Error Handling:** Nilai tambah yang kedua berupa Error Handling yang menggunakan try except:<br>
try except 1. : try except disini bermanfaat sebagai pengecek inputan user, yaitu ketika user input selain angka(int) program akan pergi ke except akan mengeluarkan print "input harus berupa angka" dan program kembali looping ke input. <br>
try except 2. :  try except disini berguna sebagai penanganan output error, yaitu ketika user melakukan penghentian paksa program dengan menginput CTRL + C, maka program berhenti dengan output print "program dihentikan oleh pengguna".





