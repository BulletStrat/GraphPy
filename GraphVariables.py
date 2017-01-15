import pandas as pd

def read_vars(file):
    df = pd.read_csv(file, sep=',', header=0, engine='python')
    vars = list(df)
    return vars

def read_vars_beta(file):
    with open(file) as f:
        data = f.readline()
    vars = data.strip().split( ',')
    print (vars)
    return vars
