##############
# exercice 2 #
##############
import random

# structure de données
distances = {
    "Berlin": {"Madrid": 2320, "Rome": 1507, "Paris": 1050, "Vienne": 640, "Hambourg": 290, "Varsovie": 575, "Bucarest": 100, "Budapest": 200, "Barcelone": 200},
    "Madrid": {"Berlin": 2320, "Rome": 1962, "Paris": 1278, "Vienne": 200, "Hambourg": 100, "Varsovie": 200, "Bucarest": 100, "Budapest": 200, "Barcelone": 200},
    "Rome": {"Berlin": 1507, "Madrid": 1962, "Paris": 1461, "Vienne": 200, "Hambourg": 100, "Varsovie": 200, "Bucarest": 100, "Budapest": 200, "Barcelone": 200},
    "Paris": {"Berlin": 1050, "Madrid": 1278, "Rome": 1461, "Vienne": 200, "Hambourg": 100, "Varsovie": 200, "Bucarest": 100, "Budapest": 200, "Barcelone": 200},
    "Vienne": {"Berlin": 640, "Madrid": 2382, "Rome": 1124, "Paris": 1235, "Hambourg": 990, "Varsovie": 672, "Bucarest": 1070, "Budapest": 244, "Barcelone": 1777},
    "Hambourg": {"Berlin": 290, "Madrid": 2173, "Rome": 1687, "Paris": 907, "Vienne": 990, "Varsovie": 853, "Bucarest": 1982, "Budapest": 1156, "Barcelone": 1787},
    "Varsovie": {"Berlin": 575, "Madrid": 2925, "Rome": 1787, "Paris": 1597, "Vienne": 672, "Hambourg": 853, "Bucarest": 1395, "Budapest": 858, "Barcelone": 2349},
    "Bucarest": {"Berlin": 1698, "Madrid": 3347, "Rome": 2040, "Paris": 2310, "Vienne": 1070, "Hambourg": 1982, "Varsovie": 1395, "Budapest": 836, "Barcelone": 2748},
    "Budapest": {"Berlin": 873, "Madrid": 2525, "Rome": 1218, "Paris": 1484, "Vienne": 244, "Hambourg": 1156, "Varsovie": 858, "Bucarest": 836, "Barcelone": 1923},
    "Barcelone": {"Berlin": 1882, "Madrid": 627, "Rome": 1343, "Paris": 1035, "Vienne": 1777, "Hambourg": 1787, "Varsovie": 2349, "Bucarest": 2748, "Budapest": 1923}
}


# distance entre 2 villes
def distance(ville1, ville2):
    return distances[ville1][ville2]


# initialisation population
def initialize_population(pop_size):
    population = [random.sample(['Berlin', 'Madrid', 'Rome', 'Paris', 'Vienne', 'Hambourg', 'Varsovie', 'Bucarest', 'Budapest', 'Barcelone'], 10) for _ in range(pop_size)]
    return population


# fonction de fitness
def fitness(individual):
    dist = 0
    
    trajets = [[individual[i], individual[(i+1) % len(individual)]] for i in range(len(individual))]

    for i in trajets :
        dist += distance(i[0], i[1])
    
    return dist


# fonction de sélection
def tournament_selection(population, tournament_size):
    tournament = random.sample(population, tournament_size)
    tournament.sort(key=lambda x: fitness(x))
    return tournament[0]


# fonction de mutation
def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(individual)), 2) # 2 indexes au hasard
        
        individual[i], individual[j] = individual[j], individual[i] # échange
    
    return individual


# fonction de croisement
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)  # point de croisement aléatoire
    
    child1 = parent1[:point]
    child1 += [city for city in parent2 if city not in child1]
    
    child2 = parent2[:point]
    child2 += [city for city in parent1 if city not in child2]
    
    return child1, child2


# algorithme complet
pop_size = 200
max_generations = 100
mutation_rate = 0.02
tournament_size = 25

population = initialize_population(pop_size)

population.sort(key=lambda x: fitness(x))
solution = population[0]
generation_solution = 0

for generation in range(max_generations):
    # mise à jour de la meilleure solution
    population.sort(key=lambda x: fitness(x))
    if fitness(population[0]) < fitness(solution):
        solution = population[0]
        generation_solution = generation
        
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

print(f"Meilleure solution trouvée : {solution}, de {fitness(solution)} km, trouvée à la génération {generation_solution}")
