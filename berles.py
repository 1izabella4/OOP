from datetime import datetime

class Berles:
    # Ez egy autóbérlést szemléltető osztály.
    # Tartalmazza az autót, a bérlő nevét, valamint a kezdő és záró dátumot.
    def __init__(self, auto, berlo_neve, kezdo_datum, veg_datum):
        self.auto = auto
        self.berlo_neve = berlo_neve
        self.kezdo_datum = kezdo_datum
        self.veg_datum = veg_datum

    def __str__(self):
        return (
            f"{self.berlo_neve} kölcsönzi a(z) {self.auto.rendszam} rendszámú autót "
            f"({self.kezdo_datum} → {self.veg_datum})"
        )

    def datum_utkozik(self, masik_kezd, masik_veg):
    # Visszaadja, hogy a megadott időszak ütközik-e ezzel a bérléssel.
        kezdo = datetime.strptime(self.kezdo_datum, "%Y-%m-%d")
        veg = datetime.strptime(self.veg_datum, "%Y-%m-%d")
        masik_kezd = datetime.strptime(masik_kezd, "%Y-%m-%d")
        masik_veg = datetime.strptime(masik_veg, "%Y-%m-%d")
        return kezdo <= masik_veg and masik_kezd <= veg

    def napok_szama(self):
        # Úgy gondoltam, hogy komfortosabb a bérlő számára, ha kiszámolja a bérlés hosszát napokban.
        kezdo = datetime.strptime(self.kezdo_datum, "%Y-%m-%d")
        veg = datetime.strptime(self.veg_datum, "%Y-%m-%d")
        return (veg - kezdo).days + 1
