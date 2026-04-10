while True:
    print("\nMenu Matriks:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("0. Exit")
    
    p = input("Pilih menu: ")

    if p == "0":
        print("Program Selesai.")
        break

    b = int(input("Input jumlah baris: "))
    k = int(input("Input jumlah kolom: "))

    A = []
    print("Input elemen Matriks A:")
    for i in range(b):
        row = []
        for j in range(k):
            nilai = int(input())
            row.append(nilai)
        A.append(row)

    B = []
    print("Input elemen Matriks B:")
    for i in range(b):
        row = []
        for j in range(k):
            nilai = int(input())
            row.append(nilai)
        B.append(row)

    print("Hasil Perhitungan:")
    for i in range(b):
        for j in range(k):
            if p == "1":
                hasil = A[i][j] + B[i][j]
            elif p == "2":
                hasil = A[i][j] - B[i][j]
            elif p == "3":
                hasil = A[i][j] * B[i][j]
            
            print(hasil, end=" ")
        print()