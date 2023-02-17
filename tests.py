import matplotlib.pyplot as plt
import skimage 
import numpy as np
################################################
#####

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
    def __init__(self,gr,matrice):
        self.gr=gr
        self.matrice = matrice
    def ass(self,iteration): 
        x=0
        l_f=[]
        for i in self.gr:
            l_f.append([])
        while x<iteration :
            for line in self.matrice:
                for i in line:
                    d=[]
                    ppos=0
                    listd=[]
                    for e in self.gr :
                        d.append(d_min(abs(e.centroid-i.intensite),ppos))
                        listd.append(abs(e.centroid-i.intensite))
                        ppos=ppos+1
                    mini=min(listd)
                    for e in d :
                        if mini==e.distance:
                            self.gr[e.pos].Liste.append(i)
            nb=0
            for i in self.gr :
                l_f[nb]=i.Liste
                i.valmoy()
                i.Liste=[]
                nb=nb+1
            x=x+1
            # print(self.c1.centroid,self.c2.centroid,self.c3.centroid)
        return l_f
        
###############################################
#prout
 text=str(input("Veuillez mettre le nom du ficher : "))
nombregroupe=int(input("Veuillez mettre le nombre de groupe dont vous avez besoin : "))



typee=text.split('.')
if typee[1]=='png':
    contenu = skimage.io.imread(text,as_gray=True)
    matrice= list(list(i) for i in contenu)
else :
    with open(text,'r') as fichier:
        contenu=fichier.read()
    matrice=[[*map(int, line.split())] for line in contenu.split('\n')]

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
    
# pixelmatrice.pop(320)
# pixelmatrice.pop(319)
maxi=max(maxii)

n=0
groupes=[]
while n<nombregroupe:
    groupes.append(groupe([],maxi/(n+1)))
    n=n+1
    

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
# place1_i=[i.pos_i for i in groupe1.Liste]
# place1_j=[j.pos_j for j in groupe1.Liste]
# place2_i=[i.pos_i for i in groupe2.Liste]
# place2_j=[j.pos_j for j in groupe2.Liste]


# plt.plot(place1_j,place1_i,'o',markersize=1,color='black')
# plt.show()
# plt.plot(place2_j,place2_i,'o',markersize=1,color='black')
# plt.show()
