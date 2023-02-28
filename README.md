# Discrete Laboratory work #1

Work was done by Team 9: Агітольєв Андрій та Сумик Марта

`Task #1.1:`

In this task we will compare Prim and Kruskal algorithms and them with the built-in one.

- So let's first compare Prim and Kruskal algorithms:

1. 20 nodes:

    Prim: 9.243965148925782e-05 seconds;
 
    Kruskal: 0.0001983928680419922 seconds;

2. 100 nodes:

    Prim: 0.0018345427513122559
 
    Kruskal: 0.0036766910552978515
 
3. 500 nodes:

    Prim: 0.09625549793243408 seconds;
 
    Kruskal: 0.13027365922927855 seconds;

3. 1000 nodes:

    Prim: 0.6964262843132019 seconds;
 
    Kruskal: 0.8470808577537536 seconds;
    
And that's graphic that shows time of Prim and Kruskal algorithms on different number of vertices:
    
![](https://drive.google.com/uc?export=view&amp;id=15KvpYM7hWlaEMdfB_9PIAgQMvsQiuDKn)

**So, we can see that for graphs with big amount of vertices Prim algorithm works much more faster, than Kruskal.
For a graph with V vertices E edges, Kruskal's algorithm runs in O(E log V) time and Prim's algorithm can run in O(E + V log V) time.
The main difference is because in Kruskal algorithm we firstly sort the edges, so with small amount of edges or if they are already sorted (or can be sorted in linear time), it will be effective.**



`Task #1.2:`

In this task we will compare our Bellman-Ford and Froyd-Worshall algorithms with the built-in ones.

This plot shows time of running our and built-in **Floyd-Warshall algorithm**.

![](https://drive.google.com/uc?export=view&amp;id=12cfMhp5Pqa6PcYipOZ8wGlFHpKTaM0Yp)

We may see that with number of nodes from 10 to 300 our algorithm is running faster, than built-in.

As there are three main loops, each containing n iterations, the time complexity of this algorithm will be O(n^2).

Comparing a built-in and custom implementations of **Bellman-Ford** algorithm, it can easily be seen that 
custom is much faster, according to the graph below:

<img width="1655" alt="Screenshot 2023-02-28 at 19 59 42" src="https://user-images.githubusercontent.com/44242769/221955483-9fab2973-9d97-4e3d-8ba8-aa0d4c35255d.png">

The time complexity of Bellman-Ford algorithm is O(VxE), where E - number of edges, V - number of vertices.
