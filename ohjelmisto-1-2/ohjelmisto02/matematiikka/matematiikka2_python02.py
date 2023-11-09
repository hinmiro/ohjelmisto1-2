import numpy as np
from matplotlib import patches
import matplotlib.pyplot as plt

X = np.linspace(-np.pi * 3, 3 * np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
plt.figure(figsize=(19, 5))

plt.plot(X, C, color="cyan", linestyle="-.", label="Cosine")
plt.plot(X, S, color="darkcyan", linestyle="dashed", label="Sine")

plt.legend(loc='upper left', frameon=False)

plt.xticks([-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
           [r'$-2\pi$', r'$-3\pi/2$', r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$', r'$+3\pi/2$',
            r'$2\pi$'])

plt.yticks([-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
           [r'$-2\pi$', r'$-3\pi/2$', r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$', r'$+3\pi/2$',
            r'$2\pi$'])

plt.show()

fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

pist_xy = np.array([np.pi / 6, np.pi / 4, np.pi / 3, np.pi / 2, 2 * np.pi / 3, 5 * np.pi / 6, np.pi, 3 * np.pi / 2])

x = np.cos(pist_xy)
y = np.sin(pist_xy)

plt.scatter(x, y, marker='X')

plt.annotate(r'$(\frac{\pi}{6})$',
             xy=(np.cos(np.pi / 6), np.sin(np.pi / 6)), xycoords='data',
             xytext=(+30, +0), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

plt.annotate(r'$(\frac{\pi}{4})$',
             xy=(np.cos(np.pi / 4), np.sin(np.pi / 4)), xycoords='data',
             xytext=(+30, +0), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

plt.annotate(r'$(\frac{\pi}{3})$',
             xy=(np.cos(np.pi / 3), np.sin(np.pi / 3)), xycoords='data',
             xytext=(+30, +0), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

plt.annotate(r'$(\frac{\pi}{2})$',
             xy=(np.cos(np.pi / 2), np.sin(np.pi / 2)), xycoords='data',
             xytext=(+30, +10), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

plt.annotate(r'$(\frac{2\pi}{3})$',
             xy=(np.cos(2 * np.pi / 3), np.sin(2 * np.pi / 3)), xycoords='data',
             xytext=(-50, +0), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

plt.annotate(r'$(\frac{5\pi}{6})$',
             xy=(np.cos(5 * np.pi / 6), np.sin(5 * np.pi / 6)), xycoords='data',
             xytext=(-50, +0), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

plt.annotate(r'$(\pi)$',
             xy=(np.cos(np.pi), np.sin(np.pi)), xycoords='data',
             xytext=(-50, +5), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

plt.annotate(r'$(\frac{3\pi}{2})$',
             xy=(np.cos(3 * np.pi / 2), np.sin(3 * np.pi / 2)), xycoords='data',
             xytext=(+0, -30), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))
plt.show()
