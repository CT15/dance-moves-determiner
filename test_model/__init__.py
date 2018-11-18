import sys
import pickle
import pandas as pd
import numpy as np

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


# Return a df that is the concatenation of two input dfs (column wise)
def concat_df(df1, df2):
    df1.reset_index(drop=True, inplace=True)
    df2.reset_index(drop=True, inplace=True)

    df = pd.concat( [df1, df2], axis=1, ignore_index=True)

    return df


class MLModel:
    DANCES = [
                'wipers',   # Wipers ==> 0
                'number7',  # Number7 ==> 1
                'chicken',  # Chicken ==> 2
                'sidestep', # SideStep ==> 3
                'turnclap', # TurnClap ==> 4
                'numbersix',# Number6 ==> 5
                'salute',   # Salute ==> 6
                'mermaid',  # Mermaid ==> 7
                'swing',    # Swing ==> 8
                'cowboy',   # Cowboy ==> 9
                'logout',   # FinalMove ==> 10
    ]

    def __init__(self):
        PATH_TO_MODEL = sys.path[0] + '/models'
        self.RF = pickle.load(open(PATH_TO_MODEL + '/random_forest.sav', 'rb'))
        # self.SVM = pickle.load(open(PATH_TO_MODEL + '/svm.sav', 'rb'))


    # This method is called when dance moves are required to be
    # predicted in real time. Return one dance label in the form
    # of the actual dance move.
    def predict(self, df):
        df_max_min = flatten(df, interval=len(df))
        df_var = flatten(df, 'var', interval=len(df))
        df_concat = concat_df(df_max_min, df_var)

        predicted_RF = self.RF.predict(df_concat)
        # predicted_SVM = self.SVM.predict(df_concat)

        # if predicted_RF != predicted_SVM:
            # return None

        return self.DANCES[predicted_RF[0]]


    # This method is used only in test.py where real-time prediction
    # is not required.
    def test_predict(self, df):
        return self.RF.predict(df)
