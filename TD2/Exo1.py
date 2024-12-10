import copy


def creerMatrice():
    matrice = [
        ['0', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', '#', '#', ' ', '#', ' ', '#', '#', '#'],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' '],
        ['#', '#', '#', '#', '#', ' ', '#', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' '],
        ['#', '#', ' ', '#', '#', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '1']
    ]
    return matrice

def printMatrice(matrice):
    for ligne in matrice:
        print(' '.join(ligne))

def chercherChemin(matrice, coos=(0,0), log=[(0,0)]):
    pathMin = []
    x, y = coos
    copyMatrice = copy.deepcopy(matrice)
    if copyMatrice[x][y] == '1':
        return log
    if copyMatrice[x][y] == '.' or copyMatrice[x][y] == '#':
        return pathMin
    
    copyMatrice[x][y] = '.'
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < len(copyMatrice) and 0 <= ny < len(copyMatrice[0]):
            path = chercherChemin(copyMatrice, (nx, ny), log + [(nx, ny)])
            if path and (not pathMin or len(path) < len(pathMin)):
                pathMin = path
    return pathMin
        

if __name__ == "__main__":
    matrice = creerMatrice()
    res = chercherChemin(matrice, (0, 0))
    print(f"Chemin trouvé : {res}, Longueur du chemin : {len(res)}")