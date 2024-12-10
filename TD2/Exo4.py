import copy


matrice = [
  [0, 7, 3, 0, 0, 0],
  [0, 0, 0, 1, 1, 0],
  [4, 0, 0, 1, 0, 6],
  [0, 2, 0, 0, 4, 0],
  [0, 0, 0, 0, 0, 1],
  [0, 0, 0, 2, 3, 0]
]

def trouverLiaison(matrice, ls, point, cheminAssocie, poid):
  liaisons = []
  for i in range(len(matrice[point])):
    if matrice[point][i] != 0 and i not in ls:
      nouvelleLiaison = (i, cheminAssocie + [i], poid + matrice[point][i])
      liaisons.append(nouvelleLiaison)
  return liaisons

def chemin(matrice, pointD, pointA):
  cpMatrice = copy.deepcopy(matrice)
  queue = [(pointD, [pointD], 0)]
  ls = []
  chemins = []
  
  while queue:
    if pointA not in [elt[0] for elt in queue]:
      actuelPoint, cheminAssocie, poid = queue.pop()
      ls.append(actuelPoint)
      queue += trouverLiaison(cpMatrice, ls, actuelPoint, cheminAssocie, poid)
    else:
      for elt in queue:
        if elt[0] == pointA:
          chemins.append(elt)
          queue.remove(elt)
  return chemins
    
print(chemin(matrice, 0, 4))