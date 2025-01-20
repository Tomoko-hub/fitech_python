# aliohjelma1:tulostaa käyttäjälle ohjelman käyttöohje

def tulostaOhjeet():
    print("Tämä ohjelma etsii antamistasi luvuista pienimmän.")
    print("Ohjelman lopussa se kertoo pienimmän luvun lisäksi antamiesi")
    print("lukujen lukumäärän.")
    print("")

# aliohjelma2:kysy käyttäjälta lukua ja palauttaa kokonaisluku
def kysyLuku(prompt):
    while True:
        luku = int(input(prompt))
        if luku >= 0:
            return luku
        else:
            print("Luku pitää olla positiivinen kokonaisluku.")

# aliohjelma3: vertailla kaksi kokonaislukua selvitä pienimmän ja palauttaa 
def vertaileLukuja(luku1, luku2):
    return min(luku1, luku2)

#aliohjelma4: 
def tulostaTiedot(pienempiLuku, lukuLen):
    if lukuLen == 1:
        print(f"Annoit yhden luvun, jonka oli {pienempiLuku}.")
    else:
        print("")
        print(f"Annoit {lukuLen} lukua.")
        print(f"Annetuista luvuista pienin oli {pienempiLuku}.")
        print("Kiitos ohjelman käytöstä.")

# pääohjelma: kutsuu yllä olevia aliohjelmia
def paaohjelma():
    tulostaOhjeet()

    lukuLen = 0
    
    while True:
         if lukuLen == 0:
             prompt = "Anna positiivinen kokonaisluku: "
         elif lukuLen == 1:
             prompt = "Anna vertailtava positiivinen kokonaisluku (0 lopettaa): "

         else:
             prompt = "Anna uusi positiivinen kokonaisluku (0 lopettaa): "

         luku = kysyLuku(prompt)

         if luku == 0:
             break

         if lukuLen == 0 or luku < pienempiLuku:
             pienempiLuku = luku

         lukuLen += 1

         if lukuLen > 1:
             pienempiLuku = vertaileLukuja(pienempiLuku, luku)
             print(f"Annetuista luvuista pienempi oli {pienempiLuku}.")

    tulostaTiedot(pienempiLuku, lukuLen)
    
paaohjelma ()
