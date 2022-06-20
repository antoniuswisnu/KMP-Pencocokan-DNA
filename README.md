# KMP-Pencocokan-DNA
Projek Akhir Analisis Algoritma dan Struktur Data

dibuat oleh:
- Akbar Fajar Ramadhan
- Herjati Aji
- Antonius Krisargo Wisnuaji Nugroho

Algoritma pencocokan string merupakan sebuah urutan sebuah metode untuk menentukan letak sebuah subteks di dalam suatu teks. Secara umum, pencocokan string terdiri dari teks dan subteks. Teks adalah sebuah string dengan panjang n karakter. Subteks adalah sebuah string dengan panjang m karakter (m < n) yang akan dicari pada teks.

Algoritma Knuth-Morris-Pratt merupakan sebuah perkembangan dari algoritma Brute Force. Algoritma Knuth-Morris-Pratt ini memiliki metode yang sama dengan menggeser perbandingan dari kiri ke kanan. Namun, pergeseran yang terjadi tidak selalunya bernilai satu.
Algoritma Knuth-Morris-Pratt ini mengambil irisan dari sebuah prefix dan suffix dari sebuah subteks yang sama. 

Prefix adalah sebuah potongan teks dari sebuah teks yang pasti memiliki indeks awal dari teks dengan panjang p (p < m) dimana m adalah panjang teks. Sedangkan suffix juga merupakan potongan teks dari sebuah teks yang mengandung indeks terakhir dari teks induk dengan dibatasi array l (l < m) dimana m adalah panjang teks.
