import matplotlib.pyplot as plt

#los valores de y son 1, 2, 3, 4 que le pasamos en el array. Los valores de x serian sus posiciones 0, 1, 2, 3
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')

#en este caso le pasamos los valores de y
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()
