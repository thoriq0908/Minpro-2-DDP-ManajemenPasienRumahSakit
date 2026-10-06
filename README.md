<div align="center">

<h1 id="readme-top">SISTEM PENGELOLAAN DATA PASIEN OPNAME DI RUMAH SAKIT</h1>
<h3 align="center"> Program ini dibuat untuk mengelola data pasien opname rumah sakit, dengan dua peran: admin (bisa CRUD semua data) dan pasien (hanya bisa mengelola data miliknya sendiri(CRU).</h3>

  <p align="center">
    NAMA: Muhammad Thoriq Kamil | NIM: 047 | KELAS: B
    <br />


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

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>




## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/github_username/repo_name/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=github_username/repo_name" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License



