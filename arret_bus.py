import json
from math import sin, cos, acos, pi

noms_arrets = []

# A) importation de bd.txt dans donneesbus
with open('bd.txt') as bd:
    donneesbus = json.load(bd)

# B) création de noms_arrets 
for val in donneesbus.keys():
    noms_arrets.append(val)


# C) création des fonctions "basiques"

#renvoie le le nom de l'arret en fonction de son indice
def nom(ind): 
    return noms_arrets[ind]

#renvoie l'indice de l'arret en fonction de son nom
def indice_som(nom_som):
    return noms_arrets.index(nom_som)

#renvoie la latitude de nom_som
def latitude(nom_som):
    return donneesbus[nom_som][0]

#renvoie la longitude de nom_som
def longitude(nom_som):
    return donneesbus[nom_som][1]

#renvoie les arret voisins sous forme de liste de nom_som
def voisin(nom_som):
    return donneesbus[nom_som][2]


# D) représentation du réseau par un graphe

# en dictionnaire
dic_bus = {}
for val in donneesbus.keys():
    dic_bus[val] = voisin(val)

# en matrice
mat_bus = [ [0 for i in range(len(noms_arrets))] for i in range(len(noms_arrets))]
for pred in range (len(mat_bus)): 
    successeurs = voisin(nom(pred))
    for i in range (len(successeurs)):
        mat_bus[pred][indice_som(successeurs[i])] = 1
        
# E) distance

#renvoie en m la distance qui sépare A et B (deux coordonnées GPS) 
def distanceGPS(latA,latB,longA,longB):
 # Conversions des latitudes en radians
 ltA=latA/180*pi
 ltB=latB/180*pi
 loA=longA/180*pi
 loB=longB/180*pi
 # Rayon de la terre en mètres (sphère IAG-GRS80)
 RT = 6378137
 # angle en radians entre les 2 points
 S = acos(round(sin(ltA)*sin(ltB) + cos(ltA)*cos(ltB)*cos(abs(loB-loA)),14))
 
 # distance entre les 2 points, comptée sur un arc de grand cercle
 return S*RT

#renvoie la distance qui sépare deux arrets
def distarrets(arret1,arret2):
    return distanceGPS(latitude(arret1), latitude(arret2), longitude(arret1), longitude(arret2))

#renvoie la distance qui sépare deux arrets si ils sont voisins, sinon il renvoie un nombre infini
def distarc(arret1,arret2):
    if (mat_bus[indice_som(arret1)][indice_som(arret2)]):
        resultat = distarrets(arret1, arret2)
    elif arret1 == arret2:
        resultat = 0
    else:
        resultat = float("inf")
    return resultat

# F) graphe pondéré

#crée une matrice vide de la taille de noms_arrets
poids_bus = [ [None for i in range(len(noms_arrets))] for i in range(len(noms_arrets))]

#calcule la distance entre tous les arrets avec distarc()
for pred in range (len(poids_bus)):
    for succ in range (len(poids_bus)):
        poids_bus[pred][succ] = distarc(nom(pred), nom(succ))

# test des fonctions
"""
print(indice_som("PALI"))
print(latitude("NOVE"))
print(longitude("NOVE"))
print(voisin("NOVE"))
print(mat_bus[indice_som("HOUN")][indice_som("7PUI")])
print("NOVE", latitude("NOVE"), " | ", longitude("NOVE"))
print("7PUI", latitude("7PUI"), " | ", longitude("7PUI"))
print("Distance à vole d'oiseau: ",distarrets("NOVE", "7PUI"))
"""

# suppression des variables inutiles (optionnel)
del i, pred, succ, val, successeurs