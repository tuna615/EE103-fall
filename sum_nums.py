num = int(input("Bir sayı girin: "))

# Döngü ile toplam hesaplama
total_sum = 0
for i in range(1, num + 1):
    total_sum += i

# Gauss formülü ile toplam hesaplama
sum_gauss = num * (num + 1) // 2

print(f"Döngü sonucu: {total_sum}")
print(f"Gauss sonucu: {sum_gauss}")

# Kontrol ve karşılaştırma
if total_sum == sum_gauss:
    print("My running sum code works correctly")
else:
    print("My running sum code failed badly")