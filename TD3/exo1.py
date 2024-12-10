import random

##############
# exercice 1 #
##############

# individu aléatoire
def create_individual():
    rand_list=[]
    for i in range(8):
        rand_list.append(random.randint(1,8))
    return rand_list


# initialisation population
def initialize_population(pop_size):
    population = [create_individual() for _ in range(pop_size)]
    return population


# fonction de fitness
def fitness(individual):
    conflicts = 0

    # diagonales
    for i in range(1, 8):
        for j in range(i + 1, 9):
            if abs(i - j) == abs(individual[i-1] - individual[j-1]) :
                conflicts += 1 
    
    # colonnes
    seen = []
    for num in individual:
        if num not in seen:
            count = individual.count(num)
            if count > 1:
                conflicts += count - 1
            seen.append(num)
    
    return conflicts


# fonction de sélection
def tournament_selection(population, tournament_size):
    tournament = random.sample(population, tournament_size)
    tournament.sort(key=lambda x: fitness(x))
    return tournament[0]


# fonction de mutation
def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        i = random.randint(0, 7)
        
        if individual[i] == 8: # ne pas sortir de l'échiquier
            individual[i] -= 1
        elif individual[i] == 1:
            individual[i] += 1
        else:
            if random.randint(0, 1): # incrémenter ou décrémenter au hasard
                individual[i] += 1
            else:
                individual[i] -= 1
    
    return individual

# fonction de croisement
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)  # point de croisement aléatoire
    
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    
    return child1, child2


# algorithme complet
pop_size = 100
max_generations = 100
mutation_rate = 0.02
tournament_size = 25

solution = None

population = initialize_population(pop_size)

for generation in range(max_generations):
    # si la meilleure solution a un fitness de 0, nous avons trouvé la solution
    population.sort(key=lambda x: fitness(x))
    if fitness(population[0]) == 0:
        print(f"Solution trouvée dans la génération {generation}: {population[0]}")
        solution = population[0]
        break
    
    print(f"Meilleur fitness pour la génération {generation} = {fitness(population[0])}")

    # sélection naturelle : la meilleure moitié de la population survit
    new_population = population[:pop_size // 2]

    # croisements remplissent la nouvelle génération
    while len(new_population) < pop_size:
        parent1 = tournament_selection(population, tournament_size)
        parent2 = tournament_selection(population, tournament_size)
        
        # croisement
        child1, child2 = crossover(parent1, parent2)
        # mutations
        child1 = mutate(child1, mutation_rate)
        child2 = mutate(child2, mutation_rate)
                    
        new_population.extend([child1, child2])
    
    population = new_population

if not solution :
    print(f"Solution non trouvée après {max_generations} générations")


# visualisation
def afficher_echiquier_ascii(solution):
    # créer un échiquier vide de 8x8
    echiquier = [['.' for _ in range(8)] for _ in range(8)]
    
    # placer les dames sur l'échiquier selon les positions de la solution
    for ligne, colonne in enumerate(solution):
        echiquier[ligne][colonne-1] = 'X'

    # afficher l'échiquier
    for ligne in echiquier:
        print(' '.join(ligne))

if solution :
    afficher_echiquier_ascii(solution)
