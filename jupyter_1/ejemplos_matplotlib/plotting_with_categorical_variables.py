import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

#tamaño total de la figura 900px x 300px
plt.figure(figsize=(9, 3))

# la subgrafica ocupa el alto total de la figura (1),
# ocupa un tercio del ancho total de la figura (3),
# y está en el la posición 1 de la subdivisión horizontal de la figura (1)
plt.subplot(131)
# hace la subgrafica usando barras a partir de names y values
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
# titulo superior de la figura
plt.suptitle('Categorical Plotting')
plt.show()
