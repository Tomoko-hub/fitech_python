# ensimm'inen vaihe aliohjelma
def eka_teksti():
    print("Ensimmäinen vaihe:")
    print("Nyt olemme tulosta-aliohjelmassa")
    print("Tämä aliohjelma tulostaa vain tekstiä.")
    print("Tämä sopii hyvin valikon tulostamiseen.")

# toka vaihe aliohjelma
def laske_luku(luku):
    print(f"Aliohjelmassa parametrin arvo on {luku}")
    luku = luku ** 2
    print(f"Aliohjelmassa parametrin arvo on neliöön korottamisen jälkeen {luku}")
    return luku

# kolmasvaihe aliohjelma
def nimet(etunimi, sukunimi):
    return f"{etunimi} {sukunimi}"
    
# pääohjelma
def main():
    # ensimmäinen vaihe
    eka_teksti()

    # toinen vaihe
    print("")
    print("Toinen vaihe:")
    luku = int(input("Anna luku: "))
    print(f"Päätasolla ennen aliohjelmaa luku on {luku}")
    laske_luku(luku)
    print(f"Päätasolla aliohjelman jälkeen luku on {luku}")

    #kolmas vaihe
    print("")
    print("Kolmas vaihe:")
    etunimi = input("Anna etunimi: ")
    sukunimi = input("Anna sukunimi: ")
    etunimi_sukunimi = nimet(etunimi, sukunimi)
    print(f"Etunimi '{etunimi}' ja sukunimi '{sukunimi}' muodostavat nimen '{etunimi_sukunimi}'.")

    print("Kiitos ohjelman käytöstä.")

main()

##if __name__ == "__main__":
##    main()
