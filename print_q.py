from collections import deque

# Membuat queue
printer_queue = deque()

# Enqueue (menambahkan dokumen)
printer_queue.append("laporan.pdf")
printer_queue.append("tugas.docx")
printer_queue.append("foto.jpg")

# Proses cetak
while printer_queue:
    doc = printer_queue.popleft()
    print(f"Mencetak: {doc}")