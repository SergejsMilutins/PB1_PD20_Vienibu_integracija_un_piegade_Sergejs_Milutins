# Praktiskā darba atskaite

---

## 1. Vispārīgā informācija

- Vārds, Uzvārds: Sergejs Miļutins
- Grupa: 76055
- Praktiskā darba kods: PB1_PD19 Docker pamati

- Datums: 28.07.2026.g.

# Praktiskā darba atskaite

## 2. Darba mērķis

nostiprināt izpratni par Docker kā reproducējamu izpildes vidi;
iemācīties izveidot Dockerfile;
izveidot un palaist Docker image;
saprast atšķirību starp image un container;
sasaistīt Docker izmantošanu ar CI un profesionālu piegādes procesu.

---

## 3. Izmantotā vide un rīki

- Operētājsistēma: Windows 10
- Programmas / rīki: VsCode, powershell, ubuntu;
- Versijas (ja nepieciešams): python 3.x;
- Papildu bibliotēkas / servisi (ja attiecas): moodle;

---

## 4. Uzdevumu izpilde

Apraksti katra uzdevuma izpildi atsevišķā apakšsadaļā.

---

### 4.1. Uzdevums 1

darba direktorijas izveide;
requirements.txt kopēšana;
bibliotēku instalēšana;
projekta failu kopēšana;
galvenās programmas palaišana.

---

### 4.2. Uzdevums 2

Uzdevums:
Izveido .dockerignore failu, lai image neiekļautu liekus failus.
Iekļauj vismaz:
__pycache__/
venv/
.git/
---

### 4.3. Uzdevums 3

Uzdevums:
Ar komandu:

docker build -t pb1-kalkulators .

uzbūvē Docker image.

---
### 4.4. Uzdevums 4

Uzdevums:
Palaid konteineru ar komandu:
docker run pb1-kalkulators
Ja nepieciešams, izmanto --rm .

### 4.5. Uzdevums 5

1. Palaid konteineru.
2. Pārbaudi darbojošos konteinerus ar docker ps .
3. Apturi konteineru ar docker stop .

### 4.6. Uzdevums 6

Uzdevums:
Pielāgo Dockerfile vai palaišanas komandu tā, 
lai konteinerā tiktu palaisti projekta testi.

## 5. Problēmas un to risinājumi

Apraksti vismaz vienu problēmu, ar kuru saskāries darba laikā:

- Problēmas apraksts: /requirements.txt/ failā biju ierakstijis - "tukšs", dēļ tā izmeta kļūdu, jo programma grib 
instalēt bibliotēkas kuras apgalvotas failā /requirements.txt/, tur rakstīts "tukšs", ar šādu nosaukumu biblieotēkas nav - met kļūdu. 
- Kļūdas ziņojums (ja bija): /pielikumi/1_ar_kludu.png
- Risinājums: Izdēst šo ierakstu no faila /requirements.txt/, un atstāt failu tukšu. 

---


## 6. Pašvērtējums

Novērtē savu darbu atbilstoši šī praktiskā darba vērtēšanas kritērijiem.


Kopā punkti: 60 / 100

Pamatojums (ja nepieciešams): Ne viss uzreiz ir saprotams, bet uzdevums izpildīs.
Šis uzdevums trenē arī darbības ar /powershell/.

---

## 8. Pielikumi

Norādi pievienotos failus vai ekrānšāviņus:
Mape:
/PB1_PD19_Docker_pamati_Sergejs_Milutins/

/pielikumi/1_ar_kludu.png
/pielikumi/2_izlabota_kluda_empty.png
/pielikumi/3_viss_izpildits.png
/pielikumi/4_6_uzdevums_izpildits.png
/projekts/.dockerignore
/projekts/Dockerfile
/projekts/kalkulators.py
/projekts/requierements.txt
/PB1_PD19_Docker_pamati_Sergejs_Milutins.md/
