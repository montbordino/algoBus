"""
@authors: Tom Montbord - apascal003
"""

from arret_bus import *
from graphics import *

""" R E C H E R C H E   D E   M I N   L A T / L O N G """
def minLatLong():
    minLat = float('inf')
    minLong = float('inf')
    for i in range (len(noms_arrets)):
        minLat = min(minLat, latitude(nom(i)))
        minLong = min(minLong, longitude(nom(i)))
    return [minLat, minLong]


limites = minLatLong()
mapBG = Image(Point(0,0), "map.gif")
echelle = 3600
coeficient = 1.38
premierArret = Point(25, 10)
longueur = mapBG.getWidth()
largeur = mapBG.getHeight()

def affichageCarte(longueur,largeur):
    win = GraphWin("S2.02 partie 3", longueur, largeur)
    mapBG = Image(Point(longueur/2,largeur/2), "map.gif")
    mapBG.draw(win)
    traceMap(win)
    afficheBoutonsCarte(win)

    return 0


def traceMap(win):

    for arret in noms_arrets:
        p1 = Point((longitude(arret) - limites[1]) * echelle + premierArret.getX(), largeur - ((latitude(arret) - limites[0]) * echelle * coeficient) - premierArret.getY())
        c = Circle(p1, 4)
        c.setFill("white")
        c.draw(win)
        
def traceResult(liste, win):
    for arret in liste:
        # affichage du cercle
        p = Point((longitude(arret) - limites[1]) * echelle + premierArret.getX(), largeur - ((latitude(arret) - limites[0]) * echelle * coeficient)- premierArret.getY())
        c = Circle(p, 4)
        c.setFill("red")
        c.draw(win)
        # affichage du nom
        pM = Point(p.getX() - 20, p.getY() - 20)
        m = Text(pM, arret)
        m.setSize(8)
        m.setFill("blue")
        m.draw(win)
        
def relierArret(arret1, arret2,win):
    p1 = Point((longitude(arret1) - limites[1]) * echelle + premierArret.getX(), largeur - ((latitude(arret1) - limites[0]) * echelle * coeficient)- premierArret.getY())
    p2 = Point((longitude(arret2) - limites[1]) * echelle + premierArret.getX(), largeur - ((latitude(arret2) - limites[0]) * echelle * coeficient)- premierArret.getY()) ### ameliorable
    l = Line(p1, p2)
    l.draw(win)

def Menu(win):
    #création de la fenêtre du menu
    menu = GraphWin("Entrez les informations", 300, 220)
    estOuvert = True #création de variable pour arreter le problème de test dans fenetre fermé
    
    #Rectangle pour valider se qu'on rentre comme infos
    hgV = Point(20,183)
    bdV = Point(280,208)
    
    hgCoXV = hgV.getX()
    hgCoYV = hgV.getY()
    
    bdCoXV = bdV.getX()
    bdCoYV = bdV.getY()
    
    
    #Rectangle pour afficher les informations à entrer
    hgI = Point(60,155)
    bdI = Point(240,175)
    
    hgCoXI = hgI.getX()
    hgCoYI = hgI.getY()
    
    bdCoXI = bdI.getX()
    bdCoYI = bdI.getY()
    
    
    #Saisie de l'arret de départ
    entryArretDepart = Entry(Point(60, 30), 10)
    entryArretDepart.draw(menu)
    
    #Texte de ce qui faut saisir
    depart = Text(Point(200,30), "Saisissez l'arret de depart")
    depart.draw(menu)
    
    
    #Saisie de l'arret d'arrivée'
    entryArretArrivee = Entry(Point(60, 80), 10)
    entryArretArrivee.draw(menu)
    
    #Texte de ce qui faut saisir
    arrive = Text(Point(200,80), "Saisissez l'arret d'arrivé")
    arrive.draw(menu)
    
    
    #Saisie de l'algo
    entryAlgo = Entry(Point(60, 130), 10)
    entryAlgo.draw(menu)
    
    #Texte de ce qui faut saisir
    algo = Text(Point(200,130), "Saisissez l'algorithme")
    algo.draw(menu)


    #Affichage du bouton d'infos
    infos = Text(Point(150,165), "Informations à renseigner")    
    infos.draw(menu)
    IRectangle = Rectangle(hgI,bdI)
    IRectangle.draw(menu)

    #Affichage du bouton de validation
    valide = Text(Point(150,195), "Cliquez pour valider les informations")    
    valide.draw(menu)
    VRectangle = Rectangle(hgV,bdV)
    VRectangle.draw(menu)

    #Test si on valide les informations
    testClicBoutonMenu(win, menu, hgCoXV, hgCoYV, bdCoXV, bdCoYV, hgCoXI, hgCoYI, bdCoXI, bdCoYI, entryArretDepart, entryArretArrivee, entryAlgo)
    
    return 0


