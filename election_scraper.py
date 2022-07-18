"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Jan Haviernik
email: haviernikjan@gmail.com
"""
import sys
import csv
import requests
from bs4 import BeautifulSoup as bs

# pomocne promenne
kody_obci = list()
jmena_obci = list()
jmena_vsech_obci = list()
nazvy_stran = list()

def test_parametru() -> tuple[str, str]:
    """
    Funkce nacte argumenty z terminalu a provede jejich kontrolu.
    """
    parametry = sys.argv
    if len(parametry) != 3:
        print("Chybi 2 povinne argumenty -> Ukoncuji beh programu")
    elif "https://volby.cz/pls/ps2017nss/" not in parametry[1]:
            print("Chybi argument: odkaz na webove stranky")

    elif ".csv" not in parametry[2]:
            print("Chybi argument: jmeno vystupniho souboru")
    else:
        return parametry[1],parametry[2]

def info_uzemni_celky(odkaz) -> None:
    """
    Funkce sesbira informace vsech nazvu a kodu obci z daneho uzemniho celku.
    """
    odpoved = requests.get(odkaz)
    soup = bs(odpoved.content, features="html.parser")
    obce = soup.find_all(class_="cislo")
    nazvy_obci = soup.find_all(class_="overflow_name")
    for hodnota in obce:
        informace_z_uzemnich_celku = list()
        kod_obce = hodnota.getText()
        default_odkaz = "https://volby.cz/pls/ps2017nss/"
        odkaz_obce = default_odkaz + hodnota.find("a").get("href")
        informace_z_uzemnich_celku.append(kod_obce)
        informace_z_uzemnich_celku.append(odkaz_obce)
        kody_obci.append(informace_z_uzemnich_celku)

    for hodnota in nazvy_obci:
       jmeno_obce = hodnota.getText()
       jmena_obci.append(jmeno_obce)

def info_strany(odkaz) -> None:
    """
    Funkce sesbira informace o nazvech stran pro kazdou obec
    ze zvoleneho okrsku
    """
    odpoved = requests.get(odkaz)
    soup = bs(odpoved.content, features="html.parser")
    strany = soup.find_all(class_="overflow_name")
    for nazev_strany in strany:
        nazvy_stran.append(nazev_strany.getText())

def kolekce_informaci(odkaz) -> list[int]:
    """
    Funkce sesbira vsechny informace pro kazdou obec ze zvoleneho
    okrsku a vrati list.
    """
    sber = list()

    odpoved = requests.get(odkaz)
    soup = bs(odpoved.content, features="html.parser")

    volici = soup.find(class_="cislo", headers="sa2").getText()
    sber.append(int(volici.replace(u'\xa0', '')))
    obalky = soup.find(class_="cislo", headers="sa3").getText()
    sber.append(int(obalky.replace(u"\xa0","")))

    hlasy = soup.find(class_="cislo", headers="sa6").getText()
    sber.append(int(hlasy.replace(u"\xa0","")))

    for rozsah in range(1,4):
        try:
            strany_pocty =  soup.find_all(
                class_="cislo",
                headers=f"t{rozsah}sa2 t{rozsah}sb3"
                )
            for pocet in strany_pocty:
                cislo = pocet.getText()
                sber.append(int(cislo.replace(u"\xa0","")))
        except:
            pass
    return sber

def stazeni_a_zpracovani_dat() -> None:
    """
    Funkce realizujici prubeh stazeni a zpracovani dat z webovych stranek.
    """
    print(
          "Zpracovavam pozadavek...Proces muze trvat i nekolik minut. "
          "Vydrzte prosim."
    )
    obce_data_list = list()
    info_strany(kody_obci[1][1])
    for i in range(0,len(kody_obci)):
        obce_data_list.extend(kody_obci[i])
        obce_data_list.pop(1)

        podrobnosti = kolekce_informaci(kody_obci[i][1])
        obce_data_list.append(jmena_obci[i])
        obce_data_list.extend(podrobnosti)
        jmena_vsech_obci.append(obce_data_list)
        obce_data_list = list()

def ulozeni_dat_do_csv(soubor) -> None:
    """
    Funkce pro ulozeni stazenych dat do noveho csv souboru.
    """
    zahlavi = [
               "Kód obce",
               "Název obce",
               "Voliči v seznamu",
               "Vydané obálky",
               "Platné hlasy"
    ]
    list_1 = list()
    list_1.extend(zahlavi)
    list_1.extend(nazvy_stran)
    print(f"Data ulozena do csv_souboru s nazvem {soubor}.")
    with open(soubor, mode="w", newline='', encoding='utf-8') as csv_soubor:
        zapis = csv.writer(csv_soubor)
        zapis.writerow(list_1)
        zapis.writerows(jmena_vsech_obci)
    print("Operace probehla uspesne. Ukoncuji program.")

def main() -> None:
    """
    Funkce zajistujici beh celeho programu.
    """
    odkaz, soubor = test_parametru()
    info_uzemni_celky(odkaz)
    stazeni_a_zpracovani_dat()
    ulozeni_dat_do_csv(soubor)

if __name__ == "__main__":
    main()