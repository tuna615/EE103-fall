# cube_root_guess.py
given_number = int(input("Küp kökünü bulmak için bir tam sayı girin: "))

is_negative = given_number < 0
abs_num = abs(given_number)

guess = 0
found = False

while guess ** 3 <= abs_num:
    if guess ** 3 == abs_num:
        cube_root = -guess if is_negative else guess
        print(f"{given_number} sayısının küp kökü: {cube_root}")
        found = True
        break
    guess += 1

if not found:
    print(f"{given_number} tam bir küp sayı değildir.")