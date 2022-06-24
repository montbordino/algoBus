from arret_bus import *
import time

def bellman(arretDepart, arretArrivee):
    #création des arcs à relacher
    chemin_arrets = {}
    for arret in noms_arrets:
        chemin_arrets[arret] = [float('inf'), None]
    chemin_arrets[arretDepart][0] = 0
        
    #resultat sous forme de liste [distanceMin, [arretDepart, ..., arretArrivee]]
    resultat = [0, []]
    
    # application de l'algorithme de bellman
    for i in range (len(noms_arrets)):
        for pred in noms_arrets:
            poid_pred = chemin_arrets[pred][0]
            for succ in voisin(pred):
                poid_succ = chemin_arrets[succ][0]
                if poid_pred + distarc(pred, succ) < poid_succ:
                    chemin_arrets[succ][0] = poid_pred + distarc(pred, succ)
                    chemin_arrets[succ][1] = pred
                    
    # modification du resultat
    resultat[0] = chemin_arrets[arretArrivee][0]                
    # création du chemin min pour aller de arretDepart à arretArrivee
    pos = arretArrivee
    while(pos != None):
        resultat[1].insert(0, pos)                  
        pos = chemin_arrets[pos][1]
                    
    return resultat
        
def fWarshall(arretDepart, arretArrivee):
    # créer la matrice pred
    pred = [ [None for i in range(len(poids_bus))] for i in range(len(poids_bus))]
    for i in range(len(poids_bus)):
        for j in range(len(poids_bus)):
            if poids_bus[i][j] > 0 and poids_bus[i][j] < float('inf'):
                pred[i][j] = i
                
    # créer resultat sous la forme [dist, [arretDepart, ..., arretArrivee]]
    resultat = [0, [arretDepart]]
    
    # parcours de la matrice poids_bus 
    for tour in range (len(poids_bus)):
        for ligne in range (len(poids_bus)):
            for colonne in range (len(poids_bus)):
                if poids_bus[ligne][tour] + poids_bus[tour][colonne] < poids_bus[ligne][colonne]:
                    poids_bus[ligne][colonne] = poids_bus[ligne][tour] + poids_bus[tour][colonne]
                    pred[ligne][colonne] = pred[tour][colonne]
   
    # remplir resultat
    resultat[0] = poids_bus[indice_som(arretDepart)][indice_som(arretArrivee)]
    pos = indice_som(arretArrivee)
    while (pred[indice_som(arretDepart)][pos]!=None):
        resultat[1].insert(1, nom(pos))
        pos = pred[indice_som(arretDepart)][pos]
    
    return resultat

def dijkstra(arretDepart, arretArrivee):
   
    #initialisation
    pred = [None for i in range(len(noms_arrets))]
    dejaTraite = [False for i in range(len(noms_arrets))]
    distance = [float('inf') for i in range(len(noms_arrets))]
    distance[indice_som(arretDepart)] = 0
    somDep = [0, arretDepart]
    resultat = [0, []]
    
    #calcul des plus cours chemins
    while dejaTraite[indice_som(arretArrivee)] == False:
        
        dejaTraite[indice_som(somDep[1])] = True
        
        for unVoisin in voisin(somDep[1]):
            if not dejaTraite[indice_som(unVoisin)]:
                dist_voisin = somDep[0] + distarc(somDep[1], unVoisin)
                
                if dist_voisin < distance[indice_som(unVoisin)]:
                    
                    distance[indice_som(unVoisin)] = dist_voisin #changement de distance
                    
                    pred[indice_som(unVoisin)] = somDep[1] # changement de predecesseur
            
        
        somDep = definirMin(distance, dejaTraite, pred) # definirMin a faire
        
    #remplissage du résultat
    resultat[0] = distance[indice_som(arretArrivee)]             
    # création du chemin min pour aller de arretDepart à arretArrivee
    pos = arretArrivee
    while(pos != None):
        resultat[1].insert(0, pos)
        pos = pred[indice_som(pos)]
        
    return resultat

def definirMin(distance, dejaTraite, nomArret):
    resultat = [float('inf'), None]
    for i in range (len(distance)):
        if resultat[0] > distance[i] and dejaTraite[i] == False:
            resultat[0] = distance[i]
            resultat[1] = noms_arrets[i]
    return resultat
  
a = dijkstra('ABB', 'PINS')
#testB = bellman('NOVE', 'CHPT')
#testF = fWarshall('NOVE', 'CHPT')
#testD = dijkstra('NOVE', 'CHPT')
