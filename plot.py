import matplotlib.pyplot as plt
import pandas as pd
import data

def plot(df, name='unknown', save=True):
    for i in range(12): # 0 - 11
        plt.plot(df[i], label=str(i))

    plt.xlabel("Timestamp")
    plt.ylabel("Sensor readings")
    plt.legend()
    
    if save:
        plt.savefig('plots/' + name)
    else:
        plt.show()

    plt.close()


if __name__ == "__main__":
    all_dfs = data.load()
    
    for index, df in enumerate(all_dfs):
        #df.drop(columns=['truth'], inplace=True)

        plot(df, name=str(index))
        print(str(index + 1) + ' / ' + str(len(all_dfs)) + ' DONE') 