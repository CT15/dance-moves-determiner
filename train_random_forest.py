import sys
import pickle
import time
import pandas as pd
import numpy as np
import train_data 
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import f1_score, confusion_matrix
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from termcolor import colored

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


def evaluate(model, X_train, y_train, X_test, y_test):
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)

    y_pred = model.predict(X_test)
    f1 = f1_score(y_test, y_pred, average='weighted')

    print(colored("[EVAL]", "blue"), " n_estimator = " + str(estimator) + "\t\tf1 = " + str(f1) + "\t\ttrain_score =  " + str(train_score) + "\t\ttest_score = " + str(test_score))
    
    print(colored("[EVAL]", "blue"), " Showing confusion matrix ...")

    confusion_matrix = confusion_matrix(y_test, y_pred)
    df_cm = pd.DataFrame(confusion_matrix, index=[i for i in range(11)+1], columns=[i for i in range(11)+1])
    plt.figure(figsize=(10,7))
    sn.set(font_scale=1.4)
    sn.heatmap(df_cm, annot=True, annot_kws={"size": 16})

    return test_score


# Generate random_forest.sav and save it to model folder
def generate_random_forest(train_df, test_df):
    sample_rf = RandomForestClassifier(random_state=40)

    print(colored("[RF]", "green"), " List of parameters ---")
    for key in sample_rf.get_params().keys():
        print("\t- " + str(key))

    print(colored("[RF]", "green"), " Hyperparameters to tune ---")
    for hyperparam in ['n_estimator', 'max_features', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'bootstrap']:
        print("\t- " + hyperparam)

    print("Creating parameter grid for random search ...")

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
    X_test, y_test = get_X_y(test_df)
    
    print(colored("[RF]", "green"), " Start Random Search fitting ...")
    clf_random.fit(X_train, y_train)
    
    print(colored("[RF]", "green"), " Time started ...")
    start_time = time.time()
    
    print(colored("[RF]", "green"), " Random Search fitting DONE with best hyperparameters --->")
    bp = clf_random.best_params_
    for key in bp.keys():
        print("\t- " + key + ":\t" + str(bp[key]))

    print(colored("[RF]", "green"), "Time stopped ... Total time = " + str(time.time() - start_time))
    
    print(colored("[RF]", "green"), " Initializing base model ...")
    base_model = RandomForestClassifier(n_estimators=bp['n_estimators'], min_samples_split=bp['min_samples_split'], 
                                        min_samples_leaf=bp['min_samples_leaf'], max_features=bp['max_features'], 
                                        max_depth=bp['max_depth'], bootstrap=bp['bootstrap'])
    
    print(colored("[RF]", "green"), " Evaluating base model ...")
    base_score = evaluate(base_model, X_train, y_train, X_test, y_test)

    print(colored("[RF]", "green"), " Creating parameter grid for grid search ...")
    
    # Number of trees in random forest
    n_estimators = [bp['n_estimators']-50, bp['n_estimators']+50, bp['n_estimators']+100, bp['n_estimators']+150]
    # Number of features to consider at every split
    max_features = [bp['max_features']]
    # Maximum number of levels in tree
    max_depth = [bp['max_depth']+10, bp['max_depth']+20, bp['max_depth']+30, bp['max_depth']+40] if bp['max_depth'] else [None]
    # Minimum number of samples required to split a node
    min_samples_split = [bp['min_samples_split']+2, bp['min_samples_split']+4, bp['min_samples_split']+6] if bp['min_samples_split'] < 4 else [bp['min_samples_split']-2, bp['min_samples_split']+2, bp['min_samples_split']+4]
    # Minimum number of samples required at each leaf node
    min_samples_leaf = [2, 3, 4] if bp['min_samples_leaf'] <= 1 else [bp['min_samples_leaf']-1, bp['min_samples_leaf']+1, bp['min_samples_leaf']+2]
    # Method of selecting samples for training each tree
    bootstrap = [bp['bootstrap']]

    param_grid = {'n_estimators': n_estimators,
                  'max_features': max_features,
                  'max_depth': max_depth,
                  'min_samples_split': min_samples_split,
                  'min_samples_leaf': min_samples_leaf,
                  'bootstrap': bootstrap}

    # Base model to tune
    clf = RandomForestClassifier()

    clf_grid = GridSearchCV(estimator=clf, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)

    print(colored("[RF]", "green"), " Start Grid Search fitting ...")
    clf_grid.fit(X_train, y_train)
    
    print(colored("[RF]", "green"), " Time started ...")
    start_time = time.time()
    
    print(colored("[RF]", "green"), " Grid Search fitting DONE with best hyperparameters --->")
    bp = clf_grid.best_params_
    for key in bp.keys():
        print("\t- " + key + ":\t" + str(bp[key]))

    print(colored("[RF]", "green"), "Time stopped ... Total time = " + str(time.time() - start_time))
    
    print(colored("[RF]", "green"), " Initializing best grid model ...")
    grid_model = RandomForestClassifier(n_estimators=bp['n_estimators'], min_samples_split=bp['min_samples_split'], 
                                        min_samples_leaf=bp['min_samples_leaf'], max_features=bp['max_features'], 
                                        max_depth=bp['max_depth'], bootstrap=bp['bootstrap'])
    
    print(colored("[RF]", "green"), " Evaluating grid model ...")
    grid_score = evaluate(grid_model, X_train, y_train, X_test, y_test)

    improvement = 100 * (grid_score - base_score) / base_score

    print(colored("[RF]", "green"), " Improvement of " + str(improvement) + "% from the base model")

    if improvement <= 0:
        print(colored("[RF]", "green"), " Base model is used")
        clf = base_model
    else:
        print(colored("[RF]", "green"), " Grid model is used")
        clf = grid_model

    print(colored("[RF]", "green"), " Saving Random Forest model ...", end=" ")
    
    with open('./models/random_forest.sav', 'wb') as f:
        pickle.dump(clf, f)
    
    print(colored("DONE"), "green")  
    
    # print("Start choosing n_estimator for random forest")
    
    # max_score = -1
    # estimator_chosen = -1
    # f1_max = 0

    # for estimator in range(1, 350, 3):
    #     clf = RandomForestClassifier(n_estimators=estimator, random_state=2, oob_score=False)
    #     clf.fit(X_train, y_train)
    #     train_score = clf.score(X_train, y_train)
    #     test_score = clf.score(X_test, y_test)
        
    #     y_pred = clf.predict(X_test)
    #     f1 = f1_score(y_test, y_pred, average='weighted')

    #     print("RF: n_estimator = " + str(estimator) + "\t\tf1 = " + str(f1) + "\t\ttrain_score =  " + str(train_score) + "\t\ttest_score = " + str(test_score))

    #     if f1 > f1_max:
    #         f1_max = f1
    #         estimator_chosen = estimator

    # print("= = = = = = = = = = =")
    # print("RF: final n_estimator chosen = " + str(estimator_chosen))
    
    # print("Generating Random Forest model")
    
    # clf = RandomForestClassifier(n_estimators=estimator_chosen, random_state=2, oob_score=False)
    
    # X_df = pd.concat([X_train, X_test], axis=0)
    # y_df = pd.concat([y_train, y_test], axis=0)
    # clf.fit(X_df, y_df)

    # print("final_train_score = " + str(clf.score(X_df, y_df)))


# Generate svm.sav and save it to model folder
def generate_svm(train_df, test_df):
    pass


if __name__ == "__main__":
    train_df, test_df = split_train_test(train_data.load())
    generate_random_forest(train_df, test_df)
