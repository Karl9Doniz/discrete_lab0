def measure_time(algorithm, vertices):
    '''
    Measures the time of the algorithm.
    '''
    NUM_OF_ITERATIONS = 2
    time_taken = 0
    for i in tqdm(range(NUM_OF_ITERATIONS)):
        G = gnp_random_connected_graph(vertices, 0.4, False)
        start = time.time()
        algorithm(G)
        end = time.time()
        
        time_taken += end - start

    return time_taken / NUM_OF_ITERATIONS

  
def visualization(algorithm1, algoritm2):
    '''
    Visualizate the time of two given algoritms.
    '''
    vertices = [i for i in range(10, 500, 1)]
    y = []
    time1 = []
    time2 = []
    for i in vertices:
        time1.append(measure_time(algorithm1, i))
        time2.append(measure_time(algoritm2, i))
        y.append(i)
    plt.plot(time1, y, label='Our')
    plt.plot(time2, y, label='Built-in')
    plt.legend()
    return plt.show()
 
