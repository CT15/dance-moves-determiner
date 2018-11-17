import sys
import pickle
import pandas as pd
import numpy as np

# Return a flattened df of the specified feature (either 'max_min' or 'std')
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

        if feature == 'std':
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
                'wipers',   # Wipers ==> 1
                'number7',  # Number7 ==> 2
                'chicken',  # Chicken ==> 3
                'sidestep', # SideStep ==> 4
                'turnclap', # TurnClap ==> 5
                'numbersix',# Number6 ==> 6
                'salute',   # Salute ==> 7
                'mermaid',  # Mermaid ==> 8
                'swing',    # Swing ==> 9
                'cowboy',   # Cowboy ==> 10
                'logout',   # FinalMove ==> 11
    ]

    def __init__(self):
        PATH_TO_MODEL = sys.path[0] + '/models'
        self.RF = pickle.load(open(PATH_TO_MODEL + '/random_forest.sav', 'rb'))
        # self.SVM = pickle.load(open(PATH_TO_MODEL + '/svm.sav', 'rb'))
    

    # This method is called when dance moves are required to be
    # predicted in real time. Return one dance label in the form
    # of the actual dance move.
    def predict_realtime(self, df):
        df_max_min = flatten(df, interval=len(df))
        df_std = flatten(df, 'std', interval=len(df))
        df_concat = concat_df(df_max_min, df_std)

        predicted_RF = self.RF.predict(df_concat)
        # predicted_SVM = self.SVM.predict(df_concat)

        # if predicted_RF != predicted_SVM:
            # return None

        return self.DANCES[predicted_RF[0]]
