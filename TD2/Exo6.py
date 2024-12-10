# objet, prix, poid(kg)

import copy

objets = [
  (1, 4, 5), 
  (2, 4, 7), 
  (3, 3, 2), 
  (4, 3, 2), 
  (5, 5, 6), 
  (6, 5, 8), 
  (7, 3, 3), 
  (8, 3, 4), 
  (9, 5, 9), 
  (10, 6, 11), 
  (11, 5, 8), 
  (12, 5, 7)
]

def sacado(objets, valeur=0, taille=0, log=[]):
  copyObjets = copy.deepcopy(objets)
  maxLog = []
  maxVal = 0
  
  if taille > 15:
    dernierObj = log.pop()
    return valeur-dernierObj[1], log
  
  for obj in copyObjets:
    _, prix, poids = obj
    copyObjets.remove(obj)
    resValeur, resLog = sacado(copyObjets, valeur + prix, taille + poids, log + [obj])
    if resValeur > maxVal:
      maxVal = resValeur
      maxLog = resLog
  return maxVal, maxLog

print(sacado(objets))