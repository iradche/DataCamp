/* Great work with the previous exercise - you had written code that created the time-series graph list. Now, you're going to finish that exercise - that is, you'll find out how many forums had the most popular forum score on a per-day basis!

One of the things you will be doing here is a "dictionary comprehension" to filter a dictionary. It is very similar to a list comprehension to filter a list, except the syntax looks like: {key: val for key, val in dict.items() if ...}. Keep that in mind! */

# Import necessary modules
from datetime import timedelta
import networkx as nx
import matplotlib.pyplot as plt

most_popular_forums = []
highest_dcs = []
curr_day = dayone 
td = timedelta(days=1)  

while curr_day < lastday:  
    if curr_day.day == 1:  
        print(curr_day)  
    G_sub = nx.Graph()
    G_sub.add_nodes_from(G.nodes(data=True))   
    G_sub.add_edges_from([(u, v, d) for u, v, d in G.edges(data=True) if d['date'] >= curr_day and d['date'] < curr_day + td])
    
    # Get the degree centrality 
    dc = ____
    # Filter the dictionary such that there's only forum degree centralities
    forum_dcs = {____:____ for ____, ____ in ____ if n in ____}
    # Identify the most popular forum(s) 
    most_popular_forum = [n for n, dc in ____ if dc == ____(____) and dc != 0] 
    most_popular_forums.append(most_popular_forum) 
    # Store the highest dc values in highest_dcs
    highest_dcs.append(max(____))
    
    curr_day += td  
    
plt.figure(1) 
plt.plot([len(____) for ____ in ____], color='blue', label='Forums')
plt.ylabel('Number of Most Popular Forums')
plt.show()

plt.figure(2)
plt.plot(____, color='orange', label='DC Score')
plt.ylabel('Top Degree Centrality Score')
plt.show()
