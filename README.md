### サンプルデータの読み方


######
# location.csv (位置情報)
# LOG.txt (加速度・角速度情報)
######

### LOG.txt
## 加速度(Acceleration)
######
# x鉛直(上が+)
# y前後(前が+)
# z左右(右が+)
######

## 角速度(AngularRate)
######
# xヨー   左右回転(右が+)
# yロール 側方回転(右手側への回転が+)
# zピッチ 前傾後傾(後傾が+)
######


### location.csv
## 時刻 (recvData)
# 刻み幅バラバラ
# 時々１〜数時間とぶ
# グラフ:緯度経度一定の区間があったので, そこは多分学校にいる


### 時系列データ
## LOG_20181219141837_00010533_0021002B401733434E45.csv (サンプルID16)
# サンプル0(最初)~45000 : 約1時間
# サンプル45001~90000 : 約1時間(計2時間)
# サンプル90001~131663(最後) : 約1時間(55分33秒)(計3時間)

# 7~8万点：約13分(帰り道全部)