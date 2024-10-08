pituus = float(input("Anna pituus (cm): "))
paino = float(input("Anna paino (kg): "))

pituus_metriksi = pituus / 100

painoindeksi = paino / (pituus_metriksi ** 2)

if painoindeksi <= 17:
    palaute = "Vaarallinen aliravitsemus"
elif 17 < painoindeksi < 18.5:
    palaute = "Liiallinen laihuus"
elif 18.5 <= painoindeksi < 25:
    palaute = "Normaali paino"
elif 25 <= painoindeksi < 30:
    palaute = "Ylipaino eli lievä lihavuus"
elif 30 <= painoindeksi < 35:
    palaute = "Merkittävä lihavuus"
elif 35 <= painoindeksi < 40:
    palaute = "Vaikea lihavuus"
else:
    palaute = "Sairaalloinen lihavuus"

print(f"Painoindeksi on {painoindeksi:.1f} ({palaute})")

tavoiteindeksi = float(input("Anna tavoiteindeksi: "))

tavoitepaino = tavoiteindeksi * (pituus_metriksi ** 2)
painonmuutos = paino - tavoitepaino

if painonmuutos > 0:
    print(f"Tavoiteindeksi vastaa {abs(painonmuutos):.1f} kg alhaisempaa painoa.")
else:
    print(f"Tavoiteindeksi vastaa {abs(painonmuutos):.1f} kg suurempaa painoa.")

print("Kiitos ohjelman käytöstä.")
