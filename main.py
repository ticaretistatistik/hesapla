# Veri Yapıları
okul = "İstanbul Ticaret Üniversitesi"
kurulus_yili = 2001
vakif_universitesi = True

# Listeler
dersler = []

dersler.append("Merhaba")
dersler.append("dünya")
dersler.append("!")

print(dersler)

ders1 = {
    "Merhaba": "dünya",
    "Dünya": 76
}

print(ders1["Merhaba"])

ders2 = {}
dersler = [ders1, ders2]

print(dersler)

for ders in dersler:
    print(ders)

    pass


dersler = []

dersler.append({
    "Ad": "Olasılık 1",
    "Vize": 60,
    "Final": 80,
    "Quizler": [],
    "Odevler": [],
    "Agirliklar": [0.4, 0.6, [], []]
})

dersler.append({
    "Ad": "İstatistik 1",
    "Vize": 40,
    "Final": 90,
    "Quizler": [100],
    "Odevler": [100],
    "Agirliklar": [0.2, 0.5, [0.2], [0.1]]
})

dersler.append({
    "Ad": "Doğrusal Programlama 1",
    "Vize": 30,
    "Final": 100,
    "Quizler": [],
    "Odevler": [],
    "Agirliklar": [0.4, 0.6, [], []]
})

dersler.append({
    "Ad": "Matematik 1",
    "Vize": 60,
    "Final": 80,
    "Quizler": [],
    "Odevler": [],
    "Agirliklar": [0.4, 0.6, [], []]
})

print(dersler)


donem_ortalamasi = 0

for ders in dersler:
    vize = ders["Vize"]
    if 0 > vize or vize > 100:
        print("Vize 0 dan küçük veya 100 den büyük olduğu için geçersizdir.")
        pass

    final = ders["Final"]
    if 0 > final or final > 100:
        print("Final 0 dan küçük veya 100 den büyük olduğu için geçersizdir.")
        pass
    
    quizler = ders["Quizler"]
    odevler = ders["Odevler"]
    
    agirliklar = ders["Agirliklar"]
    vize_agirlik = agirliklar[0]
    final_agirlik = agirliklar[1]
    quiz_agirlik = agirliklar[2]
    odevler_agirlik = agirliklar[3]

    ortalama = 0

    ortalama += vize * vize_agirlik
    ortalama += final * final_agirlik

    if len(quizler) > 0:
        quiz_ortalama = 0
        for i in range(len(quizler)):
            quiz_ortalama += quizler[i] * quiz_agirlik[i]
            pass

        ortalama += quiz_ortalama
        pass

    if len(odevler) > 0:
        odev_ortalama = 0
        for i in range(len(odevler)):
            odev_ortalama += odevler[i] * odevler_agirlik[i]
            pass
        ortalama += odev_ortalama
        pass

    print(f"{ders['Ad']} ortalaması: {ortalama}")
    donem_ortalamasi += ortalama

    pass

print(f"Ortalama {donem_ortalamasi / len(dersler)}")