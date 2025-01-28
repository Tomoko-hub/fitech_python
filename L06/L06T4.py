def readTextFile(file_name):
    try:
        with open(file_name, "r", encoding = "utf-8") as read_only_file:
            #steps = read_only_file.readlines()
            steps = [step.strip() for step in read_only_file]
        return steps
    
    except FileNotFoundError:
        print(f"Tiedostosta '{file_name}' ei löydy. Valmista että tiedosto on luotu.")
        return None
    
def getSmallestAndLargest(steps):
    smallest = min(steps, key=int) #key=intにすることで整数としてあつかう
    largest = max(steps, key=int)  #key=intがないと文字列になってしまう
    return smallest, largest

def calculateTotal(steps):
    total = sum(int(step) for step in steps)
    return total

# save = write
def saveResults(steps, smallest, largest, total, give_file_name):
    try:
        with open(give_file_name, "w", encoding = "utf-8") as save_file:
            count_lines = len(steps)
            
            save_file.write(f"Pienin askelmäärä oli {smallest} askelta.\n")
            save_file.write(f"Suurin askelmäärä oli {largest} askelta.\n")
            save_file.write(f"Yhteensä askelia oli {total} askelta.\n")

    except FileNotFoundError:
        print(f"Tiedostoa '{give_file_name}' ei löydy. Varmista, että tiedosto on luotu.")

def main():
    file_name = input("Anna tiedot sisältävän tiedoston nimi: ").strip()
    steps = readTextFile(file_name)

    if steps == 0:
        return print("Päivä pitää olla enemmän kuin kaksi.")

    smallest, largest = getSmallestAndLargest(steps)
    
    total = calculateTotal(steps)
    
    give_file_name = input("Anna tallennettavan tiedoston nimi: ").strip()
    saveResults(steps, smallest, largest, total, give_file_name)

    print(f"Pienin askelmäärä oli {smallest} askelta.")
    print(f"Suurin askelmäärä oli {largest} askelta.")
    print(f"Yhteensä askelia oli {total} askelta.")
    
    print("Kiitos ohjelman käytöstä.")

main()
