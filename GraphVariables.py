import matplotlib.pyplot as plt
import pandas as pd

# file ='World Population Growth.csv'
# print("Is your data separated by commas or empty spaces?Please specify with characters:")
# delimiter = str(input())
# df = pd.read_csv(file, sep=delimiter, header=0, engine='python')
# print(df)
# pd.crosstab(df["year"],df["population"],margins=True)
# plt.plot(df["year"],df["population"])
# plt.grid(True)
# plt.show()
def read_vars(file):

    df = pd.read_csv(file, sep=',', header=0, engine='python')
    vars = list(df)
    return vars


def read_vars_beta(file):
    with open(file) as f:
        data = f.readline()
    vars = data.strip().split(',')
    print (vars)
    return vars