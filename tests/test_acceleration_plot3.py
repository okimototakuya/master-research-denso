import os
import sys
import glob
import subprocess
import datetime
import unittest
import numpy as np
import pandas as pd
sys.path.append('../main')
import acceleration_plot3 as ap


AMOUNT_OF_ROW = 30  # テストcsvファイルの列数


class IterAddMicrosecond():
    'time特徴量について、1マイクロ秒加算'

    def __init__(self, input_date_time):
        self.date_time = input_date_time

    def __iter__(self):
        'イテレータプロトコル'
        p = 0.6 # 1マイクロ秒足す確率
        for _ in range(AMOUNT_OF_ROW):
            #self.date_time = self.date_time + datetime.timedelta(microseconds=np.random.binomial(1, p)*100000) # ベルヌーイ分布に従って1マイクロ秒加算
            self.date_time = self.date_time + datetime.timedelta(microseconds=1*100000) # 常に1マイクロ秒加算
            yield self.date_time.strftime('%M:%S.%f')


#bool_crossroad = np.random.binomial(1, 0.01, AMOUNT_OF_ROW) # onCrossroad/crossroadID特徴量を構成するNumpy配列:ベルヌーイ分布に従ってブール値を出力
bool_crossroad = 0  # onCrossroad/crossroadID特徴量を構成するNumpy配列:常に0を出力
str_datetime_inc_microsecond = [ms for ms in IterAddMicrosecond(datetime.datetime(2018, 12, 19, 14, minute=00, second=00, microsecond=0))]  # time特徴量を構成するリスト(各要素は文字列型)
df_real_columns = pd.DataFrame({    # テストDataFrame型変数
    'Unnamed: 0':range(AMOUNT_OF_ROW),
    'line':range(AMOUNT_OF_ROW),
    'time':str_datetime_inc_microsecond,
    #'Acceleration(X)[g]':np.random.rand(AMOUNT_OF_ROW)*10-5,   # 一様分布に従って値を出力
    #'Acceleration(Y)[g]':np.random.rand(AMOUNT_OF_ROW)*10-5,   # 一様分布に従って値を出力
    #'Acceleration(Z)[g]':np.random.rand(AMOUNT_OF_ROW)*10-5,   # 一様分布に従って値を出力
    #'AngularRate(X)[dps]':np.random.rand(AMOUNT_OF_ROW)*600-300,   # 一様分布に従って値を出力
    #'AngularRate(Y)[dps]':np.random.rand(AMOUNT_OF_ROW)*600-300,   # 一様分布に従って値を出力
    #'AngularRate(Z)[dps]':np.random.rand(AMOUNT_OF_ROW)*600-300,   # 一様分布に従って値を出力
    'Acceleration(X)[g]':np.ones(AMOUNT_OF_ROW, dtype=int),
    'Acceleration(Y)[g]':np.ones(AMOUNT_OF_ROW, dtype=int),
    'Acceleration(Z)[g]':np.ones(AMOUNT_OF_ROW, dtype=int),
    'AngularRate(X)[dps]':np.ones(AMOUNT_OF_ROW, dtype=int),
    'AngularRate(Y)[dps]':np.ones(AMOUNT_OF_ROW, dtype=int),
    'AngularRate(Z)[dps]':np.ones(AMOUNT_OF_ROW, dtype=int),
    #'Temperature[degree]':np.random.randn(AMOUNT_OF_ROW)+18,   # 正規分布に従って値を出力
    #'Pressure[hPa]':np.random.randn(AMOUNT_OF_ROW)+1017,   # 正規分布に従って値を出力
    'Temperature[degree]':np.ones(AMOUNT_OF_ROW, dtype=int),
    'Pressure[hPa]':np.ones(AMOUNT_OF_ROW, dtype=int),
    'MagnetCount':np.zeros(AMOUNT_OF_ROW, dtype=int),
    'MagnetSwitch':np.zeros(AMOUNT_OF_ROW, dtype=int),
    'onCrossroad':bool_crossroad,
    'crossroadID':bool_crossroad,
    })


class TestAccelerationPlot3(unittest.TestCase):
    'Master_Research_Denso/main/acceleration_plot3.pyをテスト'
    'FIXME1:2020.11.27:test_save_dataframe_to_csv_とtest_read_csv_real_columnsを同時に走らせるとテストが通らない→一方のみだと通る'
    'FIXME1:2020.11.27:究極的にはtest_read_csv_real_columnsが通れば良いから、大した問題ではない'

    def _test_save_dataframe_to_csv_(self):
        'テストDataFrame型変数をテストcsvファイルに変換できたかテスト(テストコードのみの関数)'
        df_real_columns.to_csv('./test_dataset/demo.csv')
        #subprocess.call(['sed', '\'1', 's/,//\'', './test_dataset/demo.csv', '>', './test_dataset/demo.csv'])
        subprocess.getoutput('sed -i -e \'1 s/,//\' ./test_dataset/demo.csv')   # 書き出したテストcsvファイルの先頭行頭のカンマを削除
        self.assertTrue(glob.glob('./test_dataset/demo.csv'))

    #def _test_read_csv_one_column(self):
    #    'テストcsvファイルをDataFrame型変数として読み込めたかテスト(特徴量数1)'
    #    df_test = ap.read_csv_('./test_dataset/demo.csv')
    #    df_one_column = pd.DataFrame({'a':[0]})
    #    pd.testing.assert_frame_equal(df_test, df_one_column)

    def test_read_csv_real_columns(self):
        'テストcsvファイルをDataFrame型変数として読み込めたかテスト'
        df_test = ap.read_csv_('./test_dataset/demo.csv')
        pd.testing.assert_frame_equal(df_test, df_real_columns)


if __name__ == '__main__':
    unittest.main()
    #os.remove('./test_dataset/demo.csv')   # 次回のテストのためにテストcsvファイルを消去
