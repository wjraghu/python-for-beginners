import matplotlib.pyplot as plt
import numpy as np

# Data
dimensions = ['Racial', 'Gender', 'Functional', 'Hierarchical']
current = [47, 13, 33, 33]
desired = [60, 50, 50, 60]

# Set up bar positions
x = np.arange(len(dimensions))
width = 0.35

# Create the plot
fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, current, width, label='Current Diversity', color='skyblue')
bars2 = ax.bar(x + width/2, desired, width, label='Desired Diversity', color='orange')

# Add labels and title
ax.set_xlabel('Diversity Dimensions')
ax.set_ylabel('Diversity Percentage (%)')
ax.set_title('Network Diversity: Current vs. Desired')
ax.set_xticks(x)
ax.set_xticklabels(dimensions)
ax.legend()

# Add value labels on top of bars
for bar in bars1:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height, f'{height}%', ha='center', va='bottom')
for bar in bars2:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height, f'{height}%', ha='center', va='bottom')

# Adjust layout and display
plt.tight_layout()
plt.show()
