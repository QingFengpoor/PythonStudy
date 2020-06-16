#!/usr/bin/python3
#encoding: utf-8
'''
@File    :   histograms_2d.py
@Time    :   2020/06/16 13:28:48
@Author  :   Qingfeng 
@Version :   1.0
@Contact :   2267647906@qq.com
'''

# use Qt5Agg
import matplotlib
matplotlib.use("Qt5Agg")
# libraries
import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np

def histograms_2d(): 
    # create data
    x = np.random.normal(size=50000)
    y = x * 3 + np.random.normal(size=50000)
    
    # figure 1
    fig = plt.figure(figsize=(5, 5), constrained_layout=True)
    fig.canvas.set_window_title("Basic histograms(different bins)")
    gs = fig.add_gridspec(2, 2)
    # to make the bin be square when bins-x = bins-y, make the figure be square first.
    # Big bins
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.hist2d(x, y, bins=(50, 50), cmap=plt.cm.jet)
    ax1.set_title("Big bins")
    # how to make axes be suqare?
    # pos = list(ax1.get_position().bounds)
    # print(pos)
    # pos[-2] = pos[-1]
    # print(pos)
    # ax1.set_position(pos)  #  why this make the axes disappear
    # print(ax1.get_position().bounds)
    # # plt.show()
    
    # Small bins
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.hist2d(x, y, bins=(300, 300), cmap=plt.cm.jet)
    ax2.set_title("Small bins")
    #plt.show()
    
    # If you do not set the same values for X and Y, the bins aren't square !
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.hist2d(x, y, bins=(300, 30), cmap=plt.cm.jet)
    ax3.set_title("rectangle bins")

    plt.show()
    plt.close()

    # figure 2
    fig = plt.figure(constrained_layout=True)
    fig.canvas.set_window_title("different color")
    gs = fig.add_gridspec(1, 2)

    ax1 = fig.add_subplot(gs[0, 0])
    # Reds
    ax1.hist2d(x, y, bins=(50, 50), cmap=plt.cm.Reds)
    ax1.set_title("Reds")

    ax2 = fig.add_subplot(gs[0, 1])
    # BuPu
    ax2.hist2d(x, y, bins=(50, 50), cmap=plt.cm.BuPu)
    ax2.set_title("BuPu")

    plt.show()
    plt.close()

    # figure 3
    fig, ax = plt.subplots()
    fig.canvas.set_window_title("add color bar")

    # plt.hist2d(x, y, bins=(50, 50), cmap=plt.cm.Greys)
    # cb = plt.colorbar()  
    
    # while, modify to ax.hist2d() will get 
    # error:No mappable was found to use for colorbar creation.
    # solution bellow. 

    ax.hist2d(x, y, bins=(50, 50), cmap=plt.cm.Greys)
    # print(ax.get_children())
    # [<matplotlib.collections.QuadMesh object at 0x0000022195FEB790>, 
    # <matplotlib.spines.Spine object at 0x0000022195FBF880>, 
    # <matplotlib.spines.Spine object at 0x0000022195A60FA0>, 
    # <matplotlib.spines.Spine object at 0x0000022195A60C40>, 
    # <matplotlib.spines.Spine object at 0x0000022195A60E20>, 
    # <matplotlib.axis.XAxis object at 0x0000022195FBF910>, 
    # <matplotlib.axis.YAxis object at 0x0000022195A60430>, 
    # Text(0.5, 1.0, ''), Text(0.0, 1.0, ''), Text(1.0, 1.0, ''), 
    # <matplotlib.patches.Rectangle object at 0x0000022195FCC430>] 
    # follow the output, the first is hist2d
    Hist2d = ax.get_children()[0]  
    cb = plt.colorbar(Hist2d, ax=ax)
    ax.set_title("with color bar")

    plt.show()
    plt.close()


if __name__ == "__main__":
    histograms_2d()
