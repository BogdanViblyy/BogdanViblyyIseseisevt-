



print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Mis on sinu nimi?").capitalize()
print(nimi + ", oi kui ilus nimi!")
vastus = int(input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
if vastus == 1:
    pikkus = float(input(nimi + "Mis on sinu pikkus?"))
    mass = float(input("Sõber, mis on sinu mass?"))
    indeks = mass/(0.01*pikkus)**2
    print(nimi + "! Sinu keha indeks on:",round(indeks,1))
    if indeks<=16:
        kaal="Tervisele ohtlik alakaal"	
    elif 16<indeks<=19:
        kaal="Alakaal"
    elif 19<indeks<=25:
        kaal="Normaalkaal"
    elif 25<indeks<=30:
        kaal="Ülekaal"
    elif 30<indeks<=35:
        kaal="Rasvumine"
    elif 35<indeks<=40:
        kaal="Tugev rasvumine"
    elif 40<indeks:
        kaal="Tervisele ohtlik rasvumine"
else:
    print("Kahju! See on väga kasulik info!")
    print()
    print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")