import numpy as numpy
import matplotlib.pyplot as plt 
import pandas as pd

filename = "C:\\tmp\\Euronext_Equities_2022-03-15.csv"

donnees = pd.read_csv(filename, sep=';')

# Vérifier les dimensions

print('dimensions : ', donnees.shape)

#Visualiser les données pour vérifier le chargement
print('Liste des colonnes :')
print(donnees.columns)
print('Premières lignes :')
print(donnees.head())
print(donnees)
type(donnees)

# Visualiser une colonne
print(donnees['Name'])
type(donnees['Name'])

# Visualiser une ligne
print(donnees.loc[5])
print(donnees.loc[[5]])

# Visualisation par coordonnee
print('iloc')
print(donnees.iloc[5:10, 5:10])

#Slicing

print(donnees['ISIN'][5:10])

#Suppression des lignes non nécessaires 
donnees = donnees.drop([0, 1, 2], axis=0)
# donnees = donnees.dropna(axis=0)
print('dimensions : ', donnees.shape)
print(donnees.head())

#suppression des colonnes non nécessaires
donnees = donnees.drop(['Volume', 'Turnover', 'Time Zone'], axis=1)
#donnees.drop(['Volume', 'Turnover', 'Time Zone'], axis=1, inplace=True)
print(donnees.head())

#Description des données 
print(donnees.describe())

#Conversion des champs numeriques
#donnees['Open'] = donnees['Open'].astype(float)

#Sélection des ligne où open est à '-'
index_liste = donnees[ donnees ['Open'] == '-' ].index
print(index_liste)
donnees = donnees.drop(index_liste)

#Conversion des champs numeriques
donnees['Open'] = donnees['Open'].astype(float)
donnees['High'] = donnees['High'].astype(float)
donnees['Low'] = donnees['Low'].astype(float)
donnees['Last'] = donnees['Last'].astype(float)
print(donnees.describe())
print(donnees['Last'] > 10.0)
print(donnees[donnees['Last'] > 10.0])

#Conversion de la colonne date 
donnees['Last Date/Time'] = pd.to_datetime(donnees['Last Date/Time'], format="%d/%m/%Y %H:%M")

#Répartition des actions sur les marchés 
print(donnees['Market'].value_counts())
donnees['Market'].value_counts().plot.pie()
#donnees['Market'].value_counts().plot.bar()
#plt.show()

# Agrégation des données
print(donnees.groupby(['Market']).mean())


# Garder les valeurs ou la valeur de cloture est > 10.0
index_liste = donnees[ donnees ['Last'] < 10.0 ].index
print(index_liste)
donnees = donnees.drop(index_liste )

# Garder les valeurs ou la valeur de cloture est > à la valeur d'ouverture
index_liste = donnees[ donnees ['Last'] < donnees ['Open'] ].index
print(index_liste)
donnees = donnees.drop(index_liste )

# Garder les valeur qui ont eu un mouvement dans les 60 derniers jours
index_liste = donnees[ donnees ['Last Date/Time'] > pd.to_datetime('today') - pd.Timedelta(60, "d") ].index
print(index_liste)
donnees = donnees.drop(index_liste )

#export csv
donnees.to_csv("C:\\tmp\\resultat.csv", sep=';')


