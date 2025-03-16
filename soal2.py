def ganjil(bawah, atas):
    if bawah < atas:
        return [i for i in range(bawah, atas + 1) if i % 2 != 0]
    else:
        return [i for i in range(bawah, atas - 1, -1) if i % 2 != 0]

print(ganjil(10, 30))  
print(ganjil(97, 82)) 
