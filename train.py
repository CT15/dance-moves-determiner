import sys
import pickle
import pandas as pd
import train_data 
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import f1_score

# This method split dfs to train_df and validate_df
# based on timestamp. The first `train_percent` of all
# the input dfs will be grouped into train_df. The rest
# are grouped into validate_df.
def split_train_validate(dfs, train_percent=0.8):
    train_df = pd.DataFrame()
    validate_df = pd.DataFrame()

    for df in dfs:
        train_len = round(len(df) * train_percent)
        train_df = train_df.append(df.loc[0:train_len, :])
        validate_df = validate_df.append(df.loc[train_len:len(df), :])
    
    return (train_df, validate_df)


def get_X_y(df):
    y = df.iloc[:, -1]
    X = df.iloc[:, :-1]
    return (X, y)

# Generate random_forest.sav and save it to model folder
def generate_random_forest(train_df, validate_df):
    X_train, y_train = get_X_y(train_df)
    X_validate, y_validate = get_X_y(validate_df)
    
    print("Start choosing n_estimator for random forest")
    
    max_score = -1
    estimator_chosen = -1
    f1_max = 0

    for estimator in range(1, 350, 3):
        clf = RandomForestClassifier(n_estimators=estimator, random_state=2, oob_score=False)
        clf.fit(X_train, y_train)
        train_score = clf.score(X_train, y_train)
        validate_score = clf.score(X_validate, y_validate)
        
        y_pred = clf.predict(X_validate)
        f1 = f1_score(y_validate, y_pred, average='weighted')

        print("RF: n_estimator = " + str(estimator) + "\t\tf1 = " + str(f1) + "\t\ttrain_score =  " + str(train_score) + "\t\tvalidate_score = " + str(validate_score))

        if f1 > f1_max:
            f1_max = f1
            estimator_chosen = estimator

    print("= = = = = = = = = = =")
    print("RF: final n_estimator chosen = " + str(estimator_chosen))
    
    print("Generating Random Forest model")
    
    clf = RandomForestClassifier(n_estimators=estimator_chosen, random_state=2, oob_score=False)
    
    X_df = pd.concat([X_train, X_validate], axis=0)
    y_df = pd.concat([y_train, y_validate], axis=0)
    clf.fit(X_df, y_df)

    print("final_train_score = " + str(clf.score(X_df, y_df)))

    print("Saving Random Forest model ...")
    with open('./models/random_forest.sav', 'wb') as f:
        pickle.dump(clf, f)
    print("COMPLETE")    


# Generate svm.sav and save it to model folder
def generate_svm(train_df, validate_df):
    pass


if __name__ == "__main__":
    train_df, validate_df = split_train_validate(train_data.load())
    print("a")
    generate_random_forest(train_df, validate_df)
    generate_svm(train_df, validate_df)        
