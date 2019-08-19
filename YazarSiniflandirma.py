import os
import math

def metni_Temizle(liste):
    n = len(liste)
    for i in range(0, n):
        liste[i] = liste[i].lower()
        if (liste[i] == "."):
            liste[i] = ""
        elif (liste[i] == ","):
            liste[i] = ""
        elif (liste[i] == "and"):
            liste[i] = ""
        elif (liste[i] == "or"):
            liste[i] = ""
        elif (liste[i] == "a"):
            liste[i] = ""
        elif (liste[i] == "an"):
            liste[i] = ""
        elif (liste[i] == "the"):
            liste[i] = ""
        elif (liste[i] == "on"):
            liste[i] = ""
        elif (liste[i] == "\n"):
            liste[i] = " "
        elif (liste[i] == "?"):
            liste[i] = ""
        elif (liste[i] == "!"):
            liste[i] = ""
        elif (liste[i] == "'"):
            liste[i] = ""
        elif (liste[i] == "\'"):
            liste[i] = ""
        elif (liste[i] == "-"):
            liste[i] = ""
        elif (liste[i] == "_"):
            liste[i] = ""
        elif (liste[i] == ":"):
            liste[i] = ""
        elif (liste[i] == "="):
            liste[i] = ""
        elif (liste[i] == "(", ")"):
            liste[i] == " "
    metin = "".join(liste)
    return metin

def kelimelere_Ayir(metin):
    liste = list(metin)
    n = len(liste)
    n = int(n)
    kelime = ""
    a = ""
    kelimeler = []
    i = 0
    i = int(i)
    while i != n:

        if liste[i] != " ":
            while liste[i] != " ":
                kelime += liste[i]
                i += 1
            kelimeler.append(kelime)
            kelime = a
        else:
            i += 1
    return kelimeler

def yakinlikHesapla(metin1,metin2):
    # METİN1 Sahibi aranan, METİN2 Sahibi Bilinen olmak zorunda !!!
    n1 = len(metin1)
    n2 = len(metin2)
    frekans1 = []
    frekans12 = []
    olasiliklar = []
    for k in range(0,n1):
        frekans1.append(1) # FREKANS LİSTESİ İÇİN
        frekans12.append(1) # BU DA BİRİNCİ  METNİN İKİNCİ METİNDEKİ FREKANSI
                            # (ÇARPMADA SORUN OLMAMASI İÇİN HEPSİNE 1 EKLEDİK)

    i = 0
    while i != n1:
        j = i + 1
        while j != n1:
            if metin1[i] == metin1[j]:
                    frekans1[i] += 1
                    metin1.pop(j)
                    frekans1.pop(j)
                    frekans12.pop(j) #SENSİN SPAGETTI KOD ! :D
                    n1 -= 1
            else:
                j += 1
        i += 1

    for r in range(0,n1):
        for l in range(0,n2):
            if metin1[r] == metin2[l]:
                frekans12[r] += 1

    for p in range(0,n1):
        gecici = (frekans12[p] / n2) * frekans1[p]
        olasiliklar.append(gecici)
    yakinlik = 1.0
    n = len(olasiliklar)
    for m in range(0,n):
        yakinlik *= olasiliklar[m]
        yakinlik = yakinlik * 1000


    return yakinlik


birinci_kitap = open("The Little Mermaid.txt","r")
kalip1 = birinci_kitap.read()
liste1 = list(kalip1)
metin1 = metni_Temizle(liste1)
kelimeler1 = kelimelere_Ayir(metin1)

ikinci_kitap = open("The Magic Tinderbox.txt","r")
kalip2 = ikinci_kitap.read()
liste2 = list(kalip2)
metin2 = metni_Temizle(liste2)
kelimeler2 = kelimelere_Ayir(metin2)

ucuncu_kitap = open("The Golden Goose.txt","r")
kalip3 = ucuncu_kitap.read()
liste3 = list(kalip3)
metin3 = metni_Temizle(liste3)
kelimeler3 = kelimelere_Ayir(metin3)

Bayes12 = yakinlikHesapla(kelimeler1,kelimeler2)
Bayes13 = yakinlikHesapla(kelimeler1,kelimeler3)

print(Bayes12)
print(Bayes13)

if Bayes12 > Bayes13:
    print("The Little Mermaid, The Magic Tinderbox'a Daha Yakındır. Yani, Anderson'a ait olma ihtimali fazladır.")
elif Bayes13 > Bayes12:
    print("The Little Mermaid, The Golden Goose'a Daha Yakındır. Yani, Grim Kardeşler'e ait olma ihtimali fazladır.")
else:
    print("İki Kitaba da eşit yakınlıktadır.")