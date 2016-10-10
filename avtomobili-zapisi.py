class Avto():
    znamka = ""
    model = ""
    barva = ""

    def izpisi(self):
        return self.znamka + "; " + self.model + "; " + self.barva + "\n"

avto1 = Avto()
avto1.znamka = "BMW"
avto1.model = "M3"
avto1.barva = "rdeca"

avto2 = Avto()
avto2.znamka = "Audi"
avto2.model = "S2"
avto2.barva = "zelena"

avto3 = Avto()
avto3.znamka = "Volkswagen"
avto3.model = "Golf"
avto3.barva = "crna"

avtomobili = [avto1, avto2, avto3]

with open("avtomobili.txt", "w+") as avtomobili_file:
    avtomobili_file.write("znamka; model; barva\n")
    for x in avtomobili:
        avtomobili_file.write(x.izpisi())
