import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from termcolor import colored
from sklearn.metrics import f1_score, confusion_matrix

def evaluate(model, X_train, y_train, X_test, y_test):
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)

    y_pred = model.predict(X_test)
    f1 = f1_score(y_test, y_pred, average='weighted')

    print(colored("[EVAL]", "blue"), " f1 = " + str(f1) + "\t\ttrain_score =  " + str(train_score) + "\t\ttest_score = " + str(test_score))
    
    print(colored("[EVAL]", "blue"), " Generating confusion matrix ...")

    confusion_matrix = confusion_matrix(y_test, y_pred)
    print(pd.DataFrame(confusion_matrix))

    df_cm = pd.DataFrame(confusion_matrix, index=[i for i in range(11)+1], columns=[i for i in range(11)+1])
    plt.figure(figsize=(10,7))
    sn.set(font_scale=1.4)
    sn.heatmap(df_cm, annot=True, annot_kws={"size": 16})

    return test_score