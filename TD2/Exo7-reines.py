matrice = [ ['N' for i in range(8)] for j in range(8) ]

def afficherMatrice(matrice):
  for elt in matrice:
    print(elt)

def estDisponible(matrice):
  n = len(matrice)
  return [(i, j) for i in range(n) for j in range(n) if matrice[i][j]=='N']

def mettreDame(matrice, coos, num):
    x, y = coos
    matrice[x][y] = num
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if i == x or j == y or abs(i - x) == abs(j - y):
                if matrice[i][j] == 'N':
                    matrice[i][j] = num

def enleverDame(matrice, num):
  for i in range(len(matrice)):
    for j in range(len(matrice)):
      if matrice[i][j] == num:
        matrice[i][j] == 'N'

def estFini(matrice):
  return not any('N' in elt for elt in matrice)
        
def dames(matrice, num=0):
  if estFini(matrice):
    return True

  coosDispos = estDisponible(matrice)
  
  if not coosDispos or num == len(matrice):
    return False
  
  for coos in coosDispos:
    mettreDame(matrice, coos, num)
    res = dames(matrice, num + 1)
    if res:
      return True, matrice
    enleverDame(matrice, num)
    return False, matrice
  
res, resMat = dames(matrice)

afficherMatrice(resMat)