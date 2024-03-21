import matplotlib.pyplot as plt

plt.plot(x, y, linewidth=2.0)
plt.show()

line, = plt.plot(x, y, '-')
line.set_antialiased(False)         # turn off antialiasing

lines = plt.plot(x1, y1, x2, y2)
# use keyword arguments
plt.setp(lines, color='r', linewidth=2.0)
# or MATLAB style string value pairs
plt.setp(lines, 'color', 'r', 'linewidth', 2.0)