def infos():
    info = GraphWin("Informations à saisir", 800, 150) #création de la fenetre d'informations
    estOuverte = True
    
    infosArrets = Text(Point(400,30), "Vous devez entrez un nom d'arret parmi la liste des arrets pour la case arret de départ et arret d'arrive") # mettre un bouton qui affiche la liste des arrets
    infosArrets.draw(info)  #informations à renseinger dans les cases d'arrets
    
    bouton = Text(Point(400,70), "Cliquez pour afficher la liste des arrets")
    bouton.draw(info)   #bouton pour afficher la liste des arrets
    
    hg = Point(265,55) #créations des points du rectangle
    bd = Point(535,85)
    
    rectangle = Rectangle(hg,bd) #création du rectangle à partir des points précédents
    rectangle.draw(info)
    
    hgCoX = hg.getX() #récupérations des cos pour le point haut gauche du rectangle
    hgCoY = hg.getY()
    
    bdCoX = bd.getX() #récupérations des cos pour le point bas droit du rectangle
    bdCoY = bd.getY()
    
    infosAlgo = Text(Point(400,120), "Pour choisir Dijkstra : saisissez D ; pour choisir Bellman : saisissez B")
    infosAlgo.draw(info) #informations a renseigner dans la case algorithme
    
    
    
    quitter = Text(Point(750,125), "Quitter")
    quitter.draw(info)

    hgQ = Point(725,115) #créations des points du rectangle pour quitter
    bdQ = Point(775,135)

    rectangleQ = Rectangle(hgQ,bdQ) #création du rectangle à partir des points précédents
    rectangleQ.draw(info)
    
    hgCoXQ = hgQ.getX() #récupérations des cos pour le point haut gauche du rectangle
    hgCoYQ = hgQ.getY()
    
    bdCoXQ = bdQ.getX() #récupérations des cos pour le point bas droit du rectangle
    bdCoYQ = bdQ.getY()

    testClicBoutonInfo(info, hgCoX, hgCoY, bdCoX, bdCoY, hgCoXQ, hgCoYQ, bdCoXQ, bdCoYQ, estOuverte) #on teste si le bouton pour afficher la liste des arret est cliqué

    return 0



def listeArrets():
    arrets = GraphWin("Liste des arrets (cliquez n'importe où pour fermer)",1160, 950)
 #création de la fenêtre contenant la liste de tous les arrets
    
    nbColonnes = 15 #nombre de colonne dans la fenetre (1 contient 31 arrets)    
    nbArrets = int(len(noms_arrets)/nbColonnes) #calcule le nombre d'arrets par colonne
    numArretDepart = 0 #indice de l'arret de départ
    
    for x in range(50,1125,75): #boucle incrémentant la position en x de chaque colonne
        coYColonne = 30 #on commence a 30 pour ne pas être collé a la fenetre
        
        for i in range(numArretDepart,nbArrets): #boucle allant de l'indice de l'arret de départ au nombre d'arret 
            listeArrets = Text(Point(x,coYColonne), noms_arrets[i]) #création du texte de l'arret
            listeArrets.draw(arrets) #affichage du texte
            coYColonne += 30    # on descend les coY des arrets pour ne pas les empiler
            
        numArretDepart += 31 # a chaque fois que 31 arrets sont listé (colonne pleine) on commence à partir du dernier déjà fait
        nbArrets += 31 # on finis 31 arrets plus loin
        
    arrets.getMouse() #on attend un clic
    arrets.close() #on ferme la fenetre
            
    return 0     


