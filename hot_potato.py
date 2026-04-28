from collections import deque

def hot_potato(names, num):
    q = deque(names)

    while len(q) > 1:
        # Oper sebanyak num kali
        for _ in range(num):
            q.append(q.popleft())

        # Pemain tersingkir
        keluar = q.popleft()
        print(f"Tersingkir: {keluar}")

    return q[0]

# Contoh penggunaan
pemain = ["A", "B", "C", "D", "E"]
pemenang = hot_potato(pemain, 3)

print(f"Pemenang: {pemenang}")