# Engeto_projekt_3
Election scraper – program pro scrapovaní dat z webu


Popis projektu:

Úkolem bylo vytvořit scraper výsledků voleb z roku 2017, který vytáhne data přímo z webu: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

Skript má za úkol scrapovat výsledky voleb pro jakýkoliv územní celek, který si uživatel zvolí. Volbu územního celku provede uživatel v rámci výše uvedeného webu pomocí "X" ve sloupci výběr obce. Program následně pracuje s daným odkazem. Např. "X" u územního celku Hodonín odkazuje na web: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=6205

Výstupem je csv ve tvaru "soubor.csv", přičemž každý řádek obsahuje informace pro konkrétní obec. Tedy podobu:

-	Kód obce
-	Název obce
-	Voliči v seznamu
-	Vydané obálky
-	Platné hlasy
-	Kandidující strany a počty jejich hlasů


Výsledný soubor se spouští pomocí 2 argumentů:

První argument obsahuje odkaz, který územní celek chcete scrapovat (např. při zvolené obci Hodonín je argument:"https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6205"). 
Druhým argumentem je jméno výstupního souboru (např. vysledek_Hodonin.csv). 
Mezi argumenty nezapomeňte přidat mezeru.


Instalace knihoven:

Pro funkčnost kódu je nutné si nainstalovat použité knihovny. Ty jsou dostupné v rámci souboru "requirements.txt", který je dostupný v repozitáři. 

Příklad spuštění skriptu:

Pro spuštění skriptu a stažení souboru (na uvedeném příkladě pro územní celek Hodonín) zadáme příkaz:

python election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6205" vysledky_Hodonin.csv

Pokud uživatel nezadá argumenty nebo zadá jejich nesprávný počet, je upozorněn a program končí.


Průběh stahování:

% python election_scraper.py "python election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6205" vysledky_Hodonin.csv Zpracovavam pozadavek...Proces muze trvat i nekolik minut. Vydrzte prosim.


Ukázka výstupu :

Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Občanská demokratická…
586030,Archlebov,752,416,415,25,0,0,47,1,12,49,9,2,3,1,1,39,1,10,89,0,0,73,0,3,1,0,46,3,0
586048,Blatnice pod Svatým Antonínkem,1733,1066,1055,101,1,1,70,4,50,61,7,9,42,0,2,74…
586056,Blatnička,356,239,238,16,0,0,14,0,10,17,3,0,1,0,0,23,0,4,58,0,5,42,0,0,0,2,43,0,0
