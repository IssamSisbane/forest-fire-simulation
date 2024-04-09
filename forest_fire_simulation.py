from random import *
import os
import pickle
import numpy as np


# On recupère les variables globales stockés dans le fichier variables.txt
if os.path.exists("variables.txt"):
    with open("variables.txt","rb") as file:
        variables = pickle.load(file)

# On nomme les variables
if len(variables) != 0:
    PROBA = variables[0] # probabilité qu'un arbre s'enflamme
    H = variables[1] # nombre d'arbres en hauteur
    L = variables[2] # nombre d'arbres en largeur
    Enfeu_initiale = variables[3] # Liste des emplacements des arbres en feu à l'etape initiale sous forme de tuples
    print("\nProbabilité :",PROBA)
    print("Hauteur :",H)
    print("Largeur :",L)
    print("Cases en feu initialement :",Enfeu_initiale)

Enfeu = list(Enfeu_initiale)
arbres_etat = np.zeros((L, H), dtype=int) #on initialise un tableau a deux dimensions avec L le nombre de colonnes et H le nombre de lignes
narbres = int(H*L) # nombre d'arbres total



"""
Entrée: int i, int j  => coordonnées d'une case de la grille
Renvoi toutes les cases voisines.
Sur les bords on a pas le même nombre de voisin que au milieu de la grille.
"""
def recup_voisins(i,j) :

    voisins = []

    if type(i) == int and type(j) == int:
        

        if (i in range(1,L-2)) and (j in range(1,H-2)) :
            voisins = [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]

        elif (i in range(1,L-1)) and (j==0):
            voisins = [(i-1,j),(i+1,j),(i,j+1)]

        elif (i == 0) and (j in range(1,H-1)) :
            voisins = [(i+1,j),(i,j+1),(i,j-1)]

        elif (i == L-1) and (j in range(1,H-1)) :
            voisins = [(i-1,j),(i,j+1),(i,j-1)]

        elif (i in range(1,L-1) and j == H-1) :
            voisins = [(i-1,j),(i,j-1),(i+1,j)]

        elif i == L-1 and j == H-1 :
            voisins = [(i-1,j),(i,j-1)]

        elif i == 0 and j ==0 :
            voisins = [(i+1,j),(i,j+1)]
        
        elif i == L-1 and j == 0 :
            voisins = [(i-1,j),(i,j+1)]

        elif i == 0 and j == H-1:
            voisins = [(i+1,j),(i,j-1)]

        elif i < 0 or j <0 or i >= L and j >= H :
            raise ValueError("Les entiers en paramètres ne sont pas valides")

    else :
        raise TypeError("Les paramètres entrés ne sont pas des entiers")

    return voisins

"""
Sortie --> int: nb_arbres_cendres
Met à jour la grille en enlfammant les cases voisines des cases dejà en feu et en reduisant en cendres les cases precedemment en feu
"""
def maj_etat() :

    cases_en_feu = list(Enfeu)              #On copie la liste car sinon on bouclerait sur le for a l'infini
    nb_arbres_cendres = 0                      #nombre d'arbres en cendres

    for case_en_feu in cases_en_feu :
       colonne_enfeu,ligne_enfeu = case_en_feu        #on recupère les coordonnées de la case en feu
       
       #on s'occupe de chaque voisin
       for voisin in recup_voisins(colonne_enfeu,ligne_enfeu):
            colonne_voisin,ligne_voisin = voisin
                                     #on recupère les coordonnées du voisin
            if(arbres_etat[colonne_voisin][ligne_voisin] == 0) :       #Si l'etat de la case est 0 donc la case n'est pas enflammée alors on passe à la suite
               
               if(random() < PROBA):        #Un case à une probabilité de s'enflammer de PROBA
                    arbres_etat[colonne_voisin][ligne_voisin] = 1     #On met à jour la case qui devient en feu
                    Enfeu.append((colonne_voisin,ligne_voisin))        #On ajoute la case à la liste des cases en feu

       arbres_etat[colonne_enfeu][ligne_enfeu] = 2     #On met à jour la case qui était en feu et qui est reduit en cendres donc 2
       Enfeu.pop(Enfeu.index(case_en_feu))  #On enleve la case de la liste des cases en feu
       nb_arbres_cendres += 1

    return nb_arbres_cendres

"""
Sortie: boolean
Renvoi un booleén pour savoir si il reste des cases enflammée dans notre liste
"""
def test_fin() :
    return not 1 in arbres_etat

#on rempli notre listes des etats avec les cases en feu initialement
for arbre in Enfeu :
    colonne_arbre, ligne_arbre = arbre
    arbres_etat[colonne_arbre][ligne_arbre] = 1

etape = 0
nb_arbres_cendres = 0


print("\nEtat Initial : \n")
print(arbres_etat)

while not test_fin():

    etape = etape + 1
    nb_arbres_cendres += maj_etat()

    print("\n-------------------------------")
    print("Etape : ",etape, " ====> ",test_fin(),"\n")
    print(arbres_etat)
    print("\nNombre de cases reduites en cendres : ",nb_arbres_cendres)
    print("-------------------------------\n")

    


print("\nEtat Final : \n")
print(arbres_etat)
print("\nNombre total de cases reduites en cendres : ",nb_arbres_cendres)
print("\nNombre d'arbres au total : ", narbres)
print("\nNombre d'arbres restants : ", narbres - nb_arbres_cendres)
print("Nombre total d'etapes : ",etape)



#On réecrit dans notre fichier nos variables
if os.path.exists("variables.txt"):
    with open("variables.txt","wb") as file:
        variables = [PROBA, H, L, Enfeu_initiale]
        pickle.dump(variables, file)
        file.close()