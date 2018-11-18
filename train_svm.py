import os
import pickle
import pandas as pd
import numpy as np
import train_data
import preprocess as prep
from sklearn.svm import SVC
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from termcolor import colored
from evaluate import evaluate

# Generate svc.sav and save it to model folder
def generate_svc(train_df, test_df):
    file = open('./eval_results/svc_train_stats.txt', 'w+')

    sample_svc = SVC(random_state=40)

    print(colored("[SVC]", "green"), " List of parameters:")
    for key in sample_svc.get_params().keys():
        print("\t- " + str(key))

    print(colored("[SVC]", "green"), " Hyperparameters to tune:")
    for hyperparam in ['degree', 'kernel', 'gamma']:
        print("\t- " + hyperparam)

    print("Creating parameter grid for random search ...")

    # Number of trees in random forest
    degree = [int(x) for x in np.linspace(start=2, stop=4,num=2)]
    # Number of features to consider at every split
    kernel = ['poly']
    # Maximum number of levels in tree
    gamma = ['auto']

    random_grid = {'degree': degree,
                   'kernel': kernel,
                   'gamma': gamma}

    print(colored("[SVC]", "green"), " Random grid created:")
    file.write("Random Grid for Random Search:\n")
    for key in random_grid.keys():
        to_print = "\t- " + key + ":\t" + str(random_grid[key])
        print(to_print)
        file.write(to_print + "\n")

    file.write("\n")

    print(colored("[SVC]", "green"),  " Instatiating Random Search ...")

    # Base model to tune
    clf = SVC()
    clf_random = RandomizedSearchCV(estimator=clf, param_distributions=random_grid, n_iter=2, cv=3, verbose=2, random_state=37, n_jobs=-1)

    X_train, y_train = prep.get_X_y(train_df)
    X_test, y_test = prep.get_X_y(test_df)

    print(colored("[SVC]", "green"), " Start Random Search fitting ...")
    clf_random.fit(X_train, y_train)

    print(colored("[SVC]", "green"), " Random Search fitting DONE with best hyperparameters:")
    file.write("Best hyperparameters from Random Search:\n")

    bp = clf_random.best_params_
    for key in bp.keys():
        to_print = "\t- " + key + ":\t" + str(bp[key])
        print(to_print)
        file.write(to_print + "\n")

    file.write("\n")

    print(colored("[SVC]", "green"), " Initializing base model ...")

    base_model = SVC(degree=bp['degree'], kernel=bp['kernel'],
                                        gamma=bp['gamma'])
    base_model.fit(X_train, y_train)

    print(colored("[SVC]", "green"), " Evaluating base model ...")
    base_score = evaluate(base_model, X_train, y_train, X_test, y_test, 'SVC', 1)
    file.write("Base model evaluation: [refer to svc_eval1.txt]\n\n")

    print(colored("[SVC]", "green"), " Creating parameter grid for grid search ...")

    # Number of trees in random forest
    degree = [bp['degree']]
    # Number of features to consider at every split
    kernel = [bp['kernel']]
    # Maximum number of levels in tree
    gamma = [bp['gamma']]

    param_grid = {'degree': degree,
                  'kernel': kernel,
                  'gamma': gamma}

    print(colored("[SVC]", "green"), " Random grid created:")
    file.write("Random Grid for Grid Search:\n")
    for key in param_grid.keys():
        to_print = "\t- " + key + ":\t" + str(param_grid[key])
        print(to_print)
        file.write(to_print + "\n")

    file.write("\n")

    # Base model to tune
    clf = SVC()

    clf_grid = GridSearchCV(estimator=clf, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)

    print(colored("[SVC]", "green"), " Start Grid Search fitting ...")
    clf_grid.fit(X_train, y_train)

    print(colored("[SVC]", "green"), " Grid Search fitting DONE with best hyperparameters:")
    file.write("Best hyperparameters from Grid Search:\n")
    bp = clf_grid.best_params_
    for key in bp.keys():
        to_print = "\t- " + key + ":\t" + str(bp[key])
        print(to_print)
        file.write(to_print + "\n")

    file.write("\n")

    print(colored("[SVC]", "green"), " Initializing best grid model ...")
    grid_model = SVC(degree=bp['degree'], kernel=bp['kernel'],
                                        gamma=bp['gamma'])

    grid_model.fit(X_train, y_train)

    print(colored("[SVC]", "green"), " Evaluating grid model ...")
    grid_score = evaluate(grid_model, X_train, y_train, X_test, y_test, 'SVC', 2)
    file.write("Fine tuned model evaluation: [refer to svc_eval2.txt]\n\n")

    improvement = 100 * (grid_score - base_score) / base_score

    print(colored("[SVC]", "green"), " Improvement of " + str(improvement) + "% from the base model")
    file.write("Improvement of " + str(improvement) + "% from the base model\n\n")

    if improvement <= 0:
        to_print = "Base model is used"
        print(colored("[SVC]", "green"), " " + to_print)
        file.write(to_print + "\n")
        clf = base_model
    else:
        to_print = "Grid model is used"
        print(colored("[SVC]", "green"), " " + to_print)
        file.write(to_print + "\n")
        clf = grid_model

    print(colored("[SVC]", "green"), " Saving SVCmodel ...")

    with open('./models/svc.sav', 'wb') as f:
        pickle.dump(clf, f)

    print(colored("[RF]", "green"), " SVC model saved")

    file.close()


if __name__ == "__main__":
    train_df, test_df = prep.split_train_test(train_data.load())
    print(colored("[CHECK]", "magenta"), " Total train data:\t" + str(len(train_df)))
    print(colored("[CHECK]", "magenta"), " Total test data:\t" + str(len(test_df)))
    generate_svc(train_df, test_df)
    print(colored("[END]", "green"), " SVC training completed")
