#https://pandas.pydata.org/docs/user_guide/merging.html#merging-join

import numpy as numpy
import matplotlib.pyplot as plt 
import pandas as pd

fileCours = "C:\\tmp\\Euronext_Equities_2022-03-15.csv"
fileData = "C:\\tmp\\data.csv"

cours = pd.read_csv(fileCours, sep=';')
donnees = pd.read_csv(fileData, sep=';')

# merge des deux fichiers sur la colonne ISIN
complet = pd.merge(cours, donnees, on="ISIN")

#export csv
complet.to_csv("C:\\tmp\\resultat.csv", sep=';')

