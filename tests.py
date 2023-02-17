import matplotlib.pyplot as plt
import skimage 
import numpy as np

##########
##          Création des Classes
##########

class pixel:
   def __init__(self,g,i,j):
      self.intensite=g
      self.pos_i=i
      self.pos_j=j
   def __add__(self,other):
       if type(other)==pixel :
           return other.intensite + self.intensite
       elif type(other)==int :
           return other + self.intensite

class groupe :
    def __init__ (self, Liste, centroid) :
        self.Liste = Liste
        self.centroid = centroid
    def valmoy(self):
        tot=0
        for i in self.Liste :
            tot=tot+i.intensite
        self.centroid=tot/len(self.Liste)
        return self.centroid

class d_min:
    def __init__(self,distance,pos):
        self.pos=pos
        self.distance=distance

class assignement:
    ### notre classe assignement est caractérisé par
    ### n groupes g et une matrice de pixels
    def __init__(self,gr,matrice):
        self.gr=gr
        self.matrice = matrice
    ### ici on fait la méthode k-means qui prend en entrée
    ### un nombre d'itération (le nombre de fois ou le programme tourne)
    def ass(self,iteration): 
        x=0
        l_f=[]
        ### on crée les n listes finales de l'itération de k-means
        for i in self.gr:
            l_f.append([])
        ### on commence l'itération ici
        while x<iteration :
            ### on regarde la ligne l de la matrice de pixels
            for line in self.matrice:
                ### on regarde l'élément i de notre ligne
                for i in line:
                    d=[]
                    ppos=0
                    listd=[]
                    ### on calcule la distance entre le centroid et l'intensité
                    ### du pixel dans la matrice de pixels
                    for e in self.gr :
                        d.append(d_min(abs(e.centroid-i.intensite),ppos))
                        listd.append(abs(e.centroid-i.intensite))
                        ppos=ppos+1
                    mini=min(listd)
                    ### ensuite on met le pixel dans la liste du groupe
                    ### dans laquelle la distance entre l'intensité et 
                    ### le centroid est minimale.
                    ### ces listes de groupes étaient vides 
                    for e in d :
                        if mini==e.distance:
                            self.gr[e.pos].Liste.append(i)
            ### après avoir fait toute la liste, on met les listes des groupes 
            ### dans les listes finales
            nb=0
            for i in self.gr :
                l_f[nb]=i.Liste
                ### on recalcule les centroides des groupes
                i.valmoy()
                ### on vide nos listes de groupe pour refaire une itération
                i.Liste=[]
                nb=nb+1
            ### ainsi à chaque itération, il n'y a que la valeur du centroide qui change
            ### lorsque la valeur du centroide ne bougera plus, on aura
            ### les pixels qui appartiennent tous au bon groupe
            x=x+1
        return l_f
 
       
##########
##         Lancement du Programme
##########

### on input le nom du fichier avec son extension et on met aussi le nombre de groupe
### que l'on désire
text=str(input("Veuillez mettre le nom du ficher : "))
nombregroupe=int(input("Veuillez mettre le nombre de groupe dont vous avez besoin : "))



typee=text.split('.')
if typee[1]=='png':
    contenu = skimage.io.imread(text,as_gray=True)
    matrice= list(list(i) for i in contenu)
else :
    with open(text,'r') as fichier:
        contenu=fichier.read()
        ### on lit la 1ère ligne du fichier texte 
        ### et on la met comme 1ère ligne de matrice
        ### on passe à la ligne suivante de matrice à la fin de chaque ligne de fichier lue
    matrice=[[*map(int, line.split())] for line in contenu.split('\n')]


### ici on assigne chaque valeur dans notre matrice à un pixel
### puis on met tous les pixels dans une liste
j=0
i=0
pixelmatrice=[]
linepixelmatrice=[]
maxii=[]
for e in matrice :
    if e == []:
        matrice.pop(j)
    else :
        maxii.append(max(e))
    for a in e :
        linepixelmatrice.append(pixel(a,i,j))
        i=i+1
    j=j+1
    i=0
    linepixelmatrice=[]
    pixelmatrice.append(linepixelmatrice)
    

maxi=max(maxii)

n=0
groupes=[]
while n<nombregroupe:
    groupes.append(groupe([],maxi/(n+1)))
    n=n+1
    
### on lance l'assignement avec les n groupes et 
### notre liste de pixels provenant de notre fichier texte
kmean=assignement(groupes, pixelmatrice)
listefinal = kmean.ass(30)


place_i=[]
place_j=[]
for l in listefinal :
    for p in l :
        place_i.append(p.pos_i)
        place_j.append(p.pos_j)
    plt.plot(place_j,place_i,',',markersize=1,color='black')
    plt.show()
    place_i=[]
    place_j=[]

