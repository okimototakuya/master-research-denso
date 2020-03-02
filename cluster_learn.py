import numpy as np
import acceleration_plot2 as ap
from sklearn.cluster import KMeans
import pandas as pd

# 予測値を格納する変数
pred = None

def clusterLearn():
	global pred
	# 加速度データのDataFrame型変数を作成.
	acc = ap.DataframeMaker(ap.filename)
	# 確率モデル(Kmeansアルゴリズムの作成.
	model = KMeans(n_clusters = 3)
	# DataFrame型変数から学習に用いる加速度データを抽出.
	X1 = (acc.df).loc[:,'Acceleration_x']
	X1 = pd.DataFrame(X1)
	X2 = (acc.df).loc[:,'AngularRate_x']
	X = X1.join(X2)
	X = np.array(X)		# KMeansの引数はpd.DataFrameではなくnp.array
	model.fit(X)

	#np.set_printoptions(threshold=np.inf)		# 配列の要素を全て表示(状態系列)
	#print("初期確率\n", model.startprob_)
	#print("平均値\n", model.means_)
	#print("共分散値\n", model.covars_)
	#print("遷移確率\n", model.transmat_)
	#print("対数尤度\n", model.score(X))
	pred = model.labels_
	print("状態系列の復号\n", pred)

def main():
	clusterLearn()

if __name__ == '__main__':
	main()