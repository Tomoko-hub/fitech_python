sana1 = str(input("Anna sana 1: "))
sana2 = str(input("Anna sana 2: "))

kiitos = str("Kiitos ohjelman käytöstä.")

if (sana1 == sana2):
    print("Sanat ovat samoja.")
elif (sana1 < sana2):
    print(f"'{sana1}' on aakkosissa aiemmin kuin '{sana2}'.")
else:
    print(f"'{sana2}' on aakkosissa aiemmin kuin '{sana1}'.")
    
find_z_sana1 = 'z' in sana1 or 'Z' in sana1
find_z_sana2 = 'z' in sana2 or 'Z' in sana2

if find_z_sana1:
    print(f"Kirjain 'z' löytyy sanasta 1.")
if find_z_sana2:
    print(f"Kirjain 'z' löytyy sanasta 2.")
elif not find_z_sana1 and not find_z_sana2:
    print(f"Kummastakaan sanasta ei löytynyt kirjainta 'z'.")

    
sana3=str(input("Anna testattava sana: "))

if (sana3 == sana3[::-1]):
    print(f"Antamasi sana '{sana3}' on palindromi.")
else:
    print("Antamasi sana ei ole palindromi.")
    print(f"Se on väärinpäin '{sana3[::-1]}' ja oikein päin '{sana3}'.")    

print(kiitos)
