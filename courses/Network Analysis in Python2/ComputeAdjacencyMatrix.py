/* Now, you'll get some practice using matrices and sparse matrix multiplication to compute projections! In this exercise, you'll use the matrix multiplication operator @ that was introduced in Python 3.5.

You'll continue working with the American Revolution graph. The two partitions of interest here are 'people' and 'clubs'. */

# Get the list of people and list of clubs from the graph: people_nodes, clubs_nodes
people_nodes = get_nodes_from_partition(G, 'people')
clubs_nodes = get_nodes_from_partition(G, 'clubs')

# Compute the biadjacency matrix: bi_matrix
bi_matrix = nx.bipartite.biadjacency_matrix(G, row_order=people_nodes, column_order=clubs_nodes)

# Compute the user-user projection: user_matrix
user_matrix = bi_matrix @ bi_matrix.T

print(user_matrix)
