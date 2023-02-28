# Discrete Laboratory work #1

`Task #1:`

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



`Task #2:`

In this task we will compare our Bellman-Forn and Froyd-Worshall algorithms with the built-in ones.

This plot shows time of running our and built-in Floyd-Warshall algorithm.
![](https://drive.google.com/uc?export=view&amp;id=1kIfn1CmpPf-4sbKhJ88Hylqskm5DAwjCCavE6ijaoJs)


