def tiedostoLue(tiedoston_nimi):
    try:
        with open(tiedoston_nimi, "r", encoding="utf-8") as tiedosto:
            name_lines = tiedosto.readlines()

        count_names = len(name_lines)
        count_letters = sum(len(name_line.strip()) for name_line in name_lines)

        if count_names > 0:
            average_letters = round(count_letters / count_names)
        else:
            average_letters = 0

        return count_names, count_letters, average_letters
            
    except FileNotFoundError:
        print(f"Tiedostosta '{tiedoston_nimi}' ei löydy. Varmista, että tiedosto on luotu.")
        return None, None, None
    
def main():
    tiedoston_nimi = input("Anna luettavan tiedoston nimi: ").strip()
            
    count_names, count_letters, average_letters = tiedostoLue(tiedoston_nimi)

    if count_names is not None:
        print(f"Tiedostossa oli {count_names} nimeä ja {count_letters} merkkiä.")
        print(f"Keskimääräinen nimen pituus oli {average_letters} merkkiä.")
    
    print("Kiitos ohjelman käytöstä.")

main()
