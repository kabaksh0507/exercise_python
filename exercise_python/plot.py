"""
This module is plot sample.
"""

import numpy as np
import matplotlib.pyplot as plt

# X座標
x = np.linspace(-np.pi, np.pi)
# Y座標
y = np.sin(x)

# X,Yの読み込み
plt.plot(x, y)
# グラフ表示
plt.show()
