import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from termcolor import colored
from sklearn.metrics import f1_score, confusion_matrix

# Model id should either be 'RF' or 'SVM'
def evaluate(model, X_train, y_train, X_test, y_test, model_id):
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)

    y_pred = model.predict(X_test)
    f1 = f1_score(y_test, y_pred, average='weighted')

    print(colored("[EVAL]", "blue"), " f1 = " + str(f1) + "\t\ttrain_score =  " + str(train_score) + "\t\ttest_score = " + str(test_score))
    
    print(colored("[EVAL]", "blue"), " Generating confusion matrix ...")

    cm = confusion_matrix(y_test, y_pred)
    print(pd.DataFrame(cm))

    df_cm = pd.DataFrame(confusion_matrix, index=[i for i in range(11)], columns=[i for i in range(11)])
    hm = sn.heatmap(df_cm, annot=True, annot_kws={"size": 16})
    figure = hm.get_figure()

    figure_path = './eval_results/svm_conf.png' if model_id == 'SVM' else './eval_results/random_forest_conf.png'
    file_path = './eval_results/svm_eval.txt' if model_id == 'SVM' else './eval_results/random_forest_eval.txt'

    with open(figure_path, 'wb') as f:
        figure.savefig(f, dpi=400)
   
    file = open(file_path, 'a+')
    file.write("f1:\t" + str(f1) + "\ntrain_score:\t" + str(train_score) + "\ntest_score:\t" + str(test_score) + "\n")
    file.write("Confusion Matrix:\n")
    file.write(cm)
    file.write("\n------------------------------ END\n")
    file.close()

    return test_score
