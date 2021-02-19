from random import random
from simulated_annealing import SimAnneal
import numpy as np


def tsp_read(nodes):
    infile = open(nodes, 'r')
    content = infile.readline().strip().split()
    print("File Name: ", content[2])

    while content[0] != 'NODE_COORD_SECTION':
        if(content[0] == 'DIMENSION'):
            dimension = content[2]
        content = infile.readline().strip().split()
    nodelist = []
    placelist = []
    print('Dimension', dimension)
    N = int(dimension)
    for i in range(0, N):
        x, y, z = infile.readline().strip().split()[:]
        nodelist.append([float(y), float(z)])
        placelist.append(x)

    # Close input file
    infile.close()
    return nodelist, placelist


def main():
    # generate_random_coords(100)
    nodes, place = tsp_read("Data/rajasthan.tsp")
    coords = np.random.randint(10, size=(10, 3))
    coords = np.array(nodes)
    n = len(coords)
    sa = SimAnneal(coords, place,stopping_iter=n*10000000)
    sa.simulated_annealing()
    sa.displace_optimal_path()
    sa.animateSolutions()
    sa.plot_learning()


if __name__ == "__main__":
    main()
