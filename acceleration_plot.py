import pandas as pd
import matplotlib
matplotlib.use('Agg')		# pyplotで生成した画像を保存するためのインポート
import matplotlib.pyplot as plt
import os
import hmm_learn
import cluster_learn
import numpy as np
import sys

class dataframe_maker():
	#df = None # DataFrame型インスタンスを格納

	def __init__(self, filename):
		# 列名を明示的に指定することにより, 欠損値をNaNで補完.
		col_names = ['line', 'time',
						'Acceleration_x', 'Acceleration_y', 'Acceleration_z',
						'AngularRate_x', 'AngularRate_y', 'AngularRate_z', 'Temperture', 'Pressure', 'MagnetCount', 'MagnetSwitch',
						]
		self.df = pd.read_csv(filename,
									names=col_names,
									skiprows=3,
									parse_dates=['time'],
									index_col=0, # 0:整数値, 1:時刻
									converters={'line':int, 'time':str,
													'Acceleration_x':float, 'Acceleration_y':float, 'Acceleration_z':float,
													'AngularRate_x':float, 'AngularRate_y':float, 'AngularRate_z':float,
													'Temperture':float, 'Pressure':float, 'MagnetCount':int, 'MagnetSwitch':int,
													}
									)

class dataframe_plotter():
	def plotTimeAccAng(self, df, delta, *args):
		global pred
		predict = pd.DataFrame(pred, columns=['pred'])
		df = pd.concat([df[list(args)], predict], axis=1)

		## 加速度・角速度の時系列変化をプロット
		for i in range(int(len(df)/delta)):
			copy_df = df.loc[delta*i:delta*(i+1), :]
			copy_df.dropna(how='all')
			ax = copy_df.plot(secondary_y=['pred'])
			ax.set_title(filename)
			#plt.show()
			plt.savefig(os.path.join(PATH, "demo"+str(i)+".png"))


def main():
	global pred
	global PATH
	global filename

	if sys.argv[1] == '0':		# 隠れマルコフモデル
		#np.set_printoptions(threshold=np.inf)		# 配列の要素を全て表示(状態系列)
		PATH = PATH + "hmm加速度・角加速度の時系列変化プロット"
		pred = hmm_learn.getPred()
	elif sys.argv[1] == '1':		# クラスタリング
		#np.set_printoptions(threshold=np.inf)		# 配列の要素を全て表示(状態系列)
		PATH = PATH + "cluster加速度・角加速度の時系列変化プロット"
		pred = cluster_learn.getPred()
	else:
		print("Error is here.")

	dm = dataframe_maker(filename)
	dm.init()
	dp = dataframe_plotter()
	#dp.plotTimeAcc(dm.df)
	#dp.plotTimeAng(dm.df)
	dp.plotTimeAccAng(dm.df, 250, 'Acceleration_x', 'AngularRate_x')
	#dp.plotTimeAccAng(dm.df, 250, 1, 4)

if __name__ == '__main__':
## 予測値を取得する変数
	pred = None
## 画像ファイルの保存先
	PATH = "/Users/okimototakuya/Library/Mobile Documents/com~apple~CloudDocs/Documents/研究/M1/研究データ/サンプル2件/"
## ID16
# ファイル名
	filename = "dataset/LOG_20181219141837_00010533_0021002B401733434E45.csv"
## ID19
# ファイル名
	#filename = "dataset/LOG_20181219141901_00007140_00140064401733434E45.csv"

	main()
