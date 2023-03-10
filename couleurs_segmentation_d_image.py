# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 14:22:45 2023

@author: ram
"""

import matplotlib.pyplot as plt
import skimage 
import numpy as np

##########
##          Création des Classes
##########

class pixel:
   ### chaque pixel est défini par une intensité et une position i et j
   def __init__(self, r,v,b, i, j):
      self.r = r
      self.v=v
      self.b=b
      self.pos_i = i
      self.pos_j = j

class groupe :
    ### chaque groupe est définit par une liste (de pixels) et un centroide
    def __init__ (self, Liste, centroid) :
        self.Liste = Liste
        self.centroid = centroid
    ### le centroide est définit par la valeur moyenne de l'intensité des pixels de la liste
    ### on définit donc la valeur moyenne ci-dessous
    def valmoy(self):
        tot_r=0
        tot_v=0
        tot_b=0
        ### on passe en revue tout les éléments "i" (les pixels sont les éléments i) de la liste
        for i in self.Liste :
            ### tot est la somme totale de toutes les intensités des pixels i
            tot_r = tot_r+i.r
            tot_v= tot_v+i.v
            tot_b=tot_b + i.b
        if len(self.Liste)==0:
            self.centroid=[0,0,0]
        else :
            self.centroid = [tot_r/(len(self.Liste)),tot_v/(len(self.Liste)),tot_b/(len(self.Liste))]
        return self.centroid

class d_min:
    ### la distance minimum entre le centroid et l'intensité est définit par
    def __init__(self, distance, pos):
        ### un distance
        self.distance = distance
        ### et une position "pos" qui permet de savoir à quel groupe appartient la distance
        ### par exemple, s'il y a 4 groupes, pos = 1 ou  2 ou 3 ou 4
        self.pos = pos

class assignement:
    ### notre classe assignement est caractérisé par
    ### n groupes gr et une matrice de pixels (l'image d'entrée)
    def __init__(self, gr, matrice):
        self.gr = gr
        self.matrice = matrice
    ### ici on fait la méthode k-means qui prend en entrée
    ### un nombre d'itération (le nombre de fois ou le programme tourne)
    def Kmean(self, iteration): 
        x=0
        ### on crée les n listes finales de l'itération de k-means
        l_f=[]
        ### pour le groupe "i" dans la classe assignement
        for i in self.gr:
            ### la liste finale apprend une liste vide pour avoir la même taille
            ### que la liste de groupe
            l_f.append([])
        ### on commence l'itération ici
        while x<iteration :
            ### on regarde la ligne "line" de la matrice de pixels
            for line in self.matrice:
                ### on regarde l'élément "i" de notre ligne
                for i in line:
                    d=[]
                    ppos=0
                    listd=[]
                    ### on passe en revue les n groupes "e"
                    for e in self.gr :
                        ### la liste "d" apprend la distance entre le cetroide du groupe e
                        ### et l'intensité du pixel i pour nos n groupes
                        d_m=np.sqrt((e.centroid[0]-i.r)**2 +(e.centroid[1]-i.v)**2 + (e.centroid[2]-i.b)**2)
                        d.append(d_min(d_m, ppos))
                        ### puis la liste "listd" apprend les différentes distances
                        ### sans prendre compte du groupe
                        listd.append(d_m)
                        ### ppos augmente de 1 pour que l'on change de groupe à la prochaine boucle
                        ppos=ppos+1
                    ### mini est la distance minimale entre un centroide et l'intensité
                    ### indépendamment du groupe
                    mini=min(listd)
                    ### pour l'élément "e" (représentant un groupe) de la liste "d" de toutes nos distances
                    for e in d :
                        ### si la distance minimale (indé du groupe) est égale à la distance
                        ### dans le groupe en position e
                        if mini == e.distance:
                            ### alors le groupe en position e append le pixel i
                            self.gr[e.pos].Liste.append(i)
                    
            nb=0
            ### pour le groupe "i" dans la classe assignement
            for g in self.gr :
                ### l'élément "nb" de la liste finale l_f (qui représente le groupe en position nb)
                ### apprend la nouvelle liste (de pixels) que l'on a modifiée précedemment
                ### avec la méthode des k-means
                ### remarque : nb est le numéro du groupe g.
                l_f[nb] = g.Liste
                ### on recalcule les centroides de ce groupe en position nb (càd i)
                g.valmoy()
                ### on vide nos listes de groupe pour refaire une itération
                g.Liste=[]
                ### nb augmente de 1 pour passer au groupe suivant
                nb=nb+1
            ### ainsi à chaque itération, il n'y a que la valeur du centroide qui change
            ### lorsque la valeur du centroide ne bougera plus, on aura
            ### les pixels qui appartiennent tous au bon groupe
            ### x augmente de 1 pour faire une nouvelle itération de Kmeans
            x=x+1
            ### à la fin de l'itération (x>itération) on retourne les listes finales
            ### avec nos nouveaux groupes (avec uniquement des pixels similaires à l'intérieur)
        return l_f
 
       
##########
##         Lancement du Programme
##########

### on demande le nom du fichier avec son extension
text=str(input("Veuillez mettre le nom du ficher : "))
### et on demande aussi le nombre de groupe que l'on désire
nombregroupe=int(input("Veuillez mettre le nombre de groupe dont vous avez besoin : "))

### le nom du ficher est découpé en 2 parties séparés par un point.
### la 1ère partie est le "titre" du fichier
### la 2nd est l'extension du fichier
typee=text.split('.')
## si l'extension du ficher (2nd partie du nom du ficher) est un png
if typee[1]=='png':
    ### contenu est une chaine de caractère 
    ### contenant les intensités (en niveau de gris) de tout les pixels de l'image
    contenu = skimage.io.imread(text)
    ### on met chaque ligne "i" du contenu dans une matrice de i lignes
    matrice= list(list(i) for i in contenu)
# else :
#     with open(text,'r') as fichier:
#         contenu=fichier.read()
#         ### on lit la 1ère ligne du fichier texte 
#         ### et on la met comme 1ère ligne de matrice
#         ### on passe à la ligne suivante de matrice à la fin de chaque ligne de fichier lue
#     matrice=[[*map(int, line.split())] for line in contenu.split('\n')]


j=0
i=0
pixelmatrice=[]
pixelmatricetest=[]
linepixelmatrice=[]
linepixelmatricetest=[]
### ici on va assigner chaque pixel de notre matrice à un pixel "a"
### puis on va metre tout les pixels "a" dans une liste de pixels "pixelmatrice"

### pour la ligne "e" dans la matrice
for e in matrice :
    ### si la ligne e est vide
    if e == []:
        ### la ligne est supprimée
        matrice.pop(j)
    ### pour le pixel "a" de la ligne "e"
    for a in e :
        ### la liste "linepixelmatrice" apprend le pixel a en position i et j
        linepixelmatrice.append(pixel(a[0],a[1],a[2],i,j))
        ### on augmente i de 1 afin de passer au prochain pixel de la ligne
        i=i+1
    ### on augmente j de 1 afin de passer à la prochaine ligne de la matrice
    j=j+1
    ### on reprend au premier pixel de la nouvelle ligne
    i=0
    ### on vide la liste des pixels de la ligne
    linepixelmatrice=[]
    ### la matrice de pixel apprend les lignes de pixels
    pixelmatrice.append(linepixelmatrice)

    

### ici on va créer n groupes vides
n=0
groupes=[]
while n<nombregroupe:
    if n==0:
        groupes.append(groupe([],[255,0,0]))
    elif n==1 :
        groupes.append(groupe([],[0,255,0]))
    elif n==2 :
        groupes.append(groupe([],[0,0,255]))
    else :
        groupes.append(groupe([],[255%n,255%n,255%n]))
    n=n+1
    
### on lance l'assignement avec les n groupes et 
### notre liste de pixels provenant de notre fichier texte
ass = assignement(groupes, pixelmatrice)
listefinal = ass.Kmean(10)

nb_li=0
for li in listefinal :
    if li == []:
        listefinal.pop(nb_li)
    nb_li+=1

place_i=[]
place_j=[]
for l in listefinal :
    for p in l :
        place_i.append(p.pos_i)
        place_j.append(p.pos_j)
    width = np.shape(matrice)
    plt.axis([0,width[0],0,width[1]])
    plt.plot(place_j,place_i,'s',markersize=100,color='black')
    plt.show()
    place_i=[]
    place_j=[]

