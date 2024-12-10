import random
import copy

def createGround(width, depth, percent):
    percent = percent / 100
    matrice = []
    for i in range(width):
        matrice.append([' '] * depth)
        for j in range(depth):
            if random.random() < percent:
                matrice[i][j] = 'O'
    return matrice

def printGround(matrice):
    for line in matrice:
        print(' '.join(line))
    print('\n')

def accept(matrice, x, y):
    return matrice[x][y] == ' '

def ajoutEau(matrice, x, y):
    width, depth = len(matrice), len(matrice[0])
    listeFait = []
    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        newX, newY = x + dx, y + dy
        if (0 <= newX < width and 0 <= newY < depth) and matrice[newX][newY] == ' ':
            listeFait.append((newX, newY))
            matrice[newX][newY] = '#'
    return matrice, listeFait

def infiltration(matrice, x, y):
    # copyMatrice = copy.deepcopy(matrice) # si on veut connaitre l'eau rempli pour chaque entrée uniquement
    copyMatrice = matrice # si on veut voir quelles cavités ne peuvent pas être touchées
    queue = [(x, y)]
    while queue:
        actuelX, actuelY = queue.pop()
        copyMatrice[actuelX][actuelY] = '#'
        copyMatrice, listeFait = ajoutEau(copyMatrice, actuelX, actuelY)
        queue += listeFait
    print("Entrée à", (x, y))
    printGround(copyMatrice)

def main():
    width = 10
    depth = 10
    percent = 70
    matrice = createGround(width, depth, percent)
    printGround(matrice)
    
    # Rechercher toutes les infiltrations à partir de toutes les entrées possibles en haut du terrain
    for y in range(depth):
        if matrice[0][y] == ' ':
            infiltration(matrice, 0, y)

if __name__ == '__main__':
    main()