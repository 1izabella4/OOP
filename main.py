from szemelyauto import Szemelyauto
from teherauto import Teherauto
from autokolcsonzo import Autokolcsonzo
from datetime import datetime, timedelta

def elozetes_feltoltes(kolcsonzo):
    # Feltölti az rendszert a meglévő autókkal és bérlésekkel.
    auto1 = Szemelyauto("RA 12-345", "Volkswagen Passat", 19800, 135, "diesel")
    auto2 = Szemelyauto("SMZ-503", "Audi A6", 35000, 295, "diesel")
    auto3 = Teherauto("BEL-367", "Volvo FH16 750", 40000, 750, "benzin")

    kolcsonzo.autok_hozzaadasa(auto1)
    kolcsonzo.autok_hozzaadasa(auto2)
    kolcsonzo.autok_hozzaadasa(auto3)

    kolcsonzo.auto_berlese("RA 12-345", "Tallódi Zsolt", "2025-06-10", "2025-06-13")
    kolcsonzo.auto_berlese("SMZ-503", "Demeter Katalin", "2025-06-01", "2025-06-03")
    kolcsonzo.auto_berlese("BEL-367", "Szatmári Timea", "2025-06-30", "2025-07-02")
    kolcsonzo.auto_berlese("AA AA-788", "Varga Vivien", "2025-07-02", "2025-07-04")

def menu():
    # Konzolos menü, ami lehetővé teszi az autókölcsönző szolgáltatásainak elérését.
    kolcsonzo = Autokolcsonzo("CityRent")
    elozetes_feltoltes(kolcsonzo)

    while True:
        print("\n--- Autókölcsönző Menü ---")
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        print("4. Kilépés")

        valasztas = input("Kérem, adja meg a választott művelet sorszámát (1-4): ")

        if valasztas == "1":
            print("\n Elérhető autók:")
            for auto in kolcsonzo.autok:
                print(auto)

            rendszam = input("\nKérem, adja meg a kiválasztott autó rendszámát: ")
            nev = input("Bérlő neve: ")

            datum = input("Bérlés kezdete (ÉÉÉÉ-HH-NN): ")
            kezdo_datum = datetime.strptime(datum, "%Y-%m-%d")
            
            # Lehetővé tettem a kölcsönző számára a több napos bérlési lehetőséget.
            napok = int(input("Hány napra kívánja bérelni az autót?: "))
            vege_datum = kezdo_datum + timedelta(days=napok - 1)

            kezdo = kezdo_datum.strftime("%Y-%m-%d")
            vege = vege_datum.strftime("%Y-%m-%d")

            eredmeny = kolcsonzo.auto_berlese(rendszam, nev, kezdo, vege)
            print(f"\n{eredmeny}")

        elif valasztas == "2":
            rendszam = input("Kérem, adja meg a rendszámot: ")
            kezdo = input("Bérlés kezdete (ÉÉÉÉ-HH-NN): ")
            vege = input("Bérlés vége (ÉÉÉÉ-HH-NN): ")
            print(kolcsonzo.berles_lemondasa(rendszam, kezdo, vege))

        elif valasztas == "3":
            print("\nJelenlegi bérlések:")
            print(kolcsonzo.listaz_berleseket())

        elif valasztas == "4":
            print("Kilépés a rendszerből...")
            break

        else:
            print("Érvénytelen választás. Kérem, válasszon 1 és 4 közötti számot.")

if __name__ == "__main__":
    menu()
