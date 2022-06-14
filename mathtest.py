import matplotlib.pyplot as plt

x = [0, 1, 2, 3]

x_accel = [5, 6, 3, 4]
y_accel = [2, 7, 6, 8]
z_accel = [1, 2, 3, 4]


plt.subplot(3, 1, 1)
plt.subplot(3, 1, 2)
plt.subplot(3, 1, 3)
plt.show()

plt.pause(3.05)
plt.plot(x, x_accel, '.-')
plt.pause(2.05)
plt.title('A tale of 3 subplots')
plt.ylabel('X acceleration')


plt.plot(x, y_accel, '.-')
plt.pause(2.05)
plt.xlabel('time (s)')
plt.ylabel('Y acceleration')


plt.plot(x, z_accel, '.-')
plt.pause(2.05)
plt.xlabel('time (s)')
plt.ylabel('Z acceleration')

