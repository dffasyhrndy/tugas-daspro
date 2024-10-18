import time

def lampu_lalulintas(tianglampu):
    for i in range (10, 0, -1):
        print(f"\rLampu Merah {tianglampu} - Berhenti selama {i} detik", end='')
        time.sleep(1)

    for i in range (5, 0, -1):
        print(f"\rLampu Kuning {tianglampu} - Bersiap-siap dalam {i} detik", end='')
        time.sleep(1)

    for i in range (20, 0, -1):
        print(f"\rLampu Hijau {tianglampu} - Jalan dalam {i} detik", end='')
        time.sleep(1)

def empat_arah():
    tianglampu = ("1", "2", "3", "4")

    while True:
        for arah in tianglampu:
            lampu_lalulintas(arah)

empat_arah()