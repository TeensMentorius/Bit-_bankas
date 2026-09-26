# ============================================================
# BANKO KLIENTŲ DUOMENYS
# ============================================================

klientu_id = list(range(1001, 1121))

vardai = [
    "Jonas", "Petras", "Ona", "Ieva", "Mantas",
    "Lukas", "Gabija", "Tomas", "Eglė", "Karolis",
    "Austėja", "Domas", "Monika", "Paulius", "Rūta",
    "Andrius", "Laura", "Simonas", "Greta", "Vytautas",
    "Emilija", "Nojus", "Viltė", "Rokas", "Ugnė",
    "Dominykas", "Kamilė", "Martynas", "Goda", "Arnas",
    "Viktorija", "Benas", "Liepa", "Kajus", "Patricija",
    "Tadas", "Miglė", "Augustas", "Karina", "Erikas",
    "Gabrielius", "Justė", "Danielius", "Kotryna", "Deividas",
    "Agnė", "Linas", "Marija", "Dainius", "Aistė",
    "Rimantas", "Neringa", "Mindaugas", "Simona", "Edvinas",
    "Viktoras", "Julija", "Arnas", "Paulina", "Giedrius",
    "Vakarė", "Saulius", "Indrė", "Marius", "Evelina",
    "Nedas", "Sandra", "Rytis", "Agnė", "Laurynas",
    "Beata", "Algirdas", "Vilma", "Tautvydas", "Karolina",
    "Rokas", "Erika", "Laimonas", "Greta", "Darius",
    "Milda", "Valdas", "Aurelija", "Tomas", "Jolanta",
    "Arvydas", "Kristina", "Lukas", "Dovilė", "Modestas",
    "Renata", "Gediminas", "Vaida", "Šarūnas", "Inga",
    "Dovydas", "Rasa", "Kęstutis", "Lina", "Evaldas",
    "Jurgita", "Almantas", "Violeta", "Ričardas", "Raminta",
    "Aurimas", "Ieva", "Mindaugas", "Sandra", "Raimondas",
    "Eglė", "Vytautas", "Agnė", "Mantas", "Monika",
    "Saulė", "Andrius", "Gabija", "Tadas", "Urtė"
]

pavardes = [
    "Jonaitis", "Petraitis", "Kazlauskaitė", "Jankauskaitė",
    "Petrauskas", "Lukauskas", "Kazlauskas", "Tomauskas",
    "Petraitytė", "Karalius", "Jonaitytė", "Dambrauskas",
    "Jonaitė", "Paulauskas", "Rimkutė", "Andriuškevičius",
    "Laurinaitė", "Simonas", "Grigaitė", "Vytautas",
    "Petronytė", "Kazlauskas", "Vaitkutė", "Rimkus",
    "Žukauskaitė", "Mikalauskas", "Butkutė", "Stankevičius",
    "Pociūtė", "Urbonas", "Brazaitė", "Balčiūnas",
    "Vaitkevičiūtė", "Mačiulis", "Norkutė", "Kavaliauskas",
    "Žilinskaitė", "Navickas", "Jasiūnaitė", "Rakauskas",
    "Mockus", "Vasiliauskaitė", "Ivanauskas", "Kairytė",
    "Daugėla", "Kudirka", "Mickevičiūtė", "Grigonis",
    "Šimkutė", "Rimavičius", "Valaitė", "Bagdonas",
    "Bubnytė", "Stonys", "Žukauskaitė", "Giedraitis",
    "Petkevičienė", "Kriščiūnas", "Vaičiulytė", "Ramonas",
    "Daukšas", "Sakalauskaitė", "Balsys", "Kavaliauskaitė",
    "Liaudanskas", "Tamošiūnaitė", "Venskus", "Jurevičienė",
    "Morkūnas", "Žemaitė", "Sadauskas", "Petravičiūtė",
    "Butkus", "Žukauskas", "Šukytė", "Jankauskas",
    "Rimkevičius", "Stankevičiūtė", "Vaitkus", "Mikalauskaitė",
    "Naujokas", "Kudrevičiūtė", "Kazlauskas", "Barauskas",
    "Vasiliauskaitė", "Kairys", "Dargis", "Šimkutė",
    "Baltrušaitis", "Grigaliūnaitė", "Kavaliauskas", "Pocius",
    "Urbonaitė", "Navickas", "Jasiūnas", "Rakauskaitė",
    "Mockus", "Ivanauskaitė", "Dambrauskas", "Milašiūtė",
    "Kvedaras", "Žilinskaitė", "Norkus", "Mačiulytė",
    "Sakalauskas", "Brazaitis", "Vaičiulis", "Daugėla",
    "Stonaitis", "Giedraitė", "Kriščiūnas", "Vaitkutė"
]

amzius = [
    24, 41, 67, 19, 35,
    52, 28, 44, 31, 73,
    22, 39, 56, 47, 26,
    61, 33, 29, 42, 68,
    37, 21, 54, 46, 32,
    25, 63, 48, 36, 71,
    27, 58, 43, 20, 34,
    66, 45, 30, 52, 23,
    40, 57, 69, 38, 27,
    49, 62, 31, 74, 26,
    55, 44, 36, 68, 29,
    41, 53, 22, 64, 35,
    47, 59, 24, 72, 33,
    28, 51, 43, 19, 60,
    37, 65, 30, 46, 25,
    56, 39, 70, 32, 48,
    27, 61, 45, 34, 73,
    23, 52, 40, 67, 31,
    58, 26, 49, 36, 63,
    44, 21, 55, 38, 69,
    29, 57, 42, 24, 71,
    35, 50, 62, 27, 46,
    33, 68, 41, 30, 54,
    22, 59, 37, 64, 28
]

