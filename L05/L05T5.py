def tulostaOhjeet():
    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut")
    print("2) Summa")
    print("3) Osamäärä")
    print("0) Lopeta")
    return int(input("Valitse toiminto (0-3): "))

def kysyLuvut(ohje):
    return int(input(ohje))

def summa(luku1, luku2):
    summa = luku1 + luku2
    print(f"Summa {luku1} + {luku2} = {summa}")

def osaMaara(luku1, luku2):
    if luku1 == 0 or luku2 == 0:
        print("Nollalla ei voi jakaa.")
                
    else:
        tulos = round(luku1 / luku2, 2)
        print(f"Osamäärä {luku1} / {luku2} = {tulos}")

def main():
    while True:
        toiminta = tulostaOhjeet()
            
        if toiminta == 0:
            print("Lopetetaan")
            break

        elif toiminta == 1:
            luku1 = kysyLuvut("Anna ensimmäinen luku: ")
            luku2 = kysyLuvut("Anna toinen luku: ")
            print(f"Annoit luvut {luku1} ja {luku2}")
                
        elif toiminta == 2:
            if luku1 is None or luku2 is None:
                print("Et ole vielä antanut lukuja.")
            else:
                summa(luku1, luku2)

        elif toiminta == 3:
            if luku1 is None or luku2 is None:
                print("Et ole vielä antanut lukuja.")
            else:
                osaMaara(luku1, luku2)

        else:
            print("Virheellinen valinta, yritä uudestaan.")
                
    print("Kiitos ohjelman käytöstä.")

main()
