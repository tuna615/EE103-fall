x = float(input("What x to find the cube root of? "))
guess = float(input("What guess to start with? "))

# Newton formülü (küp kök için): nextguess = guess - (guess**3 - x) / (3 * guess**2)
nextguess = guess - ((guess ** 3) - x) / (3 * (guess ** 2))

print("Current estimate cube:", guess ** 3)
print("Next guess:", nextguess)