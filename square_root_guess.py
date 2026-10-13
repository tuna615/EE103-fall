# square_root_guess.py
given_number = int(input("Karekökünü bulmak için bir sayı girin: "))

if given_number < 0:
    print("Square root of negative numbers is not a real number.")
else:
    guess = 0
    found = False
    
    while guess * guess <= given_number:
        if guess * guess == given_number:
            print(f"{given_number} sayısının karekökü: {guess}")
            found = True
            break
        guess += 1
        
    if not found:
        print(f"{given_number} bir tam kare (perfect square) değildir.")