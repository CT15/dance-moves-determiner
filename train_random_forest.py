import os
import pickle
import pandas as pd
import numpy as np
import train_data
import preprocess as prep
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from termcolor import colored
from evaluate import evaluate

# Generate random_forest.sav and save it to model folder
def generate_random_forest(train_df, test_df):
    file = open('./eval_results/random_forest_train_stats.txt', 'w+')

    sample_rf = RandomForestClassifier(random_state=40)

    print(colored("[RF]", "green"), " List of parameters:")
    for key in sample_rf.get_params().keys():
        print("\t- " + str(key))

    print(colored("[RF]", "green"), " Hyperparameters to tune:")
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
    
    print(colored("[RF]", "green"), " Random grid created:")
    file.write("Random Grid for Random Search:\n")
    for key in random_grid.keys():
        to_print = "\t- " + key + ":\t" + str(random_grid[key])
        print(to_print)
        file.write(to_print + "\n")

    file.write("\n")

    print(colored("[RF]", "green"),  " Instatiating Random Search ...")

    # Base model to tune
    clf = RandomForestClassifier()
    clf_random = RandomizedSearchCV(estimator=clf, param_distributions=random_grid, n_iter=100, cv=3, verbose=2, random_state=37, n_jobs=-1)
    
    X_train, y_train = prep.get_X_y(train_df)
    X_test, y_test = prep.get_X_y(test_df)
    
    print(colored("[RF]", "green"), " Start Random Search fitting ...")
    clf_random.fit(X_train, y_train)
    
    print(colored("[RF]", "green"), " Random Search fitting DONE with best hyperparameters:")
    file.write("Best hyperparameters from Random Search:\n")

    bp = clf_random.best_params_
    for key in bp.keys():
        to_print = "\t- " + key + ":\t" + str(bp[key])
        print(to_print)
        file.write(to_print + "\n")

    file.write("\n")

    print(colored("[RF]", "green"), " Initializing base model ...")
    base_model = RandomForestClassifier(n_estimators=bp['n_estimators'], min_samples_split=bp['min_samples_split'], 
                                        min_samples_leaf=bp['min_samples_leaf'], max_features=bp['max_features'], 
                                        max_depth=bp['max_depth'], bootstrap=bp['bootstrap'])
    base_model.fit(X_train, y_train)

    print(colored("[RF]", "green"), " Evaluating base model ...")
    base_score = evaluate(base_model, X_train, y_train, X_test, y_test, 'RF')
    file.write("Base model evaluation: [refer to random_forest_eval.txt (top)]\n\n")

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

    print(colored("[RF]", "green"), " Random grid created:")
    file.write("Random Grid for Grid Search:\n")
    for key in param_grid.keys():
        to_print = "\t- " + key + ":\t" + str(param_grid[key])
        print(to_print)
        file.write(to_print + "\n")

    file.write("\n")

    # Base model to tune
    clf = RandomForestClassifier()

    clf_grid = GridSearchCV(estimator=clf, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)

    print(colored("[RF]", "green"), " Start Grid Search fitting ...")
    clf_grid.fit(X_train, y_train)
    
    print(colored("[RF]", "green"), " Grid Search fitting DONE with best hyperparameters:")
    file.write("Best hyperparameters from Grid Search:\n")
    bp = clf_grid.best_params_
    for key in bp.keys():
        to_print = "\t- " + key + ":\t" + str(bp[key])
        print(to_print)
        file.write(to_print + "\n")

    file.write("\n")
    
    print(colored("[RF]", "green"), " Initializing best grid model ...")
    grid_model = RandomForestClassifier(n_estimators=bp['n_estimators'], min_samples_split=bp['min_samples_split'], 
                                        min_samples_leaf=bp['min_samples_leaf'], max_features=bp['max_features'], 
                                        max_depth=bp['max_depth'], bootstrap=bp['bootstrap'])
    
    grid_model.fit(X_train, y_train)

    print(colored("[RF]", "green"), " Evaluating grid model ...")
    grid_score = evaluate(grid_model, X_train, y_train, X_test, y_test, 'RF')
    file.write("Fine tuned model evaluation: [refer to random_forest_eval.txt (bottom)]\n\n")

    improvement = 100 * (grid_score - base_score) / base_score

    print(colored("[RF]", "green"), " Improvement of " + str(improvement) + "% from the base model")
    file.write("Improvement of " + str(improvement) + "% from the base model\n\n")

    if improvement <= 0:
        to_print = "Base model is used"
        print(colored("[RF]", "green"), " " + to_print)
        file.write(to_print + "\n")
        clf = base_model
    else:
        to_print = "Grid model is used"
        print(colored("[RF]", "green"), " " + to_print)
        file.write(to_print + "\n")
        clf = grid_model

    print(colored("[RF]", "green"), " Saving Random Forest model ...")
    
    with open('./models/random_forest.sav', 'wb') as f:
        pickle.dump(clf, f)
    
    print(colored("[RF]", "green"), " Random Forest model saved")  

    file.close()
    

if __name__ == "__main__":
    # Housekeeping
    try:
        os.remove('./eval_results/random_forest_eval.txt')
    except OSError:
        pass

    train_df, test_df = prep.split_train_test(train_data.load())
    print(colored("[CHECK]", "magenta"), " Total train data:\t" + str(len(train_df)))
    print(colored("[CHECK]", "magenta"), " Total test data:\t" + str(len(test_df)))
    generate_random_forest(train_df, test_df)
    print(colored("[END]", "green"), " Random Forest training completed")
