import numpy as np
reseau = [ 
  [0, 7, 3, 0, 0, 0],
  [0, 0, 0, 1, 1, 0],
  [4, 0, 0, 1, 0, 6],
  [0, 2, 0, 0, 4, 0],
  [0, 0, 0, 0, 0, 1],
  [0, 0, 0, 2, 3, 0]
]

#Backtracking 

file=open("graphe.txt")
line=file.readline()
file.close()

Sommets=line[1:].split()

D=Sommets[0]; 
A=Sommets[-1]
dpcc=np.inf                                                      #Distance PCC 
lSpcc=[]
DChemin=0
LSChemin=[D]

def acceptable(ei, e, LS, Dpcc,DChemin):
    global reseau, Sommets 
    inde=Sommets.index(e)
    indei=Sommets.index(ei)
    if (reseau[indei, inde]==0): 
        return(False)
    if (e in LS):
        return(False)
    if ((reseau[indei, inde]+DChemin)>Dpcc):
        return(False)
    else : 
        return(True)
    
#Backtracking labyrinthe 
    
lab = np.loadtxt("laby.txt")
D=(0,0)
A=(lab.shape[0]-1, lab.shape[1]-1) #0 c'est les lignes, 1 c'est les colonnes 
trouve = False 
    
def acceptable_2(lab, e):
    if ((e[0]==-1) or e[0]==lab.shape[0]):
        return(False)
    if ((e[1]==-1) or e[1]==lab.shape[1]):
        return(False)
    if (lab[e]==0):
        return(True)
    else :
        return(False)
        
  
def find_path(lab, D, A, ei): #e = étape 
    global trouve
    if (ei==A) : 
        trouve=True 
        return
    for e in[(ei[0],ei[1]+1),(ei[0]+1,ei[1]),(ei[0],ei[1]-1),(ei[0]-1,ei[1])]:
        if(acceptable_2(lab, e)):
            lab[ei]=1
            find_path(lab, D, A, e)
            if trouve==True:
                return 
            lab[ei]=0
            
        
find_path(lab, D, A, D)
if (trouve==True) : 
    lab[A]=1


bestlab=copy.deepcopy(lab)

def find_best_path(lab, D, A, ei):
    global bestlab
    if (ei==A):
        lgbestlab=len(np.where(bestlab==1)[0])
        lglab=len(np.where(lab==1)[0])
        if lgbestlab>lglab:
            bestlab=copy.deepcopy(lab)
        return 
    for e in[(ei[0],ei[1]+1),(ei[0]+1,ei[1]),(ei[0],ei[1]-1),(ei[0]-1,ei[1])]:
        if (acceptable_2(lab, e)):
            lab[ei]=1
            find_best_path(lab, bestlab, D, A, e)
            lab[ei]=0
            
find_best_path(lab,D, A, D)