#Fonction qui permet de tester si le bouton pôur afficher la lsite des arrets est bien cliqué (genre dans le rectangle)
def testClicBoutonInfo(fenetre, hgCoX, hgCoY, bdCoX, bdCoY, hgCoXQ, hgCoYQ, bdCoXQ, bdCoYQ, estOuverte):
    while (estOuverte == True):
        coClick = fenetre.getMouse() #on attend un clic souris
        coClickX = coClick.getX()   #on récupère les cos du click
        coClickY = coClick.getY()
        
        if coClickX > hgCoX and coClickX < bdCoX and coClickY > hgCoY and coClickY < bdCoY: #Test si c'est dans le bouton afficher arret
            listeArrets() #on affiche la liste des arrets
        elif coClickX > hgCoXQ and coClickX < bdCoXQ and coClickY > hgCoYQ and coClickY < bdCoYQ: #Test si c'est dans le bouton quitter
            estOuverte = False
            fenetre.close() #on ferme cette fenetre
              
    return 0

#Fonction qui permet de tester si le bouton pour afficher les informations à rentrer ou pour valider est bien cliqué 
def testClicBoutonMenu(win, menu, hgCoXV, hgCoYV, bdCoXV, bdCoYV, hgCoXI, hgCoYI, bdCoXI, bdCoYI, entryArretDepart, entryArretArrivee, entryAlgo):
    boutonClique = False #tant que l'on n'a pas validé les infos on boucle
    while (boutonClique == False): 
        coClick = menu.getMouse()#on attend un click de l'utilisateur     
        coClickX = coClick.getX()#on récupère les cos du click
        coClickY = coClick.getY()
        
        if coClickX > hgCoXI and coClickX < bdCoXI and coClickY > hgCoYI and coClickY < bdCoYI: #Test si c'est sur le bouton d'informations
            infos()#on ouvre le menu d'infos

        elif coClickX > hgCoXV and coClickX < bdCoXV and coClickY > hgCoYV and coClickY < bdCoYV: #Test si c'est sur le bouton de valider
            definirArret(win, menu,entryArretDepart, entryArretArrivee, entryAlgo, hgCoXV, hgCoYV, bdCoXV, bdCoYV, hgCoXI, hgCoYI, bdCoXI, bdCoYI)
            boutonClique = True
            menu.close() # si c'est cliqué on ferme la fenetre
            
    return 0
                    

#testClicBoutonMenu(menu, hgCoXV, hgCoYV, bdCoXV, bdCoYV, hgCoXI, hgCoYI, bdCoXI, bdCoYI)

