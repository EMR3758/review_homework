def for_loop():
    num = int(input("Lütfen bir sayı giriniz:"))
    i = 1

    sayı = 0
    for i in range(num+1):
        sayı += i
        

    print(f"For döngüsü ile toplam {sayı}")
    
def while_loop():
    n = int(input("Lütfen bir sayı giriniz:"))
    i = 1
    sayı = 0
    while i <= n :
        sayı += i
        i += 1
    print(f"While döngüsü ile toplam:{sayı}")    


for_loop()
while_loop()

