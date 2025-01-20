MIN_LENGTH = 5
MAX_LENGTH = 15

def kysyMerkkijono():
    return input("Anna merkkijono, 5-15 merkkiä: ")

def tarkistaTekstiLength(teksti):
    tekstiLength = 0
    for _ in teksti:
        tekstiLength +=1
    return tekstiLength

def main():
    while True:
        teksti = kysyMerkkijono()
        tekstiLength = tarkistaTekstiLength(teksti)
                
        if MIN_LENGTH <= tekstiLength <= MAX_LENGTH:
            print(f"Annoit sopivan merkkijonon, {tekstiLength} merkkiä.")
            break

        elif tekstiLength > MAX_LENGTH:
            print(f"Liian pitkä, {tekstiLength} merkkiä, anna uusi.")
            
        elif tekstiLength < MIN_LENGTH:
            print(f"Liian lyhyt, {tekstiLength} merkkiä, anna uusi.")
            
    print("Kiitos ohjelman käytöstä.")
    
main()