def definirArret(win, menu,entryArretDepart, entryArretArrivee, entryAlgo, hgCoXV, hgCoYV, bdCoXV, bdCoYV, hgCoXI, hgCoYI, bdCoXI, bdCoYI):
    
    lAlgos = ["D","B","F"]
    
    depart = entryArretDepart.getText()
    arrive = entryArretArrivee.getText()
    
    algo = entryAlgo.getText()
    
    
    if depart == "":
        erreurD = Text(Point(200,48), "Aucun arrêts saisis") #18 en dessous
        erreurD.setTextColor("red")
        erreurD.draw(menu)
        time.sleep(2)
        erreurD.setText("")
        
        testClicBoutonMenu(win, menu, hgCoXV, hgCoYV, bdCoXV, bdCoYV, hgCoXI, hgCoYI, bdCoXI, bdCoYI, entryArretDepart, entryArretArrivee, entryAlgo)
        
    elif depart not in noms_arrets:
         erreurD = Text(Point(200,48), "L'arret n'existe pas") #18 en dessous
         erreurD.setTextColor("red")
         erreurD.draw(menu)
         time.sleep(2)
         erreurD.setText("")
        
         testClicBoutonMenu(win, menu, hgCoXV, hgCoYV, bdCoXV, bdCoYV, hgCoXI, hgCoYI, bdCoXI, bdCoYI, entryArretDepart, entryArretArrivee, entryAlgo)
        
    if arrive == "":
        erreurA = Text(Point(200,98), "Aucun arrêts saisis") #18 en dessous
        erreurA.setTextColor("red")
        erreurA.draw(menu)
        time.sleep(2)
        erreurA.setText("")

        testClicBoutonMenu(win, menu, hgCoXV, hgCoYV, bdCoXV, bdCoYV, hgCoXI, hgCoYI, bdCoXI, bdCoYI, entryArretDepart, entryArretArrivee, entryAlgo)
        
    elif arrive not in noms_arrets:
         erreurA = Text(Point(200,98), "L'arret n'existe pas") #18 en dessous
         erreurA.setTextColor("red")
         erreurA.draw(menu)
         time.sleep(2)
         erreurA.setText("")

         testClicBoutonMenu(win, menu, hgCoXV, hgCoYV, bdCoXV, bdCoYV, hgCoXI, hgCoYI, bdCoXI, bdCoYI, entryArretDepart, entryArretArrivee, entryAlgo)
        
    
    if (algo in lAlgos):
        if (algo == "D"):
            dijkstra(depart, arrive, win)
            menu.close()
            
        elif (algo == "B"):
            bellman(depart, arrive, win)
            menu.close()

        elif (algo == "F"):
            menu.close()
            fWarshall(depart,arrive, win)
            
    elif algo == "":
        erreurA = Text(Point(200,145), "Aucun algorithmes saisis") #18 en dessous
        erreurA.setTextColor("red")
        erreurA.draw(menu)
        time.sleep(2)
        erreurA.setText("")
        
        testClicBoutonMenu(win, menu, hgCoXV, hgCoYV, bdCoXV, bdCoYV, hgCoXI, hgCoYI, bdCoXI, bdCoYI, entryArretDepart, entryArretArrivee, entryAlgo)
    
    else:
        algo = Text(Point(200,145), "L'algorithme n'existe pas") #18 en dessous
        algo.setTextColor("red")
        algo.draw(menu)
        time.sleep(2)
        algo.setText("")
                
        testClicBoutonMenu(win, menu, hgCoXV, hgCoYV, bdCoXV, bdCoYV, hgCoXI, hgCoYI, bdCoXI, bdCoYI, entryArretDepart, entryArretArrivee, entryAlgo)
    return 0
    
#Fonction qui permet de tester si le bouton valider est bien cliqué (genre dans le rectangle)
def testClicBoutonValiderCarte(win,CoXHautGauche,CoYHautGauche,CoXBasDroite,CoYBasDroite,hgCoXN, hgCoYN, bdCoXN, bdCoYN,estOuverte):
    while (estOuverte == True): 
        coClick = win.getMouse() #on attend un click de l'utilisateur
        coClickX = coClick.getX()#on récupère les cos du click
        coClickY = coClick.getY()
        
        #on compare les co du click avec les co du rectangle
        if coClickX > CoXHautGauche and coClickX < CoXBasDroite and coClickY > CoYHautGauche and coClickY < CoYBasDroite: #Test si c'est dans le rectangle
            Menu(win) #si c'est à l'interieur, on affiche le menu
            
            
        elif coClickX > hgCoXN and coClickX < bdCoXN and coClickY > hgCoYN and coClickY < bdCoYN: #Test si c'est dans le rectangle
            estOuverte = False
            win.close()
            affichageCarte(longueur, largeur)  
    return 0
            

