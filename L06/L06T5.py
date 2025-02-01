def tulostaOhjeet():
    print("Tämä laskin osaa seuraavat toiminnot:")
    print("1) Anna luvut")
    print("2) Summa")
    print("3) Osamäärä")
    print("0) Lopeta")
    return int(input("Valitse toiminto (0-3): "))

def readTextFile(file_name):
    try:
        with open(file_name, "r", encoding = "utf-8") as read_only_file:
            given_numbers = [line.strip() for line in read_only_file]
        return given_numbers

    except FileNotFoundError:
        print(f"Tiedostosta '{file_name}' ei löydy. Varmista että tiedosto on luotu.")
        return []

def isThereNumbers(given_numbers):
    return len(given_numbers) >=2

def getNumbers(given_numbers):
    if len(given_numbers) < 2:
        return None, None
    try:
        return int(given_numbers.pop(0)), int(given_numbers.pop(0))
    except ValueError:
        return None, None

def summa(luku1, luku2):
    tulos = luku1 + luku2
    print("Tulos tallennettu tiedostoon.")
    return tulos

def osaMaara(luku1, luku2):
    if luku1 == 0 or luku2 == 0:
        print("Nollalla ei voi jakaa.")
        return None
                
    else:
        tulos = round(luku1 / luku2, 2)
        print("Tulos tallennettu tiedostoon.")
        return tulos

def saveResults(luku1, luku2, summa_tulos, osaMaara_tulos, file_to_save):
    try:
        with open(file_to_save, "a", encoding = "utf-8") as save_file:
            if summa_tulos is not None:
                save_file.write(f"Summa {luku1} + {luku2} = {summa_tulos}\n")
            if osaMaara_tulos is not None:
                save_file.write(f"Osamäärä {luku1} / {luku2} = {osaMaara_tulos}\n")

    except FileNotFoundError:
        print(f"Tiedostosta '{file_to_save}' ei löydy.")

def main():
    file_name = input("Anna luettavan tiedoston nimi: ").strip()
    given_numbers = readTextFile(file_name)

    file_to_save = "L06T5T1.txt"
    luku1, luku2 = None, None
    
    while True:
        toiminta = tulostaOhjeet()
            
        if toiminta == 0:
            print("Lopetetaan")
            break

        elif toiminta == 1:
            if isThereNumbers(given_numbers):
                luku1, luku2 = getNumbers(given_numbers)
                print(f"Luettiin luvut {luku1} ja {luku2}")
                    
            else:
                print(f"Luvut loppuivat, lopeta ohjelma.")
                
                luku1, luku2 = 0, 0
                print(f"Luvut loppuivat, lopeta ohjelma.")
                print(f"Luettiin luvut {luku1} ja {luku2}")  
                
        elif toiminta == 2:
            if luku1 is None or luku2 is None:
                print("Et ole vielä antanut lukuja.")
            else:
                summa_tulos = summa(luku1, luku2)
                saveResults(luku1, luku2, summa_tulos, None, file_to_save)

        elif toiminta == 3:
            if luku1 is None or luku2 is None:
                print("Et ole vielä antanut lukuja.")
            else:
                osaMaara_tulos = osaMaara(luku1, luku2)
                saveResults(luku1, luku2, None, osaMaara_tulos, file_to_save)

        else:
            print("Virheellinen valinta, yritä uudestaan.")

             
    print("Kiitos ohjelman käytöstä.")

main()
