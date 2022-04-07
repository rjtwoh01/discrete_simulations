###
# (1,2)	3.5
# (1,5)	6
# (2,3)	6
# (2,4)	7.5
# (3,4)	6
# (4,7)	4
# (5,3)	7
# (5,4)	9
# (5,6)	8
# (6,7)	9.5
###

import random
import matplotlib.pyplot as plt

x = ['(1,2)', '(1,5)', '(2,3)', '(2,4)', '(3,4)', '(4,7)', '(5,3)', '(5,4)', '(5,6)', '(6,7)']
results = [3.5, 6, 6, 7.5, 6, 4, 7, 9, 8, 9.5]
x_pos = [i for i, _ in enumerate(x)]


plt.bar(x_pos, results)
plt.title('Average distance for paths')
plt.xlabel('Path')
plt.ylabel('Distance')
plt.xticks(x_pos, x)
plt.show()