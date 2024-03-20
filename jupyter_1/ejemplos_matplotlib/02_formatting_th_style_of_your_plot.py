import matplotlib.pyplot as plt
import numpy as np

# 'ro' formatea el estilo a puntos rojos si ponemos solo 'r' seria una linea roja. la primera letra es el color puede ser
# c,y,k,b,g,r si quitamos la 'o' seria una linea
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis((0, 6, 0, 20))
plt.show()


# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()