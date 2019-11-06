import csv
import matplotlib.pyplot as plt

x = []  # $B%0%i%U$N2#<4(B($B@0?tCM(B)
y = []  # $B%0%i%U$N=D<4(B
EVAR = 0  # $B@0?tCM(B
#EVAR = 1  # $B;~9o(B
#TBAR = 2  # $B1tD>J}8~$N2CB.EY(B($B>e$,(B+)
#TBAR = 3  # $BA08eJ}8~$N2CB.EY(B($BA0$,(B+)
#TBAR = 4  # $B:81&J}8~$N2CB.EY(B($B1&$,(B+)
TBAR = 5  # $B:81&2sE>$N3QB.EY(B($B1&$,(B+)
#TBAR = 6  # $BB&J}2sE>$N3QB.EY(B($B1&<jB&$X$N2sE>$,(B+)
#TBAR = 7  # $BA0798e79$N3QB.EY(B($B8e79$,(B+)


with open("./LOG_20181219141837_00010533_0021002B401733434E45.csv") as f:

  reader = csv.reader(f)

  i = 0
  for row in reader:
    i = i + 1
    if i <= 3:
      pass
    else:
      if EVAR == 0:
        x.append(int(row[EVAR]))
      else:
        x.append(row[EVAR])
      y.append(float(row[TBAR]))

plt.plot(x,y)
plt.show()
