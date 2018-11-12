import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold

# Return a flattened df of the specified feature (either 'max_min' or 'var')
def flatten(df, feature='max_min', interval=80):
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

def separate_test_train(dfs, test_size=0.2):
    train_df = pd.DataFrame()
    test_df = pd.DataFrame()

    for df in dfs:
        y = df['truth']
        X = df[df.columns[df.columns != 'truth']].copy()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=4)

        train = pd.concat([X_train, y_train], axis=1)
        test = pd.concat([X_test, y_test], axis=1)

        train_df = train_df.append(train)
        test_df = test_df.append(test)

    # Shuffle rows
    train_df = train_df.sample(frac=1).reset_index(drop=True)
    test_df = test_df.sample(frac=1).reset_index(drop=True)

    return (train_df, test_df)

# for train_index, test_index in kf.split(data_df):
#     print("TRAIN:", train_index, "TEST:", test_index)
#     X_train, X_test = data_df.iloc[train_index], data_df.iloc[test_index]
#     y_train, y_test = truth_df[train_index], truth_df.iloc[test_index]
def k_fold(df, fold_no=2):
    kf = KFold(n_splits=fold_no, random_state=2, shuffle=False)
    return kf.split(df)
