a = int(input("Anna a:n arvo: "))
b = int(input("Anna b:n arvo: "))

print(f"a: {a} b: {b}")

while a <=b and a<=10000 and b <= 10000:
    a *= 2
    b += 100

    print(f"a: {a} b: {b}")

print("Kiitos ohjelman käytöstä.")
