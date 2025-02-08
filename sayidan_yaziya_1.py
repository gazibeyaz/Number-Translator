sayi_isimleri_birler_basamagi_1 = {

"1": "bir",
"2": "iki",
"3": "üç",
"4": "dört",
"5": "beş",
"6": "altı",
"7": "yedi",
"8": "sekiz",
"9": "dokuz"

}

sayi_isimleri_onlar_basamagi_1 = {

"1": "on",
"2": "yirmi",
"3": "otuz",
"4": "kırk",
"5": "elli",
"6": "altmış",
"7": "yetmiş",
"8": "seksen",
"9": "doksan"

}

sayi_isimleri_yuzler_basamagi_1 = {

"1": "yüz",
"2": "iki yüz",
"3": "üç yüz",
"4": "dört yüz",
"5": "beş yüz",
"6": "altı yüz",
"7": "yedi yüz",
"8": "sekiz yüz",
"9": "dokuz yüz"

}

basamak_ayirici_isimleri_1 =["bin", "milyon", "milyar", "trilyon", "katrilyon", "kentilyon",
                             "sekstilyon", "septilyon", "oktilyon", "nonilyon", "desilyon",
                             "undesilyon", "dodesilyon", "tredesilyon",
                             "katordesilyon", "kendesilyon", "septendesilyon",
                             "oktesilyon", "novemdesilyon", "vigintilyon",
                             "sentilyon", ""
                             ]

sira_listesi_1 = [sayi_isimleri_yuzler_basamagi_1,
                  sayi_isimleri_onlar_basamagi_1,
                  sayi_isimleri_birler_basamagi_1]


def islem_1():

    global sayi_isimleri_birler_basamagi_1
    global sayi_isimleri_onlar_basamagi_1
    global sayi_isimleri_yuzler_basamagi_1
 
    global basamak_ayirici_isimleri_1

    global sira_listesi_1

    global arka_plan_gosterici_1
    
    giris_1 = input("Sayıyı girin: ")

    if arka_plan_gosterici_1 == True:

        print()
        print(giris_1)
        print()

    liste2 = []

    for i in giris_1:
        liste2.append(i)

    if arka_plan_gosterici_1 == True:
        print(liste2)

    liste2.reverse()
    
    if arka_plan_gosterici_1 == True:
        print(liste2)

    liste3 = []

    degisken_1 = 0

    for i in liste2:

        degisken_1 += 1

        liste3.append(i)

        if degisken_1 == 3:
            
            liste3.append("")

            degisken_1 = 0

    if liste3[-1] != "":
        
        liste3.append("")

    if arka_plan_gosterici_1 == True:
        print(liste3)

    liste4 = []

    bos_liste_1 = []

    for i in liste3:

        if i != "":
            bos_liste_1.append(i)

        else:

            liste4.append(bos_liste_1[:])

            bos_liste_1.clear()

    if arka_plan_gosterici_1 == True:
        print(liste4)

    liste4.reverse()

    for i in liste4:

        i.reverse()

    if arka_plan_gosterici_1 == True:
        print(liste4)

    if len(liste4[0]) < 3:

        liste4[0].reverse()

        for i in range(3 - len(liste4[0])):

            liste4[0].append("")

        liste4[0].reverse()

    if arka_plan_gosterici_1 == True:
        print(liste4)

    liste5 = liste4[:]

    for i in range(0, len(liste5)):

        for a in range(0, len(liste5[i])):

            if liste5[i][a] != "":

                if liste5[i][a] == "0":
                    
                    liste5[i][a] = ""

                else:
                    
                    liste5[i][a] = sira_listesi_1[a][ liste5[i][a] ]             

    if arka_plan_gosterici_1 == True:
        print(liste5)

    liste5.reverse()

    if arka_plan_gosterici_1 == True:
        print(liste5)

    liste6 = []

    degisken_2 = -1

    for i in liste5:

        degisken_2 += 1

        liste6.append(i)

        liste6.append([basamak_ayirici_isimleri_1[degisken_2]])

    liste6 = liste6[:-1]

    if arka_plan_gosterici_1 == True:
        print(liste6)

    liste6.reverse()

    if arka_plan_gosterici_1 == True:
        print(liste6)

    liste6_2 = []

    for i in range(0, len(liste6)):

        if i % 2 != 1:

            liste6_2.append(liste6[i])

        else:

            if liste6[i-1] != ["", "", ""]:
                liste6_2.append(liste6[i])

    liste6 = liste6_2[:]

    if arka_plan_gosterici_1 == True:
        print(liste6)

    liste7 = []

    for i in liste6:

        for a in i:

            if a != "":

                liste7.append(a)

    if arka_plan_gosterici_1 == True:
        print(liste7)

    son_durum_1 = ""

    for i in liste7:

        son_durum_1 += i
        son_durum_1 += " "

    son_durum_1 = son_durum_1[:-1]

    if "bir bin" in son_durum_1:

        if len(giris_1) == 4:

            if arka_plan_gosterici_1 == True:
            
                print()
                print("'bir bin' saptandı")
                print()

                print(liste7)

            liste7 = liste7[1:]
            
            son_durum_1 = ""

            for i in liste7:

                son_durum_1 += i
                son_durum_1 += " "

            son_durum_1 = son_durum_1[:-1]

            if arka_plan_gosterici_1 == True:
                print(liste7)

    print()
    print(son_durum_1)
    print()


while True:

    try:
        
        arka_plan_gosterici_1 = False
        islem_1()

    except:
        pass
