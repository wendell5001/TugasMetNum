# Mengimpor library numpy dan matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Membuat fungsi dengan nama interpolasi linear
def interpolasi_linear(x0, y0, x1, y1, x):
    return y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)

# Memasukkan titik x0 dan y0
print('Masukkan nilai x0 dan y0')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

# Memasukkan titik x1 dan y1
print('Masukkan nilai x1 dan y1')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))

# Membaca poin kalkulasi
x = float(input('Masukkan nilai x: '))

# Kalkulasi interpolasi linear
yp = interpolasi_linear(x0, y0, x1, y1, x)

# Tampilkan hasil
print('Nilai interpolasi pada titik x %0.4f adalah %0.4f' % (x, yp))

x_ = np.array([x0, x, x1])
y_ = np.array([y0, yp, y1])

plt.scatter(x_, y_, color="black")
plt.plot(x_, y_, color="black")

for i_x, i_y in zip(x_, y_):
    plt.text(i_x + 0.2, i_y, '({}, {})'.format(i_x, i_y))

plt.show()