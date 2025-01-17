luku_a = int(input("Anna alueen alaraja: "))
luku_b = int(input("Anna alueen yläraja: "))

for i in range (luku_a, luku_b+1):
    if ((i % 5) == 0) and ((i % 7) == 0):
        print(f"Luku {i} on jaollinen 5:llä ja 7:llä.")
        print("Lopetetaan etsintä.")
        break
    elif ((i % 5) == 0 and ((i % 7) != 0)):
        print(f"{i} ei ole jaollinen seitsemällä, hylätään.")
        continue
    else:
        print(f"{i} ei ole jaollinen viidellä, hylätään.")
        continue
if ((i % 5) != 5) and ((i % 7) != 0):
    print("Alueelta ei löytynyt sopivaa arvoa.")
        
print("Kiitos ohjelman käytöstä.")
