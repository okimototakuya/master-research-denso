import csv
import matplotlib.pyplot as plt

x = []  # $B%0%i%U$N2#<4(B($B@0?tCM(B)
y = []  # $B%0%i%U$N=D<4(B

with open("./LOG_20181219141837_00010533_0021002B401733434E45.csv") as f:

  reader = csv.reader(f)

  i = 0
  for row in reader:
    i = i + 1
    if i <= 3:
      pass
    else:
      x.append(int(row[0]))
      y.append(float(row[2]))

plt.plot(x,y)
plt.show()
