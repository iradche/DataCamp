/* You're now going to get some practice plotting other evolving graph statistics. We'll start with a simpler exercise to kick things off. First off, plot the number of edges over time.

To do this, you'll create a list of the number of edges per month. The index of this list will correspond to the months elapsed since the first month. */

# Import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()

# Create a list of the number of edges per month
edge_sizes = [len(g.edges()) for g in Gs]

# Plot edge sizes over time
plt.plot(edge_sizes)
plt.xlabel('Time elapsed from first month (in months).') 
plt.ylabel('Number of edges')                           
plt.show() 
