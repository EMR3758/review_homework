number = int(input("Lütfen bir sayı giriniz: "))

if number > 0:
    if number % 2 == 0:
        print("Girdiğiniz sayı çift.")
    else:
        print("Girdiğiniz sayı tek.")
elif number < 0:
    print("Negatif sayı girdiniz.")

