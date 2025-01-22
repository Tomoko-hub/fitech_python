def tiedostoKirjoita(tiedoston_nimi):
    with open(tiedoston_nimi, 'w') as tiedosto:
        while True:
            nimi = input("Anna tiedostoon tallennettava nimi (0 lopettaa): ")
            if nimi == "0":
                break
            tiedosto.write(nimi + "\n")
    
def tiedostoLue(tiedoston_nimi):
    try:
        with open(tiedoston_nimi, "r") as tiedosto:
            print(f"Tiedostoon '{tiedoston_nimi}' on tallennettu seuraavat nimet:")
            for rivi in tiedosto:
                print(rivi.strip())
    except FileNotFoundError:
        print(f"Tiedostoa '{tiedoston_nimi}' ei löydy. Varmista, että tiedosto on luotu.")
        
def main():
    tiedoston_nimi = input("Anna tallennettavan tiedoston nimi: ")
    tiedostoKirjoita(tiedoston_nimi)
    tiedostoLue(tiedoston_nimi)
    print("Kiitos ohjelman käytöstä.")
    
main()
