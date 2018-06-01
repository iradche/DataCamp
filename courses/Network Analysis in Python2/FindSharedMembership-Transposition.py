/*  As you may have observed, you lose the metadata from a graph when you go to a sparse matrix representation. You're now going to learn how to impute the metadata back so that you can learn more about shared membership.

The user_matrix you computed in the previous exercise has been preloaded into your workspace.

Here, the np.where() function will prove useful. This is what it does: given an array, say, a = [1, 5, 9, 5], if you want to get the indices where the value is equal to 5, you can use idxs = np.where(a == 5). This gives you back an array in a tuple, (array([1, 3]),). To access those indices, you would want to index into the tuple as idxs[0]. */

import numpy as np

# Find out the names of people who were members of the most number of clubs
diag = user_matrix.diagonal()
indices = np.where(diag == diag.max())[0]  
print('Number of clubs: {0}'.format(diag.max()))
print('People with the most number of memberships:')
for i in indices:
    print('- {0}'.format(people_nodes[i]))

# Set the diagonal to zero and convert it to a coordinate matrix format
user_matrix.setdiag(0)
users_coo = user_matrix.tocoo()

# Find pairs of users who shared membership in the most number of clubs
indices = np.where(users_coo.data == users_coo.data.max())[0]
print('People with most number of shared memberships:')
for idx in indices:
    print('- {0}, {1}'.format(people_nodes[users_coo.row[idx]], people_nodes[users_coo.col[idx]]))  
