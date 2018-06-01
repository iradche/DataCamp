/* You're now going to practice converting graphs to pandas representation. If you have taken any of DataCamp's pandas courses, you will know that there is a DataFrame.to_csv('filename.csv') method that lets you save it as a CSV file, which is a human-readable version. The main concept we hope you take away from here is the process of converting a graph to a list of records.

Start by re-familiarizing yourself with the graph data structure by calling G.nodes(data=True)[0] in the IPython Shell to examine one node in the graph. */

# Initialize a list to store each edge as a record: nodelist
nodelist = []
for n, d in G_people.nodes(data=True):
    # nodeinfo stores one "record" of data as a dict
    nodeinfo = {'person': n} 
    
    # Update the nodeinfo dictionary 
    nodeinfo.update(d)
    
    # Append the nodeinfo to the node list
    nodelist.append(nodeinfo)
    

# Create a pandas DataFrame of the nodelist: node_df
node_df = pd.DataFrame(nodelist)
print(node_df.head())
