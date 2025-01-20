def tulostaTeksti(teksti, luku):
    for _ in range(luku):
        print(teksti)
    print()
    
def main():
    while True:
        teksti = input("Anna teksti: ")
        if teksti == "lopeta":
            print(f"Lopetetaan.")
            break

        else:
            luku = int(input("Anna luku: "))
            tulostaTeksti(teksti, luku)
            
    print("Kiitos ohjelman käytöstä.")

main()
