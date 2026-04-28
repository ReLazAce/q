import random
from collections import deque

class Penumpang:
    def __init__(self, waktu_datang):
        self.waktu_datang = waktu_datang

class Agen:
    def __init__(self):
        self.sisa_waktu = 0

    def sibuk(self):
        return self.sisa_waktu > 0

    def mulai_layanan(self, waktu_layanan):
        self.sisa_waktu = waktu_layanan

    def tick(self):
        if self.sisa_waktu > 0:
            self.sisa_waktu -= 1

def simulasi(num_menit, num_agen, waktu_layanan, interval_kedatangan):
    queue = deque()
    agen_list = [Agen() for _ in range(num_agen)]

    total_wait = 0
    jumlah_dilayani = 0

    for waktu in range(num_menit):
        # R1: Kedatangan (random)
        if random.randint(1, interval_kedatangan) == 1:
            queue.append(Penumpang(waktu))

        # R2 & R3: Proses agen
        for agen in agen_list:
            if not agen.sibuk() and queue:
                penumpang = queue.popleft()
                wait = waktu - penumpang.waktu_datang
                total_wait += wait
                jumlah_dilayani += 1
                agen.mulai_layanan(waktu_layanan)

            agen.tick()

    if jumlah_dilayani == 0:
        return 0

    return total_wait / jumlah_dilayani

# Contoh simulasi
avg = simulasi(
    num_menit=1000,
    num_agen=2,
    waktu_layanan=5,
    interval_kedatangan=3
)

print(f"Rata-rata waktu tunggu: {avg:.2f} menit")