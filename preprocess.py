import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold

# Return a flattened df of the specified feature (either 'max_min' or 'var')
def flatten(df, feature='max_min', interval=60):
    result_df = pd.DataFrame()

    startIndex = 0
    while (startIndex + interval) <= len(df):
        endIndex = startIndex + interval
        subset = df.loc[startIndex:endIndex, :]
        startIndex = startIndex + interval / 2

        if feature == 'max_min':
            max_minus_min = pd.Series(np.ptp(subset[subset.columns].values, axis=0))
            result_df = result_df.append(max_minus_min, ignore_index=True)

        if feature == 'var':
            var = pd.Series(np.var(subset[subset.columns].values, axis=0))
            result_df = result_df.append(var, ignore_index=True)

    return result_df

# Return a df of the original value appended with a single truth value to the df
def append_truth(df, truth):
    df['truth'] = truth
    return df

# Return a df of the original df divided by denom
def normalise(df, denom=np.power(2, 15)):
    df = df / denom
    return df

# Return a df that is the concatenation of two input dfs (column wise)
def concat_df(df1, df2):
    df1.reset_index(drop=True, inplace=True)
    df2.reset_index(drop=True, inplace=True)

    df = pd.concat( [df1, df2], axis=1, ignore_index=True)

    return df

# This method split dfs to train_df and test_df
# based on timestamp. The first `train_percent` of all
# the input dfs will be grouped into train_df. The rest
# are grouped into test_df.
def split_train_test(dfs, train_percent=0.8):
    train_df = pd.DataFrame()
    test_df = pd.DataFrame()

    for df in dfs:
        train_len = round(len(df) * train_percent)
        train_df = train_df.append(df.loc[0:train_len, :])
        test_df = test_df.append(df.loc[train_len:len(df), :])
    
    return (train_df, test_df)

def get_X_y(df):
    y = df.iloc[:, -1]
    X = df.iloc[:, :-1]
    return (X, y)
