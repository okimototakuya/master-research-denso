import csv
import matplotlib.pyplot as plt

x = []  # $B%0%i%U$N2#<4(B($B@0?tCM(B)
y = []  # $B%0%i%U$N=D<4(B

with open("./LOG_20181219141837_00010533_0021002B401733434E45.csv") as f:
  #print(f.read())

  reader = csv.reader(f)
  #del reader[:3]

  for row in reader:
    #print(row[0])
    x.append(row[0])
    y.append(row[2])
  del x[:3]
  del y[:3]
  print(y)
