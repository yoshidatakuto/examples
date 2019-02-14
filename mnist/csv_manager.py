import csv
import pandas as pd
import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np


def write_csv(csvfilename, avg_loss_list, epoch_list):
    with open(csvfilename + '.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
        writer.writerow(epoch_list)     # list（1次元配列）の場合
        writer.writerow(avg_loss_list)     # list（1次元配列）の場合


def view_loss(csvfilename):
    print("aaaa")
    loss_list = pd.read_csv(csvfilename + '.csv').T
    print("aa")
    # plot learning curve
    plt.figure()
    plt.plot(loss_list, 'r-', label='train_loss')
    print("bb")
    plt.xticks(np.arange(1, 10 ,1))
    plt.legend()
    print("cc")
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.grid()
    print("dd")
    plt.show()
