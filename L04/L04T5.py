kiitos = str("Kiitos ohjelman käytöstä.")

print("Tämä laskin osaa seuraavat toiminnot:")
print("1) Anna luvut")
print("2) Summa")
print("3) Erotus")
print("4) Tulo")
print("5) Osamäärä")
print("6) Potenssi")
print("0) Lopeta")

while (True):
    toiminnot = int(input("Valitse toiminto (0-6): "))
    
    if toiminnot == 1:
        luku_a = int(input("Anna ensimmäinen luku: "))
        luku_b = int(input("Anna toinen luku: "))
        print(f"Annoit luvut {luku_a} ja {luku_b}")
        print("Tämä laskin osaa seuraavat toiminnot:")
        print("1) Anna luvut")
        print("2) Summa")
        print("3) Erotus")
        print("4) Tulo")
        print("5) Osamäärä")
        print("6) Potenssi")
        print("0) Lopeta")
        continue
    
    elif toiminnot == 2:
        summa = luku_a + luku_b
        print(f"Summa {luku_a} + {luku_b} = {summa}")
        print("Tämä laskin osaa seuraavat toiminnot:")
        print("1) Anna luvut")
        print("2) Summa")
        print("3) Erotus")
        print("4) Tulo")
        print("5) Osamäärä")
        print("6) Potenssi")
        print("0) Lopeta")
        
    elif toiminnot == 3:
        if luku_a > luku_b or luku_a == luku_b:
            erotus = luku_a - luku_b
            print(f"Erotus {luku_a} - {luku_b} = {erotus}")
            print("Tämä laskin osaa seuraavat toiminnot:")
            print("1) Anna luvut")
            print("2) Summa")
            print("3) Erotus")
            print("4) Tulo")
            print("5) Osamäärä")
            print("6) Potenssi")
            print("0) Lopeta")
            
        elif luku_a < luku_b:
            erotus = luku_b - luku_a
            print(f"Erotus {luku_b} - {luku_a} = {erotus}")
            print("Tämä laskin osaa seuraavat toiminnot:")
            print("1) Anna luvut")
            print("2) Summa")
            print("3) Erotus")
            print("4) Tulo")
            print("5) Osamäärä")
            print("6) Potenssi")
            print("0) Lopeta")
        elif luku_a == luku_b:
            print("Erotus on 0")
            print("Tämä laskin osaa seuraavat toiminnot:")
            print("1) Anna luvut")
            print("2) Summa")
            print("3) Erotus")
            print("4) Tulo")
            print("5) Osamäärä")
            print("6) Potenssi")
            print("0) Lopeta")
            
    elif toiminnot == 4:
        tulo = luku_a * luku_b
        print(f"Tulo {luku_a} * {luku_b} = {tulo}")
        print("Tämä laskin osaa seuraavat toiminnot:")
        print("1) Anna luvut")
        print("2) Summa")
        print("3) Erotus")
        print("4) Tulo")
        print("5) Osamäärä")
        print("6) Potenssi")
        print("0) Lopeta")
        
    elif toiminnot == 5:
        if luku_a == 0 or luku_b == 0:
            print("Nollalla ei voi jakaa.")
            print("Tämä laskin osaa seuraavat toiminnot:")
            print("1) Anna luvut")
            print("2) Summa")
            print("3) Erotus")
            print("4) Tulo")
            print("5) Osamäärä")
            print("6) Potenssi")
            print("0) Lopeta")
            
        else:
            osa = float(luku_a / luku_b)
            osamaara = round(osa, 2)
            print(f"Osamäärä {luku_a} / {luku_b} = {osamaara}")
            print("Tämä laskin osaa seuraavat toiminnot:")
            print("1) Anna luvut")
            print("2) Summa")
            print("3) Erotus")
            print("4) Tulo")
            print("5) Osamäärä")
            print("6) Potenssi")
            print("0) Lopeta")

    elif toiminnot == 6:
        potenssi = luku_a ** luku_b
        print(f"Potenssi {luku_a} ** {luku_b} = {potenssi}")
        print("Tämä laskin osaa seuraavat toiminnot:")
        print("1) Anna luvut")
        print("2) Summa")
        print("3) Erotus")
        print("4) Tulo")
        print("5) Osamäärä")
        print("6) Potenssi")
        print("0) Lopeta")

    elif toiminnot == 0:
        print("Lopetetaan")
        break

    else:
        print("Tuntematon valinta, yritä uudestaan.")
        print("Tämä laskin osaa seuraavat toiminnot:")
        print("1) Anna luvut")
        print("2) Summa")
        print("3) Erotus")
        print("4) Tulo")
        print("5) Osamäärä")
        print("6) Potenssi")
        print("0) Lopeta")

print(kiitos)

