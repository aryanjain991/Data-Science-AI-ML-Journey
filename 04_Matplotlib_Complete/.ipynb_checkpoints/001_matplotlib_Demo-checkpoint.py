import matplotlib.pyplot as plt
# 001
#plt.plot([1, 2, 3], [4, 5, 6])
#plt.show()

# 002
# import numpy as np

# plt.plot(np.random.rand(100), linewidth=1)

# plt.title("Too Much Data Can Be Confusing!")
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# 003
import numpy as np

for i in range(3):
    
    plt.plot(np.random.rand(100), linewidth=1)
    
plt.title("Too Much Data Can Be Confusing!")
plt.grid(True)
plt.tight_layout()
plt.show()

