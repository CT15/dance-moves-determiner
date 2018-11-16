import sys
import pickle
import time
import pandas as pd
import numpy as np
import train_data 
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import f1_score
from sklearn.model_selection import RandomizedSearchCV
from termcolor import colored

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
    sample_rf = RandomForestClassifier(random_state=40)

    print(colored("[RF]", "green"), " List of parameters ---")
    for key in sample_rf.get_params().keys():
        print("\t- " + str(key))

    print(colored("[RF]", "green"), " Hyperparameters to tune ---")
    for hyperparam in ['n_estimator', 'max_features', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'bootstrap']:
        print("\t- " + hyperparam)

    print("Creating parameter grid ...")

    # Number of trees in random forest
    n_estimators = [int(x) for x in np.linspace(start=100, stop=2000, num=10)]
    # Number of features to consider at every split
    max_features = ['auto', 'log2', None]
    # Maximum number of levels in tree
    max_depth = [int(x) for x in np.linspace(10, 110, num=11)]
    max_depth.append(None)
    # Minimum number of samples required to split a node
    min_samples_split = [2, 5, 10]
    # Minimum number of samples required at each leaf node
    min_samples_leaf = [1, 2, 4]
    # Method of selecting samples for training each tree
    bootstrap = [True, False]

    random_grid = {'n_estimators': n_estimators,
                   'max_features': max_features,
                   'max_depth': max_depth,
                   'min_samples_split': min_samples_split,
                   'min_samples_leaf': min_samples_leaf,
                   'bootstrap': bootstrap}
    
    print(colored("[RF]", "green"), " Random grid created ---")
    for key in random_grid.keys():
        print("\t- " + key + ":\t" + str(random_grid[key]))

    print(colored("[RF]", "green"),  " Instatiating Random Search ...")

    # Base model to tune
    clf = RandomForestClassifier()
    clf_random = RandomizedSearchCV(estimator=clf, param_distributions=random_grid, n_iter=100, cv=3, verbose=2, random_state=37, n_jobs=-1)
    
    X_train, y_train = get_X_y(train_df)
    X_validate, y_validate = get_X_y(validate_df)
    X_all = X_train.append(X_validate)
    y_all = y_train.append(y_validate)
    
    print(colored("[RF]", "green"), " Start Random Search fitting ...")
    print(colored("[RF]", "green"), " time started ...")
    start_time = time.time()
    clf_random.fit(X_all, y_all)
    
    print(colored("[RF]", "green"), " Random Search fitting DONE with best hyperparameters --->")
    for key in clf_random.best_params_.keys():
        print("\t- " + key + ":\t" + str(clf_random.best_params_[key]))

    print(colored("[RF]", "green"), "time stopped ... Total time = " + str(time.time() - start_time))

    # print("Start choosing n_estimator for random forest")
    
    # max_score = -1
    # estimator_chosen = -1
    # f1_max = 0

    # for estimator in range(1, 350, 3):
    #     clf = RandomForestClassifier(n_estimators=estimator, random_state=2, oob_score=False)
    #     clf.fit(X_train, y_train)
    #     train_score = clf.score(X_train, y_train)
    #     validate_score = clf.score(X_validate, y_validate)
        
    #     y_pred = clf.predict(X_validate)
    #     f1 = f1_score(y_validate, y_pred, average='weighted')

    #     print("RF: n_estimator = " + str(estimator) + "\t\tf1 = " + str(f1) + "\t\ttrain_score =  " + str(train_score) + "\t\tvalidate_score = " + str(validate_score))

    #     if f1 > f1_max:
    #         f1_max = f1
    #         estimator_chosen = estimator

    # print("= = = = = = = = = = =")
    # print("RF: final n_estimator chosen = " + str(estimator_chosen))
    
    # print("Generating Random Forest model")
    
    # clf = RandomForestClassifier(n_estimators=estimator_chosen, random_state=2, oob_score=False)
    
    # X_df = pd.concat([X_train, X_validate], axis=0)
    # y_df = pd.concat([y_train, y_validate], axis=0)
    # clf.fit(X_df, y_df)

    # print("final_train_score = " + str(clf.score(X_df, y_df)))

    # print("Saving Random Forest model ...")
    # with open('./models/random_forest.sav', 'wb') as f:
    #     pickle.dump(clf, f)
    # print("COMPLETE")    


# Generate svm.sav and save it to model folder
def generate_svm(train_df, validate_df):
    pass


if __name__ == "__main__":
    train_df, validate_df = split_train_validate(train_data.load())
    generate_random_forest(train_df, validate_df)
    generate_svm(train_df, validate_df)        
