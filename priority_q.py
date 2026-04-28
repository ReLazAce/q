import heapq

def antrian_rs():
    pq = []
    
    # (prioritas, urutan_kedatangan, nama)
    data = [
        (3, 0, "Budi"),
        (0, 1, "Ani"),
        (2, 2, "Citra"),
        (0, 3, "Dedi"),
        (1, 4, "Eka"),
    ]
    
    # enqueue
    for item in data:
        heapq.heappush(pq, item)
    
    # dequeue
    while pq:
        prioritas, urut, nama = heapq.heappop(pq)
        print(nama)

antrian_rs()