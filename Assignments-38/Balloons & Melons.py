import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

balloon_length = np.random.normal(30, 2, 100)
balloon_width = np.random.normal(25, 2, 100)
balloon_weight = np.random.normal(50, 10, 100)

melon_length = np.random.normal(28, 2, 100)
melon_width = np.random.normal(26, 2, 100)
melon_weight = np.random.normal(40, 10, 100)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(balloon_length, balloon_width, balloon_weight, c='tab:blue', label='Balloons', marker='o')
ax.scatter(melon_length, melon_width, melon_weight, c='tab:orange', label='Melons', marker='^')

ax.set_xlabel('Length')
ax.set_ylabel('Width')
ax.set_zlabel('Weight')
ax.set_title('3D Scatter Plot of Balloons and Melons')
ax.legend()
plt.show()