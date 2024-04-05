class StructCours:

    def __init__(self, x):
        self._nom = x[0]
        self._isin = x[1]
        self._symbol = x[2]
        self._ouverture = float(x[5])



filename = "C:\\tmp\\Euronext_Equities_2022-03-15.csv"

ligneCompte = 0
cours = {}

with open(filename) as f:
    for ligne in f:
        if (ligneCompte >= 4 ):
            x = ligne.replace('"', '').split(";")
            if not '-' in x:
                cours[x[1]] = StructCours(x)

        ligneCompte += 1

print(type(cours['FR0000063935']._ouverture))