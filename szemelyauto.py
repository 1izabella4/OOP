from auto import Auto

class Szemelyauto(Auto):
    # A személyautó osztály az Auto osztály leszármazottja, jellemzően személygépjárművekhez.
    def __init__(self, rendszam, tipus, berleti_dij, motor_teljesitmeny, uzemanyag_tipus):
        super().__init__(rendszam, tipus, berleti_dij)
        self.motor_teljesitmeny = motor_teljesitmeny
        self.uzemanyag_tipus = uzemanyag_tipus

    def __str__(self):
        return (
            f"Személyautó - {self.rendszam} ({self.tipus}), "
            f"{self.motor_teljesitmeny} LE, {self.uzemanyag_tipus}, "
            f"Díj: {self.berleti_dij} Ft/nap"
        )
