import test_data
import pandas as pd
from test_model import MLModel
from sklearn.metrics import accuracy_score

# This method combines all the dfs in the list
# and split the combined df to features df and
# truths df
def split_features_truths(dfs):
    features_df = pd.DataFrame()
    truths_df = pd.DataFrame()
    for df in dfs:
        features_df = features_df.append(df.loc[:, df.columns != 'truth'])
        truths_df = truths_df.append(df.loc[:, df.columns == 'truth'])

    return (features_df, truths_df)

if __name__ == "__main__":
    features_df, truths_df = split_features_truths(test_data.load())
    
    model = MLModel()
    predicted_df = model.predict(features_df)

    print("Accuracy score -----")
    print(accuracy_score(truths_df, predicted_df))
    print("--------------------")