miestai = [
    "Kaunas", "Vilnius", "Klaipėda", "Šiauliai",
    "Panevėžys", "Alytus", "Marijampolė", "Utena",
    "Telšiai", "Tauragė"
]

klientu_miestai = [
    "Kaunas", "Vilnius", "Klaipėda", "Šiauliai", "Panevėžys",
    "Kaunas", "Vilnius", "Alytus", "Kaunas", "Marijampolė",
    "Klaipėda", "Vilnius", "Utena", "Kaunas", "Šiauliai",
    "Vilnius", "Kaunas", "Telšiai", "Klaipėda", "Panevėžys",
    "Kaunas", "Vilnius", "Marijampolė", "Alytus", "Klaipėda",
    "Šiauliai", "Kaunas", "Vilnius", "Utena", "Kaunas",
    "Panevėžys", "Klaipėda", "Vilnius", "Kaunas", "Telšiai",
    "Marijampolė", "Šiauliai", "Kaunas", "Vilnius", "Alytus",
    "Klaipėda", "Kaunas", "Panevėžys", "Vilnius", "Utena",
    "Kaunas", "Šiauliai", "Marijampolė", "Klaipėda", "Vilnius",
    "Kaunas", "Telšiai", "Alytus", "Panevėžys", "Kaunas",
    "Vilnius", "Klaipėda", "Šiauliai", "Kaunas", "Utena",
    "Marijampolė", "Kaunas", "Vilnius", "Alytus", "Klaipėda",
    "Panevėžys", "Kaunas", "Šiauliai", "Vilnius", "Telšiai",
    "Kaunas", "Marijampolė", "Klaipėda", "Vilnius", "Kaunas",
    "Alytus", "Panevėžys", "Šiauliai", "Kaunas", "Utena",
    "Vilnius", "Klaipėda", "Kaunas", "Marijampolė", "Telšiai",
    "Vilnius", "Kaunas", "Alytus", "Panevėžys", "Šiauliai",
    "Kaunas", "Vilnius", "Klaipėda", "Kaunas", "Utena",
    "Marijampolė", "Vilnius", "Kaunas", "Telšiai", "Alytus",
    "Klaipėda", "Šiauliai", "Kaunas", "Panevėžys", "Vilnius",
    "Kaunas", "Marijampolė", "Klaipėda", "Utena", "Kaunas",
    "Vilnius", "Šiauliai", "Alytus", "Kaunas", "Panevėžys"
]

balansai = [
    1250.50, 340.20, 5820.75, 90.00, 12400.30,
    2750.45, 890.10, 4520.00, 156.70, 7340.25,
    3200.80, 650.40, 11250.00, 4780.65, 920.30,
    15600.50, 2300.00, 540.25, 8760.40, 3210.90,
    450.00, 9850.70, 1740.25, 6200.00, 135.50,
    7830.40, 2950.75, 420.00, 11340.20, 5680.60,
    870.30, 3450.50, 12800.00, 2150.40, 734.90,
    9870.65, 1650.20, 5320.40, 780.00, 14200.50,
    3670.25, 910.80, 6230.75, 4500.00, 1120.30,
    15800.40, 2740.90, 630.20, 8450.65, 3900.00,
    520.40, 10340.70, 2180.25, 7560.00, 480.80,
    9340.50, 1520.30, 6800.75, 275.00, 11900.40,
    3240.60, 870.20, 14650.00, 4150.75, 950.30,
    7820.40, 230.00, 5680.90, 12500.25, 3420.00,
    680.50, 9750.40, 1860.75, 6340.20, 5200.00,
    145.30, 11200.65, 2980.40, 760.00, 8950.20,
    4130.50, 570.25, 13400.75, 2450.00, 7100.30,
    920.60, 10560.40, 1780.25, 4890.70, 15200.00,
    360.50, 8260.40, 2940.75, 6500.20, 1080.00,
    13800.50, 4320.30, 790.65, 9560.40, 2670.00,
    580.20, 12100.75, 3140.40, 7200.00, 450.30,
    10250.60, 1980.25, 5640.70, 830.00, 14700.40,
    3710.50, 690.20, 8840.75, 2530.00, 11600.30,
    420.60, 9340.40, 2860.25, 6750.70, 1280.00
]

# ============================================================
# FUNKCIJOS
# ============================================================

def rasti_klienta(ieskomo_kliento_id):
    pass

def gauti_balansa(kliento_id):
    pass

def gauti_turtingiausia_klienta():
    pass

def gauti_maziausiai_pinigu_turinti_klienta():
    pass

def gauti_bendra_banko_suma():
    pass

def gauti_vidutini_balansa():
    pass

def gauti_vyriausia_klienta():
    pass

def gauti_jauniausia_klienta():
    pass

def atrinkti_turtingus_klientus():
    pass

def atrinkti_klientus_pagal_miesta():
    pass

def gauti_klientus_su_dideliu_balansu():
    #Didelis balansas = balansas > 10000
    print("\n\nKlientai su dideliu balansu: \n")
    for i in range(len(pavardes)):

        if balansai[i] > 10000:
            print(f"{vardai[i]} {pavardes[i]} {balansai[i]}")

def sukurti_nauja_banko_saskaita(
    vardas,
    pavarde,
    kliento_amzius,
    kliento_miestas,
    pradinis_indelis
):
    pass

# ============================================================
# PAGRINDINIS KODAS
# ============================================================

#Funkcijas paleidžiame šioje vietoje

