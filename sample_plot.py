import csv
import matplotlib.pyplot as plt

x = []  # $B%0%i%U$N2#<4(B($B@0?tCM(B)

with open("./LOG_20181219141837_00010533_0021002B401733434E45.csv") as f:
  #print(f.read())

  reader = csv.reader(f)
  #del reader[:3]

  for row in reader:
    #print(row[0])
    x.append(row[0])
  del x[:3]
