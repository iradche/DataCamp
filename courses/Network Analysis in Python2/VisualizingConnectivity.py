/* Here, you're going to visualize how the connectivity of the top connected nodes changes over time. The list of top connected values, top_connected, from the previous exercise has been loaded.

Remember the defaultdict you used in Chapter 1? You'll use another defaultdict in this exercise! As Eric mentioned in the video, a defaultdict is preferred here as a regular Python dictionary would throw a KeyError if you try to get an item with a key that is not currently in the dictionary.

This exercise will make use of nested for loops. That is, you'll use one for loop inside another. */

# Import necessary modules
import matplotlib.pyplot as plt
from collections import defaultdict

# Create a defaultdict in which the keys are nodes and the values are a list of connectivity scores over time
connectivity = defaultdict(list)
for n in top_connected:
    for g in Gs:
        connectivity[n].append(len(g.neighbors(n)))

# Plot the connectivity for each node
fig = plt.figure() 
for n, conn in connectivity.items(): 
    plt.plot(conn, label=n) 
plt.legend()  
plt.show()
