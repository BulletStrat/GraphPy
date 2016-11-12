import matplotlib.pyplot as plt
plt.style.use((['fivethirtyeight', 'ggplot']))
import matplotlib.patches as mpatches
#plt.style.use('fivethirtyeight')
import pandas as pd
import numpy as np
from datetime import datetime


colors = ['b', 'c', 'y', 'm', 'r']
color=colors[0]

# class init_function:
#     def __init__(file):
#         print("Enter file name or file path:")
#         #file = input()
#
#         if file.lower().endswith(('.txt', '.csv')):
#             CSV_Handler.__init__(file)
#         elif file.lower().endswith(('.xlrs', '.xlr', '.xlsx')):
#             Excel_Handler.__init__(file)
#         else:
#             print("Unsupported Filetype!")

col = [ 'red', 'green', 'blue', 'blue', 'yellow', 'black', 'green', 'red', 'red', 'green', 'blue', 'yellow', 'green',
     'blue', 'yellow', 'green', 'blue', 'blue', 'red', 'blue', 'yellow', 'blue', 'blue', 'yellow', 'red', 'yellow',
     'blue', 'blue', 'blue', 'yellow', 'blue', 'green', 'yellow', 'green', 'green', 'blue', 'yellow', 'yellow', 'blue',
     'yellow', 'blue', 'blue', 'blue', 'green', 'green', 'blue', 'blue', 'green', 'blue', 'green', 'yellow', 'blue',
     'blue', 'yellow', 'yellow', 'red', 'green', 'green', 'red', 'red', 'red', 'red', 'green', 'red', 'green', 'yellow',
     'red', 'red', 'blue', 'red', 'red', 'red', 'red', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'blue', 'blue',
     'blue', 'yellow', 'red', 'green', 'blue', 'blue', 'red', 'blue', 'red', 'green', 'black', 'yellow', 'blue', 'blue',
     'green', 'red', 'red', 'yellow', 'yellow', 'yellow', 'red', 'green', 'green', 'yellow', 'blue', 'green', 'blue',
     'blue', 'red', 'blue', 'green', 'blue', 'red', 'green', 'green', 'blue', 'blue', 'green', 'red', 'blue', 'blue',
     'green', 'green', 'red', 'red', 'blue', 'red', 'blue', 'yellow', 'blue', 'green', 'blue', 'green', 'yellow',
     'yellow', 'yellow', 'red', 'red', 'red', 'blue', 'blue']


# def CSV_Handler(file):
#      print("Is your data separated by commas or empty spaces?Please specify with characters:")
#      delimiter = str(input())
#      df = pd.read_csv(file, sep=delimiter, header=0, engine='python')
#      print(df)
#      return df
#
# class Excel_Handler:
#     def __init__(file):
#         df = pd.read_excel(file)
#         print(df.head())

def Sanitize():
    # if '-' in time_string:
    #     splitter = '-'
    # elif ':' in time_string:
    #     splitter = '-'
    # else:
    #     splitter = ','
    # (mins, secs) = time_string.split(splitter)
    # return (mins + '.' + secs)
    import fileinput
    file = 'titanic2.csv'
    with fileinput.FileInput(file, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('\t', ','), end='')
    print(file)
#Sanitize()
class Graph:
    def __init__(file):
        x = [1950, 1970, 1990, 2010]
        y = [2.519, 3.692, 5.263, 6.972]
        z = [2.519,2.519, 3.692, 5.263, 6.972, 6.972, 6.972, 6.972]

        print("Insert x and y label and fig name: ")
        Xlabel = input()
        Ylabel = input()
        label = input()

        plt.xlabel(Xlabel)
        plt.ylabel(Ylabel)
        plt.title(label)

        np_pop = np.array(y)
        np_pop = np_pop * 8


        plt.scatter(x,y,s=np_pop,c = col,alpha=0.8)
        plt.grid(True)
        plt.show()
        plt.savefig()
        plt.plot(x,y,marker='o')
        plt.grid(True)
        plt.show()
        plt.hist(z, bins=3)
        plt.grid(True)
        plt.show()



class GraphData:

    def __init__(self,file,title,xlabel,ylabel,grid,x,y):
        print("Graph initializing....")
        self.file = file
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.grid = grid
        self.x = x
        self.y = y
        print(file,title,xlabel,ylabel,grid,x,y)


    def CSV_Handler(self):
        print("Handling CSV....:")
        #delimiter = ',' and '\t' and ':'
        self.df = pd.read_csv(self.file, sep=',', header=0, engine='python')
        print(self.df)
        self.graph()

    def file_type(self):
        print("filetype processing....")
        if self.file.lower().endswith(('.txt', '.csv')):
            self.CSV_Handler()
        elif self.file.lower().endswith(('.xlrs', '.xlr', '.xlsx')):
            #Excel_Handler.__init__(self.file)
            print("Support for Excel coming Soon!")
        else:
            print("Unsupported Filetype!")
        print("filetype processing....")

    def details(self):
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)

        plt.minorticks_on()
        plt.grid(b=self.grid, which='minor', color='w', linestyle='-')
        plt.grid(b=self.grid, which='major', color='#737e8e', linestyle='-')

        plt.rc('axes', edgecolor='r')

    def graph(self):
        x = self.df[self.x]
        y = self.df[self.y]

        np_pop = np.array(y)
        np_pop = np_pop * 8

        self.details()
        Color = 'c'
        plt.plot(x, y, marker='o', color=Color)
        plt.grid(self.grid)
        plt.legend(handles=[mpatches.Patch(color=Color, label=self.title)])
        plt.show()
        plt.savefig(self.title + " " + datetime.now().strftime('%Y-%m-%d %H:%M') + '.png')
        Color = 'm'

        self.details()
        plt.scatter(x, y, s=np_pop, c=col, alpha=0.8)
        plt.grid(self.grid)
        plt.show()
        plt.savefig(self.title + " "+ datetime.now().strftime('%Y-%m-%d %H:%M')+" "+'.png')

        self.details()
        plt.hist(y, bins=5)
        plt.grid(self.grid)
        plt.show()
        plt.savefig(self.title + " " + datetime.now().strftime('%Y-%m-%d %H:%M') + '.png')

# x = GraphData("World Population Growth.csv","apple","x","y",True,'year','population')
# x.file_type()