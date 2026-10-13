num = int(input("Faktöriyelini hesaplamak için bir sayı girin: "))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"{num}!= {factorial}")
num = int(input("Faktöriyelini hesaplamak için bir sayı girin: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"{num}!= {factorial}")
