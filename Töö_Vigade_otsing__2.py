print("*** NUMBRIDEGA MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisestage täisarv => "))))  #Lõpetanud koodi 2 sulgudes
        break
    except ValueError:
        print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi peale hakata")
else:
#
    print("Määrake, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c=b=a
    paaris = 0
    paaritu = 0
    while b > 0:     #Lõpetanud koodi :
            if b % 2 == 0:       #Lõpetanud koodi =
                    paaris += 1    #Vahetas märke + и =
            else:
                    paaritu += 1    #Vahetas märke + и =
            b = b // 10
    print("Paarisarvud:", paaris)   #Lõpetanud koodi ,
    print("paarituid numbreid:", paaritu)   #Lõpetanud koodi ,
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörake * sisestatud number")
    print()
    b=0
    while a > 0:       #Lõpetanud koodi :
        number = a % 10
        a = a // 10
        b = b * 10
        b += number #Vahetas märke + и =
    print("*Tagurpidi* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Syracuse hüpoteesi testimine")    #Kustutatud koodi sulgud
    print()
    if c % 2 == 0:   #Lõpetanud koodi =
        print(c," - paarisarv. Jagage poolt 2.")
    else:
        print(c," - paaritu number. Korrutage 3-ga, lisage 1 ja jagage 2.")
    while c != 1:
            if c % 2 == 0:   #Lõpetanud koodi =
                    c = c / 2   #Kustutatud koodi =
            else:
                    c = (3*c + 1) / 2   #Kustutatud koodi =
            print(round(c), end=" ")   #Lisas kindla kirjavahemärgi
    print()
    print("Hüpotees on õige")   #Lisas kindla kirjavahemärgi