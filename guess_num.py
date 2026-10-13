# guess_num.py (5 Hak Sınırı ve Sonsuz Döngü)
from secret_number import secretNum

attempts = 0

while True:
    guess = int(input("Bir sayı tahmin edin: "))
    attempts += 1
    
    if guess == secretNum:
        print("Tebrikler, doğru bildiniz!")
        break
    elif guess < secretNum:
        print("Çok düşük!")
    else:
        print("Çok yüksek!")
        
    if attempts >= 5:
        print("5 hakkınız bitti!")
        while True:
            print("Oh! Noooooo...")