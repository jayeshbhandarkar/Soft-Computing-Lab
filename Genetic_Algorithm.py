import random
import string

# Target string
TARGET = "HELLO GENETIC ALGORITHM"

# Parameters
POPULATION_SIZE = 100
MUTATION_RATE = 0.01
GENERATIONS = 20

# Fitness function: how close is the string to the target?
def calculate_fitness(individual):
    return sum(1 for i, j in zip(individual, TARGET) if i == j)

# Generate a random individual (string)
def create_individual(length):
    return ''.join(random.choice(string.ascii_uppercase + ' ') for _ in range(length))

# Create the initial population
def create_population(size, target_length):
    return [create_individual(target_length) for _ in range(size)]

# Select individuals based on fitness
def selection(population, fitness_scores):
    selected = random.choices(population, weights=fitness_scores, k=2)
    return selected[0], selected[1]

# Crossover: combine two parents to produce a child
def crossover(parent1, parent2):
    pivot = random.randint(0, len(parent1) - 1)
    return parent1[:pivot] + parent2[pivot:]

# Mutation: randomly alter genes in the child
def mutate(individual, mutation_rate):
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.choice(string.ascii_uppercase + ' ')
    return ''.join(individual)

# Main Genetic Algorithm loop
def genetic_algorithm():
    population = create_population(POPULATION_SIZE, len(TARGET))
    
    for generation in range(GENERATIONS):
        # Calculate fitness for each individual
        fitness_scores = [calculate_fitness(individual) for individual in population]
        
        # Check if we've found the target string
        if max(fitness_scores) == len(TARGET):
            best_match = population[fitness_scores.index(max(fitness_scores))]
            print(f"Target reached in {generation} generations: {best_match}")
            break
        
        # Create new population
        new_population = []
        for _ in range(POPULATION_SIZE):
            # Select two parents
            parent1, parent2 = selection(population, fitness_scores)
            # Crossover to produce a child
            child = crossover(parent1, parent2)
            # Mutate the child
            child = mutate(child, MUTATION_RATE)
            new_population.append(child)
        
        # Replace the old population with the new one
        population = new_population
        
        # Print best result of the current generation
        best_match = population[fitness_scores.index(max(fitness_scores))]
        print(f"Generation {generation}, Best Match: {best_match}")

# Run the Genetic Algorithm
genetic_algorithm()
