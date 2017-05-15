import os

graphics_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"..","resources", "map"))
redmond_barrens_path = os.path.join(graphics_dir, "RedmondBarrens.png")
from scipy import misc
rb = misc.imread(redmond_barrens_path)

import matplotlib.pyplot as plt
# 7x7 tiles where the first row (index 0 is blank)
plt.imshow(rb)
plt.show()
import pdb; pdb.set_trace()