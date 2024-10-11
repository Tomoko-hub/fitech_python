aloitusarvo = int(input("Anna aloitusarvo: "))
lopetusarvo = int(input("Anna lopetusarvo: "))

print("Toteutus for-lauseella:")

# for-lauseella
for i in range(aloitusarvo, lopetusarvo+1):
    print(i, end=" ")
print()
print()
# while-lauseella
print("Toteutus while-lauseella:")


n = aloitusarvo
while n < lopetusarvo+1:
    print(n, end=" ")
    n += 1
print()
print()
print("Kiitos ohjelman käytöstä.")
