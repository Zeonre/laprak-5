def hitung_ips():
    bobot = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    
    jumlah_mk = int(input("Berapa jumlah mata kuliah? "))
    
    total_bobot = 0
    total_sks = jumlah_mk * 3  
    
    for i in range(1, jumlah_mk + 1):
        while True:
            nilai = input(f"Nilai MK {i}: ").strip().upper()
            if nilai in bobot:
                total_bobot += bobot[nilai] * 3  
                break
            else:
                print("Nilai tidak valid! Masukkan A, B, C, atau D.")
    
    ips = total_bobot / total_sks
    print(f"Nilai IPS anda semester ini {ips:.2f}")

hitung_ips()
