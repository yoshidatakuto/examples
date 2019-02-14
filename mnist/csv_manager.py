import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def write_csv(csvfilename, avg_loss, epoch):
    with open(csvfilename + '.csv', 'a') as f:
        writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
        writer.writerow(str(epoch))     # list（1次元配列）の場合
        writer.writerow(str(avg_loss))     # list（1次元配列）の場合


def view_loss(csvfilename):
    loss_list = pd.read_csv(csvfilename + '.csv')
    # plot learning curve
    plt.figure()
    plt.plot(loss_list, 'r-', label='train_loss')
    plt.xticks(np.arange(-1, 100 , 10))
    plt.legend()
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.grid()
