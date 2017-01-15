#### Created on 2016/11/08 by Taufiq ###

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np
from datetime import datetime


col = ['red', 'green', 'blue', 'yellow', 'black', 'green', 'red', 'red', 'green', 'blue', 'yellow', 'green',
       'blue', 'yellow', 'green', 'blue', 'blue', 'red', 'blue', 'yellow', 'blue', 'blue', 'yellow', 'red', 'yellow',
       'blue', 'blue', 'blue', 'yellow', 'blue', 'green', 'yellow', 'green', 'green', 'blue', 'yellow', 'yellow',
       'blue',
       'yellow', 'blue', 'blue', 'blue', 'green', 'green', 'blue', 'blue', 'green', 'blue', 'green', 'yellow', 'blue',
       'blue', 'yellow', 'yellow', 'red', 'green', 'green', 'red', 'red', 'red', 'red', 'green', 'red', 'green',
       'yellow',
       'red', 'red', 'blue', 'red', 'red', 'red', 'red', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'blue', 'blue',
       'blue', 'yellow', 'red', 'green', 'blue', 'blue', 'red', 'blue', 'red', 'green', 'black', 'yellow', 'blue',
       'blue',
       'green', 'red', 'red', 'yellow', 'yellow', 'yellow', 'red', 'green', 'green', 'yellow', 'blue', 'green', 'blue',
       'blue', 'red', 'blue', 'green', 'blue', 'red', 'green', 'green', 'blue', 'blue', 'green', 'red', 'blue', 'blue',
       'green', 'green', 'red', 'red', 'blue', 'red', 'blue', 'yellow', 'blue', 'green', 'blue', 'green', 'yellow',
       'yellow', 'yellow', 'red', 'red', 'red', 'blue', 'blue']

class GraphData:
    def __init__(self, file, title, xlabel, ylabel, grid, x, y, threshold):
        print("Graph initializing....")
        self.file = file
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.grid = grid
        self.x = x
        self.y = y
        self.threshold = threshold

        print("GD constructor initialized with:", file, title, xlabel, ylabel, grid, x, y, threshold)

    def CSV_Handler(self):
        print("Handling CSV file....")
        # delimiter = ',' and '\t' and ':'
        self.df = pd.read_csv(self.file, sep=',', header=0, engine='python')
        print(self.df)
        self.graph()

    def file_type(self):
        print("file_type processing....")
        if self.file.lower().endswith(('.txt', '.csv')):
            self.CSV_Handler()
        elif self.file.lower().endswith(('.xlrs', '.xlr', '.xlsx')):
            # Excel_Handler.__init__(self.file)
            print("Support for Excel coming Soon!")
        else:
            print("Unsupported Filetype!")
        print("[Process Finished]")

    def details(self):
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        #plt.title("Histogram of IQ: " r'$\mu = 100, \sigma$ =15')
        plt.minorticks_on()
        plt.grid(b=self.grid, which='minor', color='w', linestyle='-')
        plt.grid(b=self.grid, which='major', color='#737e8e', linestyle='-')

        plt.rc('axes', edgecolor='r')

    def graph(self):
        plt.style.use(['fivethirtyeight', 'ggplot'])
        x = self.df[self.x]
        y = self.df[self.y]

        np_pop = np.array(y)
        np_pop = np_pop * 8

        self.details()
        Color = 'c'
        plt.plot(x, y, marker='o', color=Color)
        plt.grid(self.grid)
        plt.legend(handles=[mpatches.Patch(color=Color, label=self.title)])
        if self.threshold < 1:
            print("threshold is less than 1 ")
        else:
            plt.axhline(y=self.threshold, xmin=0, xmax=1, hold=None, color='m')
        plt.show()
        plt.savefig(self.title + " " + datetime.now().strftime('%Y-%m-%d %H:%M') + '.png')
        self.details()
        plt.scatter(x, y, s=np_pop, c=col, alpha=0.8)
        plt.grid(self.grid)
        if self.threshold < 1:
            print("threshold is less than 1 ")
        else:
            plt.axhline(y=self.threshold, xmin=0, xmax=1, hold=None, color='m')
        plt.show()
        plt.savefig(self.title + " " + datetime.now().strftime('%Y-%m-%d %H:%M') + " " + '.png')
        self.details()
        plt.hist(y, bins=12)
        plt.grid(self.grid)
        plt.show()
        plt.savefig(self.title + " " + datetime.now().strftime('%Y-%m-%d %H:%M') + '.png')


class LiveGraph:
    def __init__(self, file):
        self.file = file
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1, 1, 1)

    def animate(self, i):
        plt.style.use('fivethirtyeight')
        graph_data = open(self.file, 'r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(x)
                ys.append(y)
        self.ax1.clear()
        self.ax1.plot(xs, ys)

    def showupdate(self):
        ani = animation.FuncAnimation(self.fig, self.animate, interval=1000)
        plt.show()
