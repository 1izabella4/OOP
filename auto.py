class Auto:
    # Az Auto osztály egy általános járműosztály,
    # amit más járműtípusok örökölnek (pl. személyautó, teherautó).
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij
