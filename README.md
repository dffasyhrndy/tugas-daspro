#### Nama:  Daffa Syahrandy Husain
#### NIM :  2409116069

#### #Menggunakan time sebagai waktu dari lampu
```import time```

#### #Membuat function lampu lalu lintas
```def lampu_lalulintas(tianglampu):```

```for i in range (10, 0, -1):``` #Menggunakan range untuk menghitung mundur waktu

```print(f"Lampu Merah {tianglampu} - Berhenti selama {i} detik")``` # Sebagai output untuk menampilkan waktu yang menhitung mundur

```time.sleep(1)``` # time.sleep sebagai jeda dari waktu yang ditentukan sebelumnya

```for i in range (5, 0, -1):``` #Menggunakan range untuk menghitung mundur waktu

```print(f"Lampu Kuning {tianglampu} - Bersiap-siap dalam {i} detik")``` # Sebagai output untuk menampilkan waktu yang menhitung mundur

```time.sleep(1)``` # time.sleep sebagai jeda dari waktu yang ditentukan sebelumnya

```for i in range (20, 0, -1):``` #Menggunakan range untuk menghitung mundur waktu

```print(f"Lampu Hijau {tianglampu} - Jalan {i} detik")``` # Sebagai output untuk menampilkan waktu yang menhitung mundur

```time.sleep(1)``` # time.sleep sebagai jeda dari waktu yang ditentukan sebelumnya

#### # Membuat function untuk mendefinisikan tianglampu

```def empat_arah():```

```tianglampu = ("1", "2", "3", "4")```

#### # Melakukan pengulangan tanpa henti menggunakan while True
```while True:```

```for tiang in tianglampu:``` # Melakukan pengulangan untuk tianglampu

```lampu_lalulintas(tiang)```

#### # Memanggil function untuk memulai program

```empat_arah()```
