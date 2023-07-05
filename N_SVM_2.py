import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

xx, yy = np.meshgrid(np.linspace(-3, 3, 500), np.linspace(-3, 3, 500))
np.random.seed(0)
X = np.random.randn(300, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)

clf = svm.NuSVC(gamma='auto')
clf.fit(X,Y)


z = clf.decision_function(np.c_[xx.ravel(),yy.ravel()])
z=z.reshape(xx.shape)

plt.imshow(
    z,
    interpolation="nearest",
    extent=(xx.min(),xx.max(),yy.min(),yy.max()),
    aspect='auto',
    origin='lower',
    cmap=plt.cm.PuOr_r,
)
contours = plt.contour(xx,yy,z,levels=[0])
plt.scatter(X[:,0],X[:,1],s=30,c=Y,cmap=plt.cm.Paired,edgecolors='k')

plt.show()