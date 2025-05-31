from berles import Berles
from datetime import datetime

class Autokolcsonzo:
  
    # Az autókölcsönző főosztálya, ami tárolja az autókat és bérléseket,
    # és biztosítja az autófelvétel, bérlés, lemondás és listázás lehetőségét.
    
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def autok_hozzaadasa(self, auto):
        # Egy új autó hozzáadása a kölcsönző kínálatához.
        self.autok.append(auto)

    def auto_berlese(self, rendszam, berlo_neve, kezdo_datum, veg_datum):
        # Új bérlés létrehozása, ha nincs időpontütközés az adott autóra.
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.datum_utkozik(kezdo_datum, veg_datum):
                return "Ez az autó foglalt a megadott időszakban."

        for auto in self.autok:
            if auto.rendszam == rendszam:
                uj_berles = Berles(auto, berlo_neve, kezdo_datum, veg_datum)
                self.berlesek.append(uj_berles)
                napok = uj_berles.napok_szama()
                total = napok * auto.berleti_dij
                return f"A bérlés sikeres! Összesen fizetendő: {total} Ft ({napok} napra)"

        return "Nincs ilyen rendszámú autó."

    def berles_lemondasa(self, rendszam, kezdo_datum, veg_datum):
        # Egy meglévő bérlés törlése rendszám és dátum alapján.
        for berles in self.berlesek:
            if (berles.auto.rendszam == rendszam and
                berles.kezdo_datum == kezdo_datum and
                berles.veg_datum == veg_datum):
                self.berlesek.remove(berles)
                return "Bérlés lemondva."
        return "Nem található ilyen bérlés."

    def listaz_berleseket(self):
        # Összes aktív bérlés kilistázása.
        if not self.berlesek:
            return "Nincs aktív bérlés."
        return "\n".join(str(b) for b in self.berlesek)
