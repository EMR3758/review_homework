def fin_min_max():
    numbers = []
    for i in range(5):
        num = int(input(f"{i+1}. sayıyı girin: "))
        numbers.append(num)
        
    min_num = min(numbers)
    max_num = max(numbers)

    print(f"En küçük sayı: {min_num}")
    print(f"En büyük sayı: {max_num}")


fin_min_max()
    