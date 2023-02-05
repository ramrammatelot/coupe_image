import matplotlib.pyplot as plt
import skimage 
################################################
# pif pouf paf
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
            for i in self.gr:
                self.gr[i].Liste=[]
            for l in self.matrice:
                for i in l:
                    d=[]
                    for e in self.gr :
                        d.append(abs(e.centroid-i.intensite))
                    mini=min(d)
                    for e in self.gr :
                        if mini==e.centroid:
                            e.Liste.append(i)
            for i in range(len(self.gr)) :
                l_f[i]=self.gr[i].Liste
                self.gr[i].valmoy()
                self.gr[i].Liste=[]
            # print(self.c1.centroid,self.c2.centroid,self.c3.centroid)
            x=x+1
        return l_f
        
###############################################
#prout
text=str(input("Veuillez mettre le nom du ficher : "))
nombregroupe=int(input("Veuillez mettre le nombre de groupe dont vous avez besoin : "))



typee=text.split('.')
if typee[1]=='png':
    contenu = skimage.io.imread('bretagne.png',as_gray=True)
    matrice= list(list(i) for i in contenu)
else :
    with open(text,'r') as fichier:
        contenu=fichier.read()
    matrice=[[*map(int, line.split())] for line in contenu.split('\n')]

j=0
i=0
pixelmatrice=[]
linepixelmatrice=[]
for e in matrice :
    for a in e :
        linepixelmatrice.append(pixel(a,i,j))
        i=i+1
    j=j+1
    i=0
    linepixelmatrice=[]
    pixelmatrice.append(linepixelmatrice)
    
pixelmatrice.pop(320)
pixelmatrice.pop(319)

n=0
groupes=[]
while n<nombregroupe:
    groupes.append(groupe([],n))
    n=n+1
    

kmean=assignement(groupes, pixelmatrice)
listefinal = kmean.ass(30)
place_i=[]
place_j=[]
for i in listefinal :
    groupes[i].Liste=i
    for e in groupes :
        for p in e.Liste:
            
place1_i=[i.pos_i for i in groupe1.Liste]
place1_j=[j.pos_j for j in groupe1.Liste]
place2_i=[i.pos_i for i in groupe2.Liste]
place2_j=[j.pos_j for j in groupe2.Liste]


plt.plot(place1_j,place1_i,'o',markersize=1,color='black')
plt.show()
plt.plot(place2_j,place2_i,'o',markersize=1,color='black')
plt.show()
