arvosanat = []

while True:
    arvosana = int(input("Anna kurssiarvosana väliltä 1-5 (-1 lopettaa): "))
    
    if (arvosana == -1):
        if len(arvosanat) > 0:
            keskiarvo = sum(arvosanat) / len(arvosanat)
            formatted_keskiarvo = round(keskiarvo, 2)
            print(f"Arvosanojen keskiarvo on {formatted_keskiarvo}.")
        else:
            print("Yhtään arvosanaa ei syötetty.")
        
        break
    
    if (1 <= arvosana <= 5):
        arvosanat.append(arvosana)
        
    else:
        print("Väärä syöte. Vain arvosanat 1-5 kelpaavat (-1 lopettaa).")
        

print("Kiitos ohjelman käytöstä.")