def afficheBoutonsCarte(win):
    estOuverte = True #création de variable pour arreter le problème de test dans fenetre fermé
    
    boutonRenseignementInfos = Text(Point(100,25), "Entrez des informations") #Ecriture du texte bouton
    boutonRenseignementInfos.draw(win) #dans win
    
    hgR = Point(10,10) #place point représentant coordonnées du coin supérieur gauche du rectangle
    bdR = Point(190,40) #place point représentant coordonnées du coin inférieur droit du rectangle
    
    aRectangle = Rectangle(hgR,bdR) #Création du rectangle avec les deux points choisi
    aRectangle.draw(win) #traçage du rectangle
    
    hgCoX = hgR.getX() #récupération des coordonnés de chaque points
    hgCoY = hgR.getY()
    
    bdCoX = bdR.getX()
    bdCoY = bdR.getY()
    
    
    hgN = Point(10,50)
    bdN = Point(190,80)
    
    boutonInfos = Text(Point(100,65), "Relancer la carte") # création du bouton pour relancer la carte
    boutonInfos.draw(win) # on le dessine 
    
    aRectangle = Rectangle(hgN,bdN) #On dessine le rectangle pour le bouton relancer
    aRectangle.draw(win)
    
    hgCoXN = hgN.getX() #récupération des coordonnés de chaque points
    hgCoYN = hgN.getY()
    
    bdCoXN = bdN.getX()
    bdCoYN = bdN.getY()

    testClicBoutonValiderCarte(win, hgCoX, hgCoY, bdCoX, bdCoY, hgCoXN, hgCoYN, bdCoXN, bdCoYN, estOuverte) #on teste si le bouton est cliqué #y a win, win parce que 1 arg et pour pouvoir l'utiliser dans la carte en général et l'autre specifique à celle là

    return 0


def bellman(arretDepart, arretArrivee, win):
    print("calcul bellman en cours ...")
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
                if i == 1:                                      # permet de n'afficher qu'une fois le trait pour chaque ligne
                    relierArret(pred, succ, win) 
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
    traceResult(resultat[1], win)
    print("calcul bellman terminé")

def dijkstra(arretDepart, arretArrivee,win):
    print("calcul dijkstra en cours ...")
    #initialisation
    pred = [None for i in range(len(noms_arrets))]
    dejaTraite = [False for i in range(len(noms_arrets))]
    distance = [float('inf') for i in range(len(noms_arrets))]
    distance[indice_som(arretDepart)] = 0
    somDep = [0, arretDepart]
    resultat = [0, []]
    premierTour = True
    
    #calcul des plus cours chemins
    while dejaTraite[indice_som(arretArrivee)] == False:
        dejaTraite[indice_som(somDep[1])] = True
        for unVoisin in voisin(somDep[1]):
            if not dejaTraite[indice_som(unVoisin)]:
                if premierTour:  # permet de n'afficher qu'une fois le trait pour chaque ligne
                    relierArret(unVoisin, somDep[1],win)
                dist_voisin = somDep[0] + distarc(somDep[1], unVoisin)
                if dist_voisin < distance[indice_som(unVoisin)]:
                    distance[indice_som(unVoisin)] = dist_voisin #changement de distance
                    pred[indice_som(unVoisin)] = somDep[1] # changement de predecesseur
        
        somDep = definirMin(distance, dejaTraite, pred,win) # definirMin a faire
        
    #remplissage du résultat
    resultat[0] = distance[indice_som(arretArrivee)]             
    # création du chemin min pour aller de arretDepart à arretArrivee
    pos = arretArrivee
    while(pos != None):
        resultat[1].insert(0, pos)
        pos = pred[indice_som(pos)]
    print("calcul dijkstra terminé")
    traceResult(resultat[1],win)

def definirMin(distance, dejaTraite, nomArret, win):
    resultat = [float('inf'), None]
    for i in range (len(distance)):
        if resultat[0] > distance[i] and dejaTraite[i] == False:
            resultat[0] = distance[i]
            resultat[1] = noms_arrets[i]
    return resultat

def fWarshall(arretDepart, arretArrivee, win):
    # créer la matrice pred
    print("calcul Floyd Warshall en cours ...")
    pred = [ [None for i in range(len(poids_bus))] for i in range(len(poids_bus))]
    for i in range(len(poids_bus)):
        for n in range(len(poids_bus)):
            if poids_bus[i][n] > 0 and poids_bus[i][n] < float('inf'):
                pred[i][n] = i
                
                
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
    print("calcul Floyd Warshall terminé ...")
    traceResult(resultat[1], win)
    
    

""" A P P E L   D E S   F O N C T I O N S """
affichageCarte(longueur,largeur)


