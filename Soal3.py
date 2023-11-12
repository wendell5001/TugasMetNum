# Mengimpor library
from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan fungsi interpolasi_kubik beserta dengan rumus interpolasi kubik
def interpolasi_kubik(x0, y0, x1, y1, x2, y2, b0, b1, b2, x):
    return b0 + b1 * (x - x0) + b2 * (x - x0) * (x - x1)

# Memasukkan titik x0 dan y0
print('Masukkan nilai x0 dan y0')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

# Memasukkan titik x1 dan y1
print('Masukkan nilai x1 dan y1')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))

# Memasukkan titik x2 dan y2
print('Masukkan nilai x2 dan y2')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

# Memasukkan titik x3 dan y3
print('Masukkan nilai x3 dan y3')
x3 = float(input('x3 = '))
y3 = float(input('y3 = '))

# Membaca poin kalkulasi
x = float(input('Masukkan nilai x: '))

# Menghitung koefisien interpolasi kubik
b0 = y0
b1 = (y1 - y0) / (x1 - x0)
c1 = (y2 - y1) / (x2 - x1)
b2 = (c1 - b1) / (x2 - x0)
d1 = (y3 - y2) / (x3 - x2)
c2 = (d1 - c1) / (x3 - x1)
b3 = (c2 - b2) / (x3 - x0)

# Nilai y pada Interpolasi kubik
yp = interpolasi_kubik(x0, y0, x1, y1, x2, y2, b0, b1, b2, x)

# Tampilkan hasil
print('Nilai interpolasi pada titik x %0.4f adalah %0.4f' % (x, yp))

# Membuat Grafik
titik_x = np.array([x0, x1, x, x2, x3])
titik_y = np.array([y0, y1, yp, y2, y3])

X_Y_Spline = interp1d(titik_x, titik_y, kind='cubic')
X_ = np.linspace(titik_x.min(), titik_x.max(), 500)
Y_ = X_Y_Spline(X_)

plt.scatter(titik_x, titik_y, color='black')
plt.plot(X_, Y_)

for i_x, i_y in zip(titik_x, titik_y):
    plt.text(i_x + 0.2, i_y, '({}, {})'.format(i_x, i_y))

plt.show()