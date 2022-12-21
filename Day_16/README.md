# Problem Explaination  
Today's problem was pretty difficult.  
The general idea for the problem is that you are given a graph of nodes, where each node has a pressure associated with it. 
As you traverse the graph, it takes 1 step to move between each node, and another step to release the pressure at the node, 
which will then continue to release for the remainder of steps in the program.  
  
## Part 1
In this section, challenge is to find the path which will release the most pressure in 30 steps. I solved this using the following steps:  
1. Load in the graph data from the text file.  
2. Apply dijkstra's algorithm to each node to determine the minimum steps to reach any other node in the graph.  
3. Perform a depth-first search of all possible paths, using the moves defined by the result of dijkstra's algorithm.  
4. After each step, add the pressure released from the node to the graph's total pressure.  
5. End the branch's search once the number of steps reaches 30, or when we run out of movement options.  
6. Compare the branch's total pressure to a maximum recorded value to determine if a new maximum was reached.  
  
This process worked reasonably well, although it is a bit slow. The program will take a couple of minutes to complete the search.  
  
## Part 2
In this section, the challenge is to find 2 combined paths which will release the most pressure in 26 steps on the same graph. 
Rather than having one operator traversing the graph and releasing pressure, there are 2 operators on the same graph.  
For my solution, I added to the algorithm from part 1 to make this section run a bit faster. These are the steps I added:  
1. When performing the search in part 1, record all paths taken in every step of the search up to 26 steps.
2. Iterate through these paths, looking for 2 paths with no overlap in nodes where pressure was released.
3. For each of these pairs, calculate the pressure released in each graph, add them together, and compare with a maximum value.
  
While this process also takes a few minutes to complete, it is significantly faster than performing another full DFS of a graph with 2 operators moving between nodes.
