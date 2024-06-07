import random
import math
from data import vertices, list_vertices
from graph import Vertex

def generate_random_state_traverse(cities):
    '''Generate a random state'''
    vertices = list(cities.keys())
    random_state = [vertices[0]]
    while True:
        for vertex in vertices:
            adjacent = cities[vertex]
            decision = random.choice(adjacent)
            if decision not in random_state:
                random_state.append(decision)
        if len(random_state) == len(vertices):
            break
    random_state.append(random_state[0])
    return random_state

def distance(state, euclidean = False): 
    '''Calculate the total distance'''
    d = 0
    if euclidean:
        for i in range(len(state) - 1):
            Euclidean = Euclidean_distance(state[i], state[i + 1])
            d += Euclidean
    else:
        for i in range(len(state) - 1):
            Haversine = Haversine_distance(state[i], state[i + 1])
            d += Haversine
    return d

def Haversine_distance(first_vertex, second_vertex):
    '''Calculate Haversine distance'''
    x_lat = math.radians(first_vertex.horizon)
    x_long = math.radians(first_vertex.vertical)
    y_lat = math.radians(second_vertex.horizon)
    y_long = math.radians(second_vertex.vertical)
    r = 6371 #Radius of the Earth
    theta = math.sqrt(math.sin((x_lat - y_lat) / 2)**2 + math.cos(x_lat)*math.cos(y_lat)*(math.sin((x_long - y_long) / 2)**2))

    return 2*r*math.asin(theta)

def Euclidean_distance(first_vertex, sencond_vertex):
    '''Calculate Euclidean distance'''
    x1 = first_vertex.horizon
    y1 = first_vertex.vertical
    x2 = sencond_vertex.horizon
    y2 = sencond_vertex.vertical
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 

def swap_cities(state): #state is a tour
    '''Create neighbor by swapping the position of cities'''
    route = [state[0]]
    sample = random.sample(state[1:len(state)-1],len(state[1:len(state)-1]))
    for x in sample:
        route.append(x)
    route.append(state[0])
    return route   

def get_coordinates(state):
    '''Get x, y coordinates of each vertex in a state'''
    X = []
    y = []
    for vertex in state:
        X.append(vertex.horizon)
        y.append(vertex.vertical)
    return X, y

def simulated_annealing(problem, T_min = 10,  initial_temperature = 10000, iteration_limit = 200, p = 0.99): 
    #p is cooling rate
    '''Return a state in which all cities are visited only once.
    This algorithm picks a random move
    and if that move improves the situation, it is accepted. Otherwise, the algorithm
    accepts the move with some probability less than 1.'''
    #Initial solution
    result = []
    coordinates_X = []
    coordinates_y = []
    total_distance = 0
    best_state = None
    T = 0 
    loop = 0
    while loop >= 0 and loop < iteration_limit:
        current_state = generate_random_state_traverse(problem) #problem is a graph 
        if loop == 0:
            T = initial_temperature
        else:
            if T < T_min:
                return result, coordinates_X, coordinates_y, best_state, total_distance
            else:
                T = T * p
        neighbor_state = swap_cities(current_state)
        delta_e = distance(neighbor_state) - distance(current_state)
        if -delta_e > 0:
            current_state = neighbor_state
            result.append(current_state)
            coordinates_X.append(get_coordinates(current_state)[0])
            coordinates_y.append(get_coordinates(current_state)[1])
        else:
            r = math.exp(-delta_e) / T
            threshold = random.uniform(0, 1)
            if r > threshold:
                current_state = neighbor_state
                result.append(current_state)
                coordinates_X.append(get_coordinates(current_state)[0])
                coordinates_y.append(get_coordinates(current_state)[1])
        loop += 1
    best_state = current_state
    return result, coordinates_X, coordinates_y, best_